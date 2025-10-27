#Senaryo 1 Kullanıcıdan pozitif tam sayı al, sayının faktöriyelini alıp ekranda göster örneğin "Kaç faktöriyel - 5 - 5!= 120"

"""sayi= int(input("Pozitif tam sayı giriniz (Pozitif olmayan değerler kabul edilmeyecektir) : "))

faktoriyel = 1
for i in range(1,sayi+1):
    faktoriyel = faktoriyel * i
   
print(faktoriyel)"""

#Senaryo 2 Kullanıcının hesapında 2000tl para var kartı atm ye terleştirdiğinden itibaren sonsuz döngüye girecek, 1. işlem para çekme 2. işlem para yatırma, 3. işlem kart bilgileri, 4. İşlem kart iade

sahipOlunanPara= 2000
kullanıcı = "Alper Kara"

secim= input("Kartı sokmak için 's' çıkarmak için 'a' yazınız : ")

if secim == "s":
    while True:
        islem = int(input("""
        İşlemler
        -----------
        1- Para Çekme
        2- Para Yatırma
        3- Kart Bilgileri
        4- Kart İade
        Yapmak istediğiniz işlemin numarasını giriniz: 
"""))
        if islem ==1:
          cekilmekİstenenTutar = int(input("Çekmek istediğiniz tutarı giriniz: "))
          if sahipOlunanPara < cekilmekİstenenTutar:
              print("Yetersiz bakiye")
          else:
              sahipOlunanPara-=cekilmekİstenenTutar                    
        if islem == 2:
            eklenenTutar = int(input("Eklemek istediğiniz tutarı yazınız: "))
            sahipOlunanPara+=eklenenTutar              
        
        if islem == 3:
            print("Merhaba {}, mevcut bakiyeniz :  {}".format(kullanıcı,sahipOlunanPara))


        if islem == 4:
            print("Kartı iade aldınız ATM den ayrılabilrisiniz.")
            break

else:
    print("ATM'den ayrıldınız")