#LIST COMPREHENSION 
"""sayilar =[]
for i in range(1, 25):
    if i % 2 == 0 and i % 3 == 0:
        sayilar.append(i)
print(sayilar)"""

sayilar = [x for x in range(1,100) if x % 2 ==0 and x % 3 == 0]

print(sayilar)