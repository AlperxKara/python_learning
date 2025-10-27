#RANGE()

"""
Range kullanımı 3 farklı şekildedir.
1- range(parametre:bitis)
2- range(parametre:baslangic,parametre:bitis)
3- range(parametre:baslangic,parametre:bitis,parametre:atlama)
"""

"""for sayi in range(10_000):
    print(sayi)
"""
"""
for x in range(1,1001):
    print(x)
"""

"""
for x in range(100,1000,10):
    print(x)
"""

#ÖRNEK KULLANICIDAN SAYI AL VE BU SAYIYA 1 DEN SAYIYA KADAR YAZDIR ASAL OLANLARI YAZDIR

sayi = int(input("Bir Sayi Giriniz: "))

sayac = 2

asal_sayilar = []

while sayi >0:
    asal_sayilar.append(sayi)
    while sayac<sayi:
        if sayi % sayac ==0:
            asal_sayilar.remove(sayi)
            break
        sayac +=1
    sayac = 2
    sayi -=1
print(asal_sayilar)