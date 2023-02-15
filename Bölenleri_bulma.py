
liste = list()

def bolenleri_bulma(sayı):
    for i in range(1, sayı+1):
        if(sayı % i == 0):
           liste.append(i)
           i += 1

while True:
    sayı = input("Sayı: ")

    if(sayı == "q"):
        break;
    else:
        sayı = int(sayı)
        bolenleri_bulma(sayı)
        print("Tam Bölenler Listesi ", liste)
        break;