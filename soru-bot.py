import json

# Soru JSON verisini yükle
with open('soru.json', 'r', encoding='utf-8') as f:
    soru_json = json.load(f)

while True:
    # Her soru ve seçenekleri ekrana yazdır
    for soru in soru_json:
        print(soru['soru'])
        for cevap in soru['cevaplar']:
            print(cevap)

        # Kullanıcının cevabını al
        kullanici_cevabi = input("Cevabınızı girin (A, B, C veya D) veya çıkmak için 'q' basın: ").upper()

        if kullanici_cevabi == 'Q':
            print("Programdan çıkılıyor...")
            exit()

        # Doğru cevabı kontrol et
        if kullanici_cevabi == soru['dogruCevap']:
            print("Tebrikler, doğru cevap!")
        else:
            print("Maalesef, yanlış cevap. Lütfen cevabınızı gözden geçirmenizi öneririm. Çünkü, Doğru cevap: " + soru['dogruCevap'])+" seçeneğidir"

print("Programdan çıkıldı.")
