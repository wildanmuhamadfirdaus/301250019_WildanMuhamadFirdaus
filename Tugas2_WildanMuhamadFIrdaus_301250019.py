a = int(input("Masukkan Bilangannya! "))

if a > 0:
    print("Bilangan Positif")
elif a < 0:
    print("Bilangan Negatif")
else:
    print("Bilangan Nol")

# jika variable a lebih dari 0 maka akan tereksekusi if yang pertama yaitu bilangan positif
# dan jika bilangan kurang dari 0 maka akan teresksekusi elif yaitu bilangan negatif
# terakhir jika variable a nya adalah 0 maka else akan tereksekusi yaitu bilangan nol

b = int(input("Masukkan Nilai Yang Ingin di Konversi! "))

if b >= 85:
    print("A")
elif b >= 70:
    print("B")
elif b >= 55:
    print("C")
elif b >= 40:
    print("D")
else:
    print("E")

# jika variabel b lebih dari sama dengan 85 maka if pertama akan tereksekusi yaitu A
# jika variable b lebih dari sama dengan 70 dan kurang dari sama dengan 84 maka elif pertama akan tereksekusi yaitu b
# jika variable b lebih dari sama dengan 55 dan kurang dari sama dengan 69 maka elif kedua akan tereksekusi yaitu C 
# jika variable b lebih dari sama dengan 40 dan kurang dari sama dengan 54 maka elif ketiga akan terseksekusi yaitu D 
# dan jika variable b bukan kondisi selain yang di atas maka else akan terseksekusi yaitu E

c = int(input("Masukkan Total Belanjanya! "))

if c >= 500000:
    d = 0.20
elif c >= 250000:
    d = 0.10
else:
    d = 0

diskon = int(c * d)
total_bayar = c - diskon

print(f"Total Belanja: Rp {c}")
print(f"Diskon: RP {diskon}")
print(f"Total bayar: Rp {total_bayar}")

# jika variable c lebih dari sama dengan 500000 maka if pertama akan tereksekusi yaitu diskon 20%
# jika variable c lebih dari sama dengan 250000 maka elif akan tereksekusi yaitu diskon 10%
# dan jika variabel c dalam dua kondisi diatas tidak terpenuhi else akan tereksekusi yaitu diskon 0%
