def sayilariTopla(*degerler):
    toplam=0
    for deger in degerler:
        toplam += deger
    
    return toplam

sayilar = [x for x in range(1,1001)]

print(sayilariTopla(*sayilar)) 

# * işareti, listedeki elemanları tek tek fonksiyona argüman olarak geçirmeyi sağlar.
# Yani *sayilar ifadesi, [1, 2, 3] listesini sayilariTopla(1, 2, 3) şeklinde aktarır.
