# Nama : Naufal Arkan El Rochim
# NIM : 2505060068
# Rombel : 04

import datetime
import random
import string

perpustakaan = {
    "judul" : "judul",
    "penulis" : "00000000",
    "status" :  "True / False",
    "terbit" : datetime.datetime(1111, 1, 11),
    "pinjam" : datetime.datetime(1111, 1, 11)
}
x = "y"
data_perpustakaan = {}

while x == "y":
    print(f"{"SISTEM MANAGEMENT PERPUSTAKAAN":^20}")
    print("-" * 20)

    perpustakaan = dict.fromkeys(perpustakaan.keys(), "___")
    print(perpustakaan)

    perpustakaan["judul"] = input("judul buku: ")
    perpustakaan["penulis"] = input("Penulis buku: ")
    
    TAHUN_TERBIT = int(input("Tahun terbit (YYYY): "))
    BULAN_TERBIT = int(input("Bulan terbit (1-12): "))
    TANGGAL_TERBIT = int(input("Tanggal terbit (1-31): "))
    perpustakaan["terbit"] = datetime.datetime(TAHUN_TERBIT, BULAN_TERBIT, TANGGAL_TERBIT).strftime("%x")

    TAHUN_PINJAM = int(input("Tahun pinjam (YYYY): "))
    BULAN_PINJAM = int(input("Bulan pinjam (1-12): "))
    TANGGAL_PINJAM = int(input("Tanggal pinjam (1-31): "))
    perpustakaan["pinjam"] = datetime.datetime(TAHUN_PINJAM, BULAN_PINJAM, TANGGAL_PINJAM).strftime("%x")
    
    perpustakaan["status"] = input("Status buku (ya / tidak): ")

    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_perpustakaan.update({KEY : perpustakaan})

    print(f"{"KEYS":<10} {"JUDUL":<25} {"PENULIS":<15} {"TERBIT":<10} {"PINJAM":<10} {"STATUS":<10}")
    print("-" * 65)

    for data_perpus in data_perpustakaan:

        JUDUL = data_perpustakaan[data_perpus]["judul"]
        PENULIS = data_perpustakaan[data_perpus]["penulis"]
        TERBIT = data_perpustakaan[data_perpus]["terbit"]
        PINJAM = data_perpustakaan[data_perpus]["pinjam"]
        STATUS = data_perpustakaan[data_perpus]["status"]

        print(f"{data_perpus:<10} {JUDUL:<25} {PENULIS:<15} {TERBIT:<10} {PINJAM:<10} {STATUS:<10}")

    x = input("Apakah ingin melanjutkan? (y/n): ").lower()

print("Program selesai berjalan, sampai jumpa")