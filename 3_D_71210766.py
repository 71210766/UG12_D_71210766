bilangan = int(input("Masukkan Angka: "))
print()


for i in range (bilangan) :
    for j in range (bilangan,i,-1) :
        print(" ",end = "")
    for j in range (2*i+1) :
        print("*", end = "")
    print()


for i in range (bilangan-1,-1,-1) :
    for j in range (bilangan,i,-1) :
        print( " ",end = "")
    for j in range (2*i+1) :
        print("*",end = "")
    print()