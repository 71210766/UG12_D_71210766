Bil1 = int(input("Masukkan awal deret: "))
Bil2 = int(input("Masukkan akhir deret: "))

x = []

if (Bil1 + 1) % 2 == 0:
     for i in range (Bil1 + 1, Bil2, 2):
         if i % 3 == 0 or i % 7 == 0: continue
         print ( i, end = " " )
else:
     for i in range (Bil1, Bil2, 2):
         if i % 3 == 0 or i % 7 == 0 : continue
         print (i, end = " ")