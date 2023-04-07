import json

# Kullanıcıdan kaç soru eklemek istediğini alalım
num_sorular = int(input("Kaç soru eklemek istiyorsunuz? "))

# Boş bir soru listesi oluşturalım
soru_listesi = []

# Kullanıcıdan soruları ve cevapları alalım ve soru listesine ekleyelim
for i in range(num_sorular):
    soru = input(f"{i+1}. soru: ")
    cevapA = input("A) ")
    cevapB = input("B) ")
    cevapC = input("C) ")
    cevapD = input("D) ")
    dogruCevap = input("Doğru cevap (A/B/C/D): ")
    
    # Oluşturduğumuz sözlüğü soru listesine ekleyelim
    soru_listesi.append({
        "soru": soru,
        "cevaplar": [f"A) {cevapA}", f"B) {cevapB}", f"C) {cevapC}", f"D) {cevapD}"],
        "dogruCevap": dogruCevap
    })

# Son olarak, soru listesini JSON dosyasına yazdıralım
json_dosyasi = input("JSON dosyasının adı: ")
with open(json_dosyasi, "w") as f:
    json.dump(soru_listesi, f)
    
print("JSON dosyası başarıyla oluşturuldu!")
