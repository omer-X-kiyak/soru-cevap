import json
import random

# Sorular json dosyasında bu yüzden json dosyasındaki soruları alalım
with open('soru.json', 'r', encoding='utf-8') as f:
    soru_json = json.load(f)

def yeniden_oyna():
    while True:
        cevap = input("Tüm soruları yanıtladınız. Yeniden oynamak istiyor musunuz? (E/H)").upper()
        if cevap == "E":
            return True
        elif cevap == "H":
            print("Programdan çıkılıyor...")
            return False
        else:
            print("Lütfen geçerli bir cevap verin (E/H).")

while True:
    # Soruları rastgele bir şekide yeniden düzenle
    random.shuffle(soru_json)

    # soruları ve cevapları ekrana bastır
    for soru in soru_json:
        print(soru['soru'])
        for cevap in soru['cevaplar']:
            print(cevap)

        # Kullanıcının cevabını al
        kullanici_cevabi = input("Cevabınızı girin (A, B, C veya D) veya çıkmak için 'q' basın: ").upper()

        if kullanici_cevabi == 'Q':
            print("Programdan çıkılıyor...")
            exit()

        # cevabı kontrol et
        if kullanici_cevabi == soru['dogruCevap']:
            print("Tebrikler, doğru cevap!")
        else:
            print("Maalesef, yanlış cevap. Lütfen cevabınızı gözden geçirmenizi öneririm. Çünkü, Doğru cevap: " + soru['dogruCevap'])

    # Tüm soruları yanıtladıktan sonra kullanıcıya yeniden oynamak isteyip istemediğini soralım
    if not yeniden_oyna():
        break

print("Programdan çıkıldı.")
