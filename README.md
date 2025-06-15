![Screenshot 2025-06-15 213048](https://github.com/user-attachments/assets/17a7f5ea-f8d2-42df-b500-ec1e38196537)# Automated-Certificate-Generator
# 🧾 Birth & Death Certificate Generator Automation

An automated system that simulates an **e-Governance module** used in municipal systems to generate digitally verifiable **Birth** and **Death Certificates** from structured user data. Built using Python and HTML templates with optional QR code integration, this project streamlines certificate creation with form-based data input and secure PDF generation.

---

## 🎯 Objective

To design and implement a mini application that:
- Collects relevant information via form/CLI.
- Generates formatted, printable Birth or Death certificates.
- Includes certificate validation mechanisms like auto-generated IDs and QR codes.
- Mimics real-world municipal workflows for official documentation.

---

## ✅ Key Features

- 🧍‍♂️ **Form-based data input**
- 📜 **PDF generation** using styled certificate templates
- 🆔 **Auto-generated certificate numbers** and date of issue
- 🔍 **Optional QR Code** for digital verification
- 🔐 Basic **security practices** in certificate handling

---

## 🧰 Tools & Technologies Used

| Component         | Details                                           |
|------------------|---------------------------------------------------|
| Language          | Python 3.x                                        |
| PDF Libraries     | `FPDF`, `ReportLab`                               |
| QR Code           | `qrcode` (optional)                               |
| Templates         | HTML + CSS-based or PDF-based templates           |
| Data Input        | CLI / HTML Form / CSV                             |
| Editor            | VS Code or any IDE                                |

---

## 🗃️ Folder Structure
CertificateGenerator/
├── templates/
│ ├── birth_certificate_template.html
│ ├── death_certificate_template.html
│
├── static/
│ ├── fonts/
│ ├── logos/
│ └── bg_images/
│
├── data/
│ └── sample_input.csv
│
├── output/
│ ├── sample_birth_output.pdf
│ └── sample_death_output.pdf
│
├── qr_utils.py # QR code generation module (optional)
├── generate_certificate.py # Main certificate generation logic
├── config.py # Configuration and paths
├── README.md
└── requirements.txt


---

## 🖼️ Output Previews

### 🍼 Birth Certificate Sample

> Replace the image below with the actual output image of the `.html` rendered birth certificate PDF.

![Birth Certificate](output_images/birth_certificate_output.png)

---

### ⚰️ Death Certificate Sample

> Replace the image below with the actual output image of the `.html` rendered death certificate PDF.

![Death Certificate](output_images/death_certificate_output.png)

---

## 🧑‍💼 Certificate Fields

| Field               | Birth Certificate              | Death Certificate              |
|--------------------|-------------------------------|--------------------------------|
| Certificate No.     | Auto-generated                | Auto-generated                 |
| Full Name           | Name of Child                 | Name of Deceased               |
| Date                | Date of Birth (DOB)           | Date of Death (DOD)            |
| Gender              | Male / Female / Other         | Male / Female / Other          |
| Place of Event      | Place of Birth                | Place of Death                 |
| Parent/Relative     | Father/Mother Name            | Relative Name (e.g., Son of…)  |
| Issuing Authority   | Registrar/Medical Officer     | Registrar/Medical Officer      |
| QR Code (optional)  | Yes                           | Yes                            |

---

## 🚀 How to Run the Project

### 1. Clone the Repository

bash
git clone https://github.com/yourusername/certificate-generator.git
cd certificate-generator

### 2. Install Requirements
pip install -r requirements.txt

### 3. Add Your Data
prepare a CSV with column like:
name,dob/dod,gender,place,parent/relative,address,registration_no,authority,type

Example:
John Doe,2000-12-15,Male,Pune,Robert Doe,MG Road,REG2025001,Dr. Sharma,birth

### 4. Run the Script
python generate_certificate.py
Certificates will be auto-generated and saved in the output/ folder.

## 🔒 Security Features (Optional)
✅ Unique Certificate Numbers (auto-generated)

✅ QR Code containing encoded certificate data or linking to a verification URL

✅ Audit trail (save logs of issued certificates)

## 💡 Future Enhancements
🔗 Integration with a web form (HTML/PHP)

🧾 Email dispatch of certificates

🖨️ Print-ready layout styling

📂 Database storage using SQLite or MySQL

🌐 Online verification portal


## 📚 References
FPDF Documentation

ReportLab PDF Guide

QR Code Python Library


## 📸 Screenshot Section

Form/CLI interface:
![Screenshot 2025-06-15 205441](https://github.com/user-attachments/assets/d5538dc0-d0b2-420b-8e45-912f4c048631)
![Screenshot 2025-06-15 205456](https://github.com/user-attachments/assets/11ca80f5-7f82-46fd-a775-c505a1bddca4)
![Screenshot 2025-06-15 205523](https://github.com/user-attachments/assets/725bddd9-b50e-44bc-b5b1-2964ee62ee43)
![Screenshot 2025-06-15 205720](https://github.com/user-attachments/assets/473a37eb-0985-4a87-8679-a85edec2ca0c)
![Screenshot 2025-06-15 205732](https://github.com/user-attachments/assets/b4622bb8-77b8-486b-ba40-bbe417f11374)
![Screenshot 2025-06-15 205853](https://github.com/user-attachments/assets/f0950cba-8f4f-431f-aff0-0d129327ef29)

Sample birth certificate (PDF/HTML screenshot)
![Screenshot 2025-06-15 213057](https://github.com/user-attachments/assets/52ee32d4-6030-4863-a987-2cde03e67682)

Sample death certificate (PDF/HTML screenshot)
![Screenshot 2025-06-15 213048](https://github.com/user-attachments/assets/1e0809c0-1689-4117-b652-a61c09de67d0)


## 👨‍💻 Contributors
Nikhil Rokade – Python Developer
