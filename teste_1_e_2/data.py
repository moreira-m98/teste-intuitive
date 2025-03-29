import pdfplumber
import csv
import zipfile
import os

pdf_path = "../Anexo_I.pdf"
csv_path = "../Anexo_I_Rol_2021.csv"
zip_filename = "../Teste_Matheus.zip"

data = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                if any(row):
                    data.append([cell.replace("\n", " ") if cell else "" for cell in row])

if data:
    header = data[0]
    header = [col.replace("OD", "Seg. Odontológica").replace("AMB", "Seg. Ambulatorial") for col in header]
    data[0] = header

with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

if os.path.exists(csv_path):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))
    print(f'Arquivo ZIP criado: {zip_filename}')
else:
    print(f'Erro: O arquivo CSV "{csv_path}" não foi encontrado.')
