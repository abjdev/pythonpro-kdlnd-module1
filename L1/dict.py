meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            
            }

while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word in meme_dict.keys():
        print(f"Kelimenizin anlamı: {meme_dict[word]}")
    elif word == "liste":
        print(meme_dict)
    else:
        print("ben de bilmiyorum.")
        addinp = input("Bu kelimeyi sözlüğe eklemek ister misin?")
        if addinp == "evet" or addinp == "Evet" or addinp == "EVET":
            desc = input("Anlamı ne?")
            meme_dict[word] = desc
        else:
            continue
print("Baybay!")