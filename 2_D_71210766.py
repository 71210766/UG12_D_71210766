A = input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: ")
Senin = ("kelas ke-1 Algorima Graf", "kelas ke-3 Sistem Operasi", "kelas ke-4 PAK")
Selasa = ("kelas ke-2 Matematika Teknik", "kelas ke-4 Bhs Indonesia", "kelas ke-6 PKN")
Rabu = ("kelas ke-2 Sistem Basis Data", "kelas ke-4 Praktikum Sistem Basis Data")
Kamis = ("kelas ke-1 IMK", "kelas ke-3 LogMat", "kelas ke-4 Praktekkom")


if A == "senin" :
    for i in range(len(Senin)):
        print(Senin [i])
elif A == "selasa" :
    for i in range(len(Selasa)):
        print(Selasa [i])
elif A == "rabu" :
    for i in range(len(Rabu)):
        print(Rabu [i])
elif A == "kamis" :
    for i in range(len(Kanis)):
        print(Kamis [i])
elif A == "jumat" :
    print("Hari Jumat Anda tidak ada kelas")

