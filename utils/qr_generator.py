import qrcode
import os

def generate_qr_full(data, save_path="static/qr"):
    os.makedirs(save_path, exist_ok=True)
    qr_text = (
        f"Certificate ID: {data['certificate_id']}\n"
        f"Type: {data['type'].title()} Certificate\n"
        f"Name: {data['name']}\n"
        f"{'DOB' if data['type'] == 'birth' else 'DOD'}: {data['date']}\n"
        f"Gender: {data['gender']}\n"
        f"Place of {'Birth' if data['type'] == 'birth' else 'Death'}: {data['place']}\n"
        f"{'Parent' if data['type'] == 'birth' else 'Relative'}: {data['relative']}\n"
        f"Issuing Authority: {data['authority']}\n"
        f"Issue Date: {data['issue_date']}"
    )
    file_path = os.path.join(save_path, f"{data['certificate_id']}.png")
    qrcode.make(qr_text).save(file_path)
    return file_path

def generate_qr_link(certificate_id, save_path="static/qr"):
    os.makedirs(save_path, exist_ok=True)
    qr_data = f"http://localhost:5000/verify/{certificate_id}"
    file_path = os.path.join(save_path, f"{certificate_id}.png")
    qrcode.make(qr_data).save(file_path)
    return file_path
