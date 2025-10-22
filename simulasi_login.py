username_benar = "admin"
password_benar = "python"

kesempatan = 3
percobaan = 0

while percobaan < kesempatan:
    print(f"percobaan ke- {percobaan + 1}")
    username = input("masukkan username ")
    password = input("masukkan password ")
    if username == username_benar and password == password_benar:
        print("login berhasil")
        break
    else:
        percobaan += 1
        sisa = kesempatan - percobaan
        if sisa > 0:
            print("login gagal!")
        else:
            print("kesempatan kamu udah habis coba lagi besok")

