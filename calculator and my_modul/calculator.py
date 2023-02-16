import math_modul
print("""
İşlemler: 

1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme 
""")

islem = input("Yapmak istediğiniz işlemi seçiniz: ")

a = int(input("İşlem Yapacağınız Birinci Sayı: "))
b = int(input("İşlem Yapacağınız İkinci Sayı: "))

while True:
    if islem == "1":
        print(math_modul.toplama(a,b))
        break;
        
    elif islem == "2":
        print(math_modul.cıkarma(a,b))
        break;

    elif islem == "3":
        print(math_modul.carpma(a,b))
        break;

    elif islem == "4":
        print(math_modul.bolme(a,b))
        break;

    else:
        print("Böyle bir işlem bulunmamaktadır.")
        break;