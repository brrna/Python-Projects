# fibonacci başlangıçları yapıldı
a = 1
b = 1

#fibonacci serisi içiçn dizinin tanımlaması yapıldı
fibonacci = [a,b]

# 20 elemanlı dizi olmasını tanımladık
for i in range(20):

    #eski elemanlara yeni değerleri atandı
    a,b = b,a+b

    #yeni değeri listeye ekledik
    fibonacci.append(b)

print(fibonacci)