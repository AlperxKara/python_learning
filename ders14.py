#MANTIKSAL BAĞLAÇLAR

"""""

print( 5 == 5 or "alper" == "kara")
print( 5 == 5 and "alper" == "alper")


kbilgileri= ["alper", "12345"]

kadi= input("Kullanıcı adını giriniz : ")
sifre= input("Şifrenizi giriniz : ")

a= kbilgileri[0] == kadi and kbilgileri[1] == sifre

print(a)


sayiAl = int(input("Bir sayi giriniz : "))

a = sayiAl % 2 == 0 or sayiAl % 3 == 0 or sayiAl % 5 == 0

print(a)
"""