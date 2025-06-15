from fpdf import FPDF
import os
from datetime import datetime

class CertificatePDF(FPDF):
    def header(self):
        pass  # No header; using background image

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f"Issued on {datetime.now().strftime('%d-%m-%Y')}", 0, 0, 'C')

def generate_certificate(data, qr_path, save_folder="logs"):
    os.makedirs(save_folder, exist_ok=True)

    pdf = CertificatePDF("L", "mm", "A4")
    pdf.add_page()

    # Load the correct background template
    template_img = f"cert_templates/{data['type']}_template.png"
    if os.path.exists(template_img):
        pdf.image(template_img, x=35, y=0, w=240, h=190)

    # Text formatting
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=44)

    # Align just the entries (no labels)
    y = 45
    row_gap = 17

    fields = [
        data['certificate_id'],
        data['name'],
        data['date'],
        data['gender'],
        data['place'],
        data['relative'],
        data['authority']
    ]

    for value in fields:
        pdf.set_xy(140, y)
        pdf.set_font("Arial", '', 22)
        pdf.cell(0, 22, value)
        y += row_gap

    # Add QR Code at bottom-right
    pdf.image(qr_path, x=49, y=139, w=31)

    # Save the PDF
    filename = f"{data['certificate_id']}_{data['type']}.pdf"
    output_path = os.path.join(save_folder, filename)
    pdf.output(output_path)
    return output_path
