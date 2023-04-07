# soru-cevap
Bu kod, bir "docx" adlı belgedeki soruları ve cevaplarını alarak, bir "json" adlı dosyaya yazıyor.

Öncelikle, program kullanıcıdan bir "docx" dosyası adı istiyor. Bu dosya, programın çalışması için gerekli olan belgedir.

Sonra, program belgedeki metinleri alıyor ve soruların ve cevapların listelerini oluşturuyor.

Her bir soru, bir "soru" anahtar kelimesi ile başlayan ve bir soru işareti ile biten bir metin parçasıdır. Bu metin parçası, bir "soru" adlı sözlükte saklanır.

Her bir cevap, "A)", "B)", "C)" veya "D)" ile başlayan bir metin parçasıdır. Bu metin parçası, "cevaplar" adlı bir liste içine eklenir.

Doğru cevap, "Doğru Cevap:" ile başlayan bir metin parçasıdır. Bu metin parçası, "dogruCevap" adlı bir sözlük anahtarına sahip sorunun altında saklanır.

En sonunda, program bir "json" adlı dosyaya soruların ve cevapların listesini yazıyor. Bu dosya, başka bir program tarafından okunabilir veya bir web sitesinde kullanılabilir.




Bu kod, kullanıcının kaç tane soru eklemek istediğini sorduktan sonra, kullanıcıdan soruları, cevapları ve doğru cevabı alır. Ardından, bu bilgileri bir sözlükte saklar ve tüm soruları bir soru listesinde saklar. Son olarak, soru listesini bir JSON dosyasına yazdırır.

Yani, bu kod, insanların bir sınav oluşturmasına yardımcı olmak için yazılmıştır. İnsanlar bu kodu kullanarak, sınav sorularını ve cevaplarını kaydedebilirler. Daha sonra, bu soruları bir JSON dosyasında saklayabilirler, böylece başka bir bilgisayarda veya programda da kullanabilirler.





Bu Python kodu, kullanıcının bir JSON dosyasındaki soruları yanıtlamasını sağlayan bir quiz programıdır. Programın başında, kullanıcının kaç soru eklemek istediğini belirlediği ve bu soruları soru listesine eklediği bir döngü bulunur. Daha sonra, bu sorular rastgele bir şekilde karıştırılır ve kullanıcıya sırayla gösterilir.

Kullanıcının cevabını alındıktan sonra, cevap doğruysa tebrik edilir ve yanlışsa kullanıcıya doğru cevap gösterilir. Program, tüm soruları yanıtladıktan sonra kullanıcıya yeniden oynamak isteyip istemediğini sorar ve kullanıcının cevabına göre tekrar oynanabilir veya programdan çıkılır.

Bu programın özellikleri arasında, kullanıcının yanıtları yanlışsa doğru cevapları görebilmesi, tüm soruları yanıtladıktan sonra yeniden oynama seçeneği sunulması ve kullanıcının programdan çıkma seçeneği bulunması yer almaktadır. Ayrıca, soruların JSON dosyasından yüklenmesi, soruların rastgele bir şekilde karıştırılması ve kullanıcının cevaplarının büyük harf/küçük harf duyarlı olması gibi özellikler de vardır.
