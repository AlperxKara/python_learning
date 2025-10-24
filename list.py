#Liste Veri Tipleri
ogrenciler = ["Melike", "Mahmut","Umut","Tolga","Ela","Mert","Ziya","Turgut","Ece","Asli","Kerem"]
ogrenciler2 = ["Ali", "Veli", "Eda"]
""""

a= list()

b=[]

print(type(b))
"""


""""print(ogrenciler[2]) # İndex numarasına göre listedeki veriyi yazdırır"""

""""
for ogrenci in ogrenciler:
    print(ogrenci) #Tüm Öğrencileri Yazdırır
"""

""""
Listeden Veri Kaldırma
ogrenciler.remove("Mert")
print(ogrenciler)
"""

""""
ogrenciler = ogrenciler + ogrenciler2  #listeleri toplar ve sonuna ekler

print(ogrenciler)
"""

""""
liste= [1,2,3]

liste.append("Alper") # Append Listeye eleman ekler 

print(liste)
"""

""""
liste= [1,2,3]

liste.pop() # Pop Listeden eleman çıkarır

print(liste)
"""

""""
kullanicilar= ["Alper", "Ferit", "Yusuf"]
sifre = ["123456","78910","123123"]

users=[kullanicilar,sifre]

print(users[0][0],users[1][0],users[0][1],users[1][1])
"""