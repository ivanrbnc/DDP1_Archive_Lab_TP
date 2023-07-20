
#mengikuti contoh yang berisi matkul tersedia
MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

MATKUL_TERSEDIA = [
["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
["ddp 1 b", HARI[0] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
["manbis", HARI[4] + JAM[13] + 1, HARI[4] + JAM[15] + 40],
["matdis 1 a", HARI[4] + JAM[9] + 0, HARI[4] + JAM[13] + 0],
["matdis 1 b", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
["kalkulus 1 c", HARI[2] + JAM[10] + 0, HARI[2] + JAM[12] + 00]
]

#mengkategorikan list dari matkul yang telah diambil, nama-nama matkul saja, serta list kosong
#untuk membantu men-sort pada jadwal
matkul_added = []
matkul_added_name = []
sorted_matkul = []

#pembuatan looping agar program terus dijalankan
while True:
    print('''
=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul 
5  Selesai 
====================================
''')
    #meminta jawaban dan diwajibkan sesuai dengan pilihan yang tersedia
    option = input('Masukkan pilihan: ').strip() #memastikan input tidak memiliki extra space
    possible_option = ['1', '2', '3', '4', '5']
    while option not in possible_option:
        print('Maaf, pilihan tidak tersedia')
        option = input('Masukkan pilihan: ').strip()

    if option == '1':
        matkul_add = input('Masukkan nama matkul: ').lower().strip() #memastikan penambahan matkul case insensitive dan mengabaikan extra space
        for matkul, start, end in MATKUL_TERSEDIA: #mengiterasi variabel MATKUL_TERSEDIA
            if matkul_add == matkul: #matkul spesifik sesuai dengan salah satu elemen MATKUL_TERSEDIA
                matkul_added.append([matkul, start, end]) #memasukkan keseluruhan data matkul
                matkul_added_name.extend([matkul]) #memasukkan nama matkul saja
        if matkul_add not in matkul_added_name: #memastikan nama matkul dengan kumpulan nama matkul
            print('Matkul tidak ditemukan')
      
    elif option == '2':
        matkul_remove = input('Masukkan nama matkul: ').lower().strip() #mamstikan pengurangan matkul case insensitive dan mengabaikan extra space
        if matkul_remove not in matkul_added_name: #membandingkan input user dengan kumpulan nama matkul
            print('Matkul tidak ditemukan')
        for matkul, start, end in matkul_added: #mengiterasi sesuai matkul_added
            if matkul_remove == matkul: #akan menghilangkan matkul spesifik dari list
                matkul_added.remove([matkul, start, end]) 
                matkul_added_name.remove(matkul_remove)
        
    elif option == '3':
        counter = 0 
        for i in range(len(matkul_added)-1): #membaca isi matkul_added, -1 karena membaca per 2 data 
            range_a_1 = matkul_added[i][1] #batas bawah data pertama
            range_a_2 = matkul_added[i][2] #batas atas data pertama
            j = i + 1 
            for j in range(len(matkul_added)):
                if j > i: #agar tidak melakukan pengulangan dengan data
                    range_b_1 = matkul_added[j][1] #batas bawah data kedua
                    range_b_2 = matkul_added[j][2] #batas atas data kedua
                    #mengkalkulasi apakah ada irisan
                    #minus 1 pada range_b_1 agar tetap menghitung ketika jadwal pertama selesai dan mulai kedua sama
                    if range_b_1 - 1 in range(range_a_1, range_a_2) or range_b_2 in range(range_a_1, range_a_2):
                        print(f'{matkul_added[i][0]} bentrok dengan {matkul_added[j][0]}')
                        counter += 1
        if counter == 0: #ketika tidak terjadi irisan, counter akan tetap 0
            print('Tidak ada matkul yang bermasalah')
                    
    elif option == '4':
        if matkul_added == []: #memastikan isi matkul_added
            print('Tidak ada matkul yang diambil')
        else:
            print('daftar matkul: ')            
            for matkul, start, end in matkul_added: #mengiterasi isi dari matkul_added sesuai data yang dibutuhkan
                matkul = matkul.upper() 
                days_selected = start // MENIT_DALAM_HARI #mendapatkan hari ke- (mulai dari 0)
                start_hours = start % MENIT_DALAM_HARI // MENIT_DALAM_JAM #mendapatkan jam ke-
                start_minutes = start % MENIT_DALAM_JAM #mendapatkan menit ke-
                end_hours = end % MENIT_DALAM_HARI // MENIT_DALAM_JAM #mendapatkan jam ke-
                end_minutes = end % MENIT_DALAM_JAM #mendapatkan menit ke-
                
                #memasukkan data tadi ke list untuk keperluan print
                sorted_matkul.append([matkul, days_selected, start_hours, start_minutes, end_hours, end_minutes])
        
        #melakukan sort lewat list menggunakan lambda
        sorted_matkul.sort(key = lambda x: (x[1],x[2], x[0]))   #x[1] terlebih dahulu yang berarti memprioritaskan hari dibandingkan jam. Terakhir adalah nama matkul
        
        #mengiterasi dari list yang sudah di-sort lalu mengubah days_selected sehingga sesuai dengan kriteria print
        for matkul, days_selected, start_hours, start_minutes, end_hours, end_minutes in sorted_matkul:  
            if days_selected == 0:
                days_name = 'Senin,'
            elif days_selected == 1:
                days_name = 'Selasa,'
            elif days_selected == 2:
                days_name = 'Rabu,'
            elif days_selected == 3:
                days_name = 'Kamis,'
            elif days_selected == 4:
                days_name = 'Jum\'at,'
            elif days_selected == 5:
                days_name = 'Sabtu,'
            elif days_selected == 6:
                days_name = 'Minggu,'
            #memprint sesuai pemformatan
            print(f'{matkul:14s} {days_name:8s} {start_hours:02d}.{start_minutes:02d} s/d {days_name:8s} {end_hours:02d}.{end_minutes:02d}')

        #menghilangkan list sorted_matkul karena tadi menggunakan append
        sorted_matkul.clear() #clear juga dilakukan agar list sorted_matkul selalu berwadah kosong

    elif option == '5':
        print('Terima kasih!')
        exit() #menutup program