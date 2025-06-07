import os
import pandas as pd
from PyPDF2 import PdfReader

# 📂 Ścieżka do folderu z plikami PDF
folder_path = "ścieżka/do/folderu/z/pdfami"  # ← ZMIEŃ to na lokalny folder z PDF-ami

# 📦 Lista danych do eksportu
articles = []

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            articles.append({
                "title": filename.replace(".pdf", ""),
                "body": text.strip(),
                "folder": "Baza wiedzy CS",  # Możesz zmienić nazwę folderu
                "tags": ""  # Dodaj tagi jeśli potrzebujesz
            })
        except Exception as e:
            print(f"❌ Błąd w pliku {filename}: {e}")

# 💾 Zapis do CSV
df = pd.DataFrame(articles)
df.to_csv("baza_wiedzy.csv", index=False, encoding="utf-8")

print("✅ Gotowe! Zapisano plik: baza_wiedzy.csv")
