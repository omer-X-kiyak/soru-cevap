import docx
import json

# Kullanıcıdan docx dosyası adını al
docx_file = input("Docx dosya adını girin (örn: sorular.docx): ")

# Docx dosyasını aç
doc = docx.Document(docx_file)

# Tüm metinleri bir listede birleştir
doc_text = [para.text.strip() for para in doc.paragraphs if para.text.strip()]

# Soru ve seçenekleri JSON dosyasına yazdır
soru_json = []
soru = {}

for text in doc_text:
    if text.endswith("?"):
        # Yeni bir soru başlat
        if soru:
            soru_json.append(soru)
        soru = {"soru": text.strip(), "cevaplar": []}
    elif text.upper().startswith("A)"):
        soru["cevaplar"].append(text.strip())
    elif text.upper().startswith("B)"):
        soru["cevaplar"].append(text.strip())
    elif text.upper().startswith("C)"):
        soru["cevaplar"].append(text.strip())
    elif text.upper().startswith("D)"):
        soru["cevaplar"].append(text.strip())
    elif text.startswith("Doğru Cevap:"):
        soru["dogruCevap"] = text.strip().split(":")[1].strip().upper()

# Son soruyu JSON listesine ekle
soru_json.append(soru)

# JSON dosyasına yazdır
json_file = input("JSON dosya adını girin (örn: sorular.json): ")
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(soru_json, f, ensure_ascii=False, indent=4)

print("JSON dosyası başarıyla oluşturuldu!")
