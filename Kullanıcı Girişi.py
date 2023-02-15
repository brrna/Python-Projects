print("""
*************** Sisteme Giriş ***************""")

s_kullanıcı_adı = "Berna"
s_parola = "1234"
giriş_hakkı = 3


while True:
    kullanıcı_adı = input("Kullanıcı Adı: ")
    parola = input("Parola: ")

    if(s_kullanıcı_adı != kullanıcı_adı and s_parola == parola):
        print("Kullanıcı Adı Hatalı")
        giriş_hakkı -= 1
    elif(s_kullanıcı_adı == kullanıcı_adı and s_parola != parola):
        print("Parola Hatalı")
        giriş_hakkı -= 1
    elif(s_kullanıcı_adı != kullanıcı_adı and s_parola != parola):
        print("Kullanıcı Adı ve Parola Hatalı")
        giriş_hakkı -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı.")
        break;
    if(giriş_hakkı == 0):
        print("Giriş Hakkınız bitti")
        break;