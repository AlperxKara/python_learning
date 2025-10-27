def ogrenci_yazdir():
    print("******** BAŞARI DURUMU HESAPLAMA **********")

    isim = input("Öğrencinin Adı : ")
    soyad = input("Öğrencinin Soyadı : ")
    vize = float(input("Öğrencinin Vize Notunu Giriniz : "))
    final = float(input("Öğrencinin Final Notunu Giriniz : "))

    basariPuani = vize * 0.4 + final * 0.6
    print(f"Başarı Puanı: {basariPuani}")

    if basariPuani >= 85:
        harf_notu = "AA"
    elif basariPuani >= 70:
        harf_notu = "BA"
    elif basariPuani >= 60:
        harf_notu = "BB"
    elif basariPuani >= 50:
        harf_notu = "CB"
    elif basariPuani >= 40:
        harf_notu = "CC"
    else:
        harf_notu = "FF"

    with open("notlar.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"{isim} {soyad} adlı öğrencinin bu derste elde ettiği harf notu: {harf_notu}\n")


kac_ogrenci = int(input("Kaç öğrenci gireceksiniz : "))

for i in range(kac_ogrenci):
    ogrenci_yazdir()
