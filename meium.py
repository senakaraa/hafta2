def buyuk_harfe_cevir(kelime):
    return kelime.upper()

try:
    kullanici_kelimesi = input("Lütfen bir kelime girin: ")
    buyuk_harfler = buyuk_harfe_cevir(kullanici_kelimesi)
    print("Kelimenin büyük harf hali:", buyuk_harfler)
except Exception as e:
    print("Bir hata oluştu:", e)
