karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
karakterSayısı = int (input("karakter Sayısını giriniz:"))
parola = ""
import random
for i in range(karakterSayısı):
    rastgeleKarakter = random.choice (karakterler)
    parola += rastgeleKarakter
print (karakterler)   
