weight = int(input("Masukkan berat badan Anda : "))
tipe = input("lbs(L) atau kg(K) : ")

kg = weight / 2.20462
lbs = weight * 2.20462

if (tipe == 'K'):
    print(kg)
else:
    print(lbs)

