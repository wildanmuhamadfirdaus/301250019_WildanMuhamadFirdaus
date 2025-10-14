import random

print('===Game tebak angka===')
print('saya sudah memilih angka antara 1 sampai 20')
print('coba tebak dalam 3 tebakan.')

angka_rahasia = random.randint(1,20)
kesempatan = 3

for i in range(kesempatan):
    tebakan = int(input(f'masukan tebakan anda yang ke-{i+1}: '))

    if tebakan == angka_rahasia:
        print('tebakan kamu benar')
    elif tebakan > angka_rahasia:
        print('terlalu besar')
    else:
        print("terlalu kecil")
else:
    print('maaf kesempatan habis angka yang benar adalah: ' + str(angka_rahasia))


