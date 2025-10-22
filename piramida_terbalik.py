for i in range(5,0,-1):
    print('*' * i)


bilangan = int(input("masukan angka bilangan nya "))
index = 1
n = int(input("masukan angka pangkat nya "))
while index <= n:
    i = bilangan ** index
    print(i)
    index += 1



