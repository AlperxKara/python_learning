#PRİNT FONKSİYONU VE ÖZELLİKLERİ

""""def faktoriyeAl(sayi):
    faktoriyel = 1
    for i in range(1,sayi + 1):
        faktoriyel = faktoriyel * i
    return faktoriyel

print(faktoriyeAl(5))

print("Alper\nKara") # \n kullanımı alt satıra yazdırır n burada new line anlamına gelir

"""

""""
a = 6
b = "Alper"
c= True

print(a,b,c,sep="X")  #sep verilerin arasına değer ekler
"""

""""a = 6
b = "Alper"
c= True

print(b,end=" -- ") #end özelliği değerin sonuna veri eklemeye yarar.
print(b)
"""

""""
a = 6
b = "Alper"
c= True

print(*b) # * işareti veriyi index olarak tek tek yazmaya yarar"""

""""
isim= "Alper"
soyad="kara"

print("Merhaba Sayın {} {}, sitemize hoş geldiniz".format(isim,soyad)) #{} dışardaki verileri str içinde kullanmamıza yarar
print("Merhaba Sayın %s %s , sitemize hoş geldiniz" %(isim,soyad))  #%s dışardaki verileri str içinde kullanmamıza yarar"""