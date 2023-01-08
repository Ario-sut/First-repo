member = input("apakah customer punya member? : ")
if member == "ya":
    age = int(input("Masukan umur : "))
    if age >= 17:
        money = int(input("Uang = Rp"))
        alkohol = 50000
        jus = 20000
        if money >= alkohol:
            print("bisa beli alkohol")
        elif jus <= money < alkohol:
            print("bisa beli jus")
        else:
            print("bokek")
    else:
        money = int(input("Uang = Rp"))
        jus = 20000
        if money >= jus:
            print("bisa beli jus")
        else:
            print("bokek")
else:
    print("Anda dilarang masuk")




