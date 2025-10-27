#BREAK & CONTUNIE

#Break var olduğu dögünün doğruluk değeri ne olursa olsun sonlandırır Örneğin:
#Continue Döngü o turdaki kalan kodları atlar ve bir sonraki döngü turunun başına gider.
while True:
    sayi = int(input("Sayıyı giriniz (Eğer tek sayı girerseniz ekrana yazdırılmayacak) : "))
    if sayi % 2 == 1:
        continue
    
    print(sayi)

 
 
"""  
   sayi = int(input("Bir sayi giriniz (Eğer tek sayi girerseniz dongu sonlanacak) : "))
    if sayi % 2 == 1:
        break
    
    print("Döngünün sonu")
    
print("Döngü bloğunun dışı")
"""


