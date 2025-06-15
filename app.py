from flask import Flask, render_template, request, Response
from datetime import datetime
import uuid
import os
import csv

# Local utilities
from utils.qr_generator import generate_qr_full
from utils.pdf_generator import generate_certificate
from database.db import get_db

app = Flask(__name__)

# ------------------ ROUTES ------------------

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/user')
def user_page():
    return render_template("user.html")

@app.route('/form/<type>')
def form_page(type):
    if type not in ['birth', 'death']:
        return "Invalid certificate type", 400
    return render_template("index.html", cert_type=type)

@app.route('/generate', methods=['POST'])
def generate_certificate_route():
    try:
        data = {
            "type": request.form.get('type', 'birth'),
            "name": request.form['name'],
            "date": request.form['date'],
            "gender": request.form['gender'],
            "place": request.form['place'],
            "relative": request.form['relative'],
            "authority": request.form['authority'],
            "certificate_id": str(uuid.uuid4())[:8],
            "issue_date": datetime.now().strftime("%Y-%m-%d")
        }

        # Step 1: Generate QR Code with certificate data
        qr_path = generate_qr_full(data)

        # Step 2: Generate Certificate PDF
        save_folder = f"logs/{data['type']}"
        cert_path = generate_certificate(data, qr_path, save_folder)

        # Step 3: Save to MongoDB
        try:
            db = get_db()
            if db:
                db.certificates.insert_one(data)
                print("Saved to MongoDB.")
            else:
                raise Exception("MongoDB connection failed.")
        except Exception as e:
            print(f"MongoDB error: {e}")
            # Fallback: Save to CSV
            csv_file = "certificate_log.csv"
            fieldnames = list(data.keys())
            file_exists = os.path.exists(csv_file)

            with open(csv_file, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(data)
            print("Saved to CSV.")

        return render_template("result.html", data=data, cert_path=cert_path)

    except Exception as e:
        print(f"Error generating certificate: {e}")
        return "An error occurred while generating the certificate.", 500

@app.route('/verify/<certificate_id>')
def verify_certificate(certificate_id):
    try:
        db = get_db()
        result = db.certificates.find_one({"certificate_id": certificate_id})
    except Exception as e:
        print("MongoDB error:", e)
        result = None

    if result:
        return render_template("verify.html", data=result)
    else:
        return render_template("verify.html", data=None, error="Certificate not found.")

@app.route('/admin')
def admin_dashboard():
    try:
        db = get_db()
        cert_type = request.args.get("type")
        export = request.args.get("export")

        query = {"type": cert_type} if cert_type in ["birth", "death"] else {}
        records = list(db.certificates.find(query))

        if export == "csv":
            # Create CSV response
            keys = ["certificate_id", "type", "name", "date", "gender", "place", "relative", "authority", "issue_date"]
            csv_data = ",".join(keys) + "\n"
            for rec in records:
                csv_data += ",".join(str(rec.get(k, "")) for k in keys) + "\n"

            return Response(
                csv_data,
                mimetype="text/csv",
                headers={"Content-Disposition": "attachment;filename=certificates.csv"}
            )

    except Exception as e:
        print("MongoDB error:", e)
        records = []

    return render_template("admin.html", records=records)

# ------------------ MAIN ------------------

if __name__ == '__main__':
    app.run(debug=True)
