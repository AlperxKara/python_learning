""""
def kareAl(a):
    return a**2

sayi = int(input("Bir Sayı Giriniz: "))
print(kareAl(sayi))
"""

print("***** HESAP MAKİNESİ *****")

sayi1 = int(input("Birinci Sayıyı Giriniz:"))
sayi2 = int(input("İkinci sayıyı giriniz: "))

secenek= int(input("1-Topla\n2-Çıkar\n3-Çarp\n4-Böl"))

if secenek == 1:
    print(sayi1+sayi2)
elif secenek ==2:
    print(sayi1-sayi2)

elif secenek ==3:
    print(sayi1*sayi2)

else:
    print(sayi1/sayi2)

