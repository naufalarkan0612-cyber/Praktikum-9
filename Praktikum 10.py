# Nama : Naufal Arkan El Rochim
# NPM : 2505060068
# Rombel : 4

# 1.

# a.
mahasiswa = ("Arkan", "2505060068", "Teknologi Informasi")

# c.
print(mahasiswa[1])
print(mahasiswa[2])

# 2.

# a.
keranjang = {
    "apel" :  5000,
    "pisang" : 3000,
    "jeruk" : 7000,
    "anggur" : 15000
}

# c.
for buah, harga in keranjang.items():
    print(f"harga : {buah} -> Rp {harga}")

# b. d.
jumlah = 0
for i in keranjang.values():
    jumlah += i
print(jumlah)