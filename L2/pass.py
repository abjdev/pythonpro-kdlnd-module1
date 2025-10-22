import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunglugu = int(input("Şifre kaç karakterli olsun? (Sadece sayı belirtin.): "))

sifre = ""
for i in range(sifre_uzunglugu):
    sifre += random.choice(karakterler)
    
print("Şifreniz:", sifre)