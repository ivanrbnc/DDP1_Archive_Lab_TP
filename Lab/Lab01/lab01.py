import math

#bertanya kepada user terkait nilai jari-jari lingkaran (r)
r = float(input('Masukkan radius lingkaran: ')) 

s = 2 * r #panjang sisi persegi yang didapat dari panjang jari-jari lingkaran

#rumus bangun datar berdasarkan gambar
segitiga = s * r / 2
lingkaran = math.pi * r ** 2
persegi = s ** 2

#penerapan rumus berdasarkan warna
luas_merah = persegi - lingkaran
luas_kuning = lingkaran - segitiga
luas_ungu = segitiga

#pemotongan angka di belakang koma yang terlalu banyak
luas_merah_edit = '{:.2f}'.format(luas_merah)
luas_kuning_edit = '{:.2f}'.format(luas_kuning)
luas_ungu_edit = '{:.2f}'.format(luas_ungu)

#menampilkan output dari luas-luas warna
print('Luas daerah cat merah: ', luas_merah_edit)
print('Luas daerah cat kuning: ', luas_kuning_edit)
print('Luas daerah cat ungu: ', luas_ungu_edit)