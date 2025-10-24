# VERİ DÖNÜŞÜMLERİ

a = 5.42

print(type(a)) # type bize değişkenin veri tipini verir

print(type(int(a))) # buradaki int(a) kullanımı veri tipini değiştirir

#ÖRNEK

b = "500"

print(int(b)+200)

#ÖRNEK

sayi = 1234561265

print(len(str(sayi)))

#HESAP MAKİNESİ

c = int(input("sayi1: "))
d = int(input("sayi2: "))

secenek = int(input("1-topla\n2-cikar\n3-carp\n4-bol"))

if secenek == 1:
    print(c+d)
elif secenek ==2:
    print(c-d)
elif secenek ==3:
    print(c*d)
else: 
    print(c/d)
