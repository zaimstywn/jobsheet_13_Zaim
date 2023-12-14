secret_number = 9
guess_count = 0
guess_limit = 3

print("Game menebak angka")
while guess_count < guess_limit:
    User = int(input("Masukkan tebakan angka : "))
    if User == secret_number:
        print("Anda berhasil menebak Angka")
        break
    else:
        print("Salah, masukkan lagi")
        guess_count += 1
else:
    print("Kesempatan menebak Anda habis")
