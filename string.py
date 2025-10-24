yazi = "Alper Kara"

print(yazi[0]) #index numarasına göre seçim
print(yazi[0:5]) #index numraları ile aralık alma slice yöntemi

#örnek

instagram_takipcileri = "Mahmut :200,Esra:100,Ali:90,tehlikelicocuk:2000,Ela:150,Tolga:120"

isim = "Ali"
isim_uzunluk = len(isim)

print(instagram_takipcileri[instagram_takipcileri.find("Ali")+isim_uzunluk:instagram_takipcileri.find("Ali")+isim_uzunluk+3])

print(len(instagram_takipcileri)) #len karakter sayısını verir

#ÖRNEK

kullanici_adi="Alperr"

if len(kullanici_adi)< 6:
    print("Kullanıcı adı 6 karakterden az olamaz")
else: print(kullanici_adi)