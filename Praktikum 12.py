# Nama : Naufal Arkan El Rochim
# NIM : 2505060068
# Rombel : 04

def persegi_panjang(panjang = 0, lebar = 0):
  hasil = panjang * lebar
  print(f"luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {hasil}")
  return hasil

def balok(panjang = 0, lebar = 0, tinggi = 0):
  hasil = panjang * lebar
  print(f"volume balok dengan panjang {panjang} dan lebar {lebar} serta tinggi {tinggi} adalah {hasil}")
  return hasil

def bundar(rusuk):
  lingkaran = 3.14 * (rusuk ** 2)
  bola = (4 / 3) * 3.14 * (rusuk ** 3)

  print(f"luas lingkaran dengan rusuk {rusuk} adalah {lingkaran}")
  print(f"volume bola dengan rusuk {rusuk} adalah {bola}")
  return lingkaran, bola

persegi_panjang(5, 5)
balok(10, 20, 70)
lingkaran, bola = bundar(7)