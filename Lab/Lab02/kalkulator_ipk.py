#menampilkan judul dari program
print('Selamat datang di kalkulator IPK!')

#meminta input user untuk jumlah mata kuliah yang diinginkan
jumlah_matkul = int(input('Masukkan jumlah mata kuliah: '))

#mempastikan jumlah matkul yang diinput tidak negatif
while jumlah_matkul < 0:
    jumlah_matkul = int(input('Harap menggunakan angka positif.\nMasukkan jumlah mata kuliah: '))

#ketika tidak mengikuti matkul, program akan berhenti
if jumlah_matkul == 0:
    print('Tidak ada mata kuliah yang diambil.')
    exit()  #memaksa menghentikan program

#nilai mula-mula
total_ipk_pembilang = 0
total_ipt_pembilang = 0
total_ipk_penyebut = 0
total_ipt_penyebut = 0

#menentukan ronde awal untuk looping
round = 1

while round <= jumlah_matkul:
    #mengubah integer menjadi string
    round_str = str(round)

    #meminta input user untuk deskripsi matkul
    nama_matkul = str(input('\nMasukkan nama mata kuliah ke-' + round_str + ': '))
    sks = int(input('Masukkan jumlah SKS ' + nama_matkul + ': '))

    #mempastikan sks yang diinput tidak negatif dan tidak 0
    while sks <= 0:
        sks = int(input('SKS yang kamu masukkan tidak valid.\nMasukkan jumlah mata kuliah: '))

    nilai = float(input('Masukkan nilai yang kamu dapatkan: '))

    #mempastikan nilai yang diinput tidak negatif
    while nilai < 0:
        nilai = float(input('Nilai yang kamu masukkan tidak valid.\nMasukkan jumlah mata kuliah: '))
    
    #penentuan sks yang lulus serta bobot masing-masing nilai sesuai tabel yang diberikan
    if nilai > 55:
        sks_lulus = sks
        if nilai >= 85:
            bobot = 4.0
        elif 80 <= nilai < 85:
            bobot = 3.7
        elif 75 <= nilai < 80:
            bobot = 3.3
        elif 70 <= nilai < 75:
            bobot = 3
        elif 65 <= nilai < 70:
            bobot = 2.7
        elif 60 <= nilai < 65:
            bobot = 2.3
        elif 55 <= nilai < 60:
            bobot = 2.0
    else:
        sks_lulus = 0
        if 40 <= nilai < 55:
            bobot = 1.0
        elif 0 <= nilai < 50:
            bobot = 0.0
    
    #mengkalkulasi berdasarkan rumus per ronde
    ipk_pembilang = sks_lulus * bobot
    total_ipk_pembilang += ipk_pembilang
    total_ipk_penyebut += sks_lulus

    ipt_pembilang = sks * bobot
    total_ipt_pembilang += ipt_pembilang
    total_ipt_penyebut += sks

    round += 1

#mengubah agar maksimal angka mutu di belakang koma ialah dua
mutu_lulus = '{:.2f}'.format(total_ipk_pembilang)
mutu_total = '{:.2f}'.format(total_ipt_pembilang)

#mengkalkulasi nilai akhir ipk dan ipt
if total_ipk_penyebut == 0: #agar nilai ipk dapat terdefinisi
    nilai_ipk = 0.0
else:
    nilai_ipk = total_ipk_pembilang / total_ipk_penyebut

nilai_ipt = total_ipt_pembilang / total_ipt_penyebut

#mengubah agar maksimal angka ipk dan ipt di belakang koma ialah dua
ipk_simple = '{:.2f}'.format(nilai_ipk)
ipt_simple = '{:.2f}'.format(nilai_ipt)

#output akhir yang diberikan
print(' ')
print('Jumlah SKS lulus : ' + str(total_ipk_penyebut) + ' / ' + str(total_ipt_penyebut))
print('Jumlah mutu lulus : ' + str(mutu_lulus) + ' / ' + str(mutu_total))
print('Total IPK kamu adalah ' + str(ipk_simple))
print('Total IPT kamu adalah ' + str(ipt_simple))