#Bir dik üçgenin a ve b değerini alıp hipotenüsünü hesaplama
import math
""""
print("****** Hipotenüs Hesapla ******")

kenar1 = int(input("Dik Üçgen Kenar 1: "))
kenar2 = int(input("Dik Üçgen Kenar 2: "))

sonuc = math.sqrt(kenar1**2+kenar2**2)

print(sonuc)
"""


""""
print("******** Akım Bulma ***********")

v= float(input("Gerilim Değeri: "))
r=float(input("Direnç Değeri: "))

i=v/r

print("Akım Değeri =  {}".format(i))
"""

print("***** SÖZLÜK YAPISI ******")

kelimeler = dict()

ingKelime= input("Öğrendiğiniz kelimeyi yazınız: ")
karsilik= input("Türkçe Karşılığını yazınız: ")

kelimeler[ingKelime] = karsilik

ingKelime= input("Öğrendiğiniz kelimeyi yazınız: ")
karsilik= input("Türkçe Karşılığını yazınız: ")

kelimeler[ingKelime] = karsilik

ingKelime= input("Öğrendiğiniz kelimeyi yazınız: ")
karsilik= input("Türkçe Karşılığını yazınız: ")

kelimeler[ingKelime] = karsilik

ingKelime= input("Öğrendiğiniz kelimeyi yazınız: ")
karsilik= input("Türkçe Karşılığını yazınız: ")

kelimeler[ingKelime] = karsilik

ingKelime= input("Öğrendiğiniz kelimeyi yazınız: ")
karsilik= input("Türkçe Karşılığını yazınız: ")

kelimeler[ingKelime] = karsilik

print(kelimeler)