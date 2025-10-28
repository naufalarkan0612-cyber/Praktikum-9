# Nama : Naufal Arkan El Rochim
# NPM : 2505060068
# Rombel : 4


# 1. Diberikan list berikut:

buah = ['apel', 'mangga', 'jeruk', 'anggur', 'pisang']

# a. Tambahkan 'semangka' di akhir list
buah.append('semangka')
print("Setelah menambahkan 'semangka':", buah)

# b. Sisipkan 'durian' di antara 'jeruk' dan 'anggur'
buah.insert(3, 'durian')
print("Setelah menyisipkan 'durian':", buah)

# c. Hapus 'mangga' dari list
buah.pop(1)
print("Setelah menghapus 'mangga':", buah)

# d. Ubah 'pisang' menjadi 'nanas'
buah[4] = 'nanas'
print("Setelah mengubah 'pisang' menjadi 'nanas':", buah)

# e. Tampilkan 3 buah pertama
print("Tiga buah pertama:", buah[:3])

# 2. Diberikan list berikut:

angka = [45, 12, 78, 23, 56, 89, 34]

# a. Urutkan list secara ascending
angka.sort()
print("List angka setelah diurutkan secara ascending:", angka)
# b. Urutkan list secara descending
angka.reverse()
print("List angka setelah diurutkan secara descending:", angka)