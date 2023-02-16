# random sayılar üretilmesi gerektiği için
import random

# oyun içinde zaman fonksiyonu kullanacağımız için
import time

print("""
Sayı Tahmin Oyunu

1'den 50'ye kadar olan sayıyı tahmin etmeye çalışılacak.

""")

rastgele_sayi = random.randint(1, 50)
tahmin_hakki = 5

while True:
    tahmin = int(input("Sayı: "))
    
    if(tahmin < rastgele_sayi):
        print("Kontrol ediliyor...")
        time.sleep(1) # 1 saniye bekleticek
        print("Daha büyük bir sayı seçiniz.")
        tahmin_hakki -= 1

    elif (tahmin > rastgele_sayi):
        print("Kontrol ediliyor...")
        time.sleep(1) # 1 saniye bekleticek
        print("Daha küçük bir sayı seçiniz.")
        tahmin_hakki -= 1

    else:
        print("Kontrol ediliyor...")
        time.sleep(1) # 1 saniye bekleticek
        print("Seçtiğiniz sayı doğru. Tebrikler!")
        break;

    if tahmin_hakki == 0:
        print("Tahmin hakkınız bitti.")
        break;