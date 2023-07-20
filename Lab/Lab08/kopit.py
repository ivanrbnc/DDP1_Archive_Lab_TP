#membuat fungsi rekursi dimana dia akan membuat dict baru berisi kumpulan dari koneksi dirinya
def check(key, fixed):
    #membuat dict baru
    if fixed not in dict_new:
        dict_new[fixed] = []
    #ketika value dari key tersebut kosong, maka akan dikembalikan key-nya
    if dict_sickness[key] == []:
        return key
    #menambahkan ke dict baru yang berisi kumpulan dari koneksi penyebaran
    for element in dict_sickness[key]:
        dict_new[fixed] += [check(element, fixed)]

#meminta macam-macam rantai penyebaran
print('Masukkan rantai penyebaran:')

#membuat data-data dasar
input_sick = ''
list_sick_total = []
dict_sickness = {}
dict_new = {}

#memastikan jawaban yang dibolehkan
possible_ans = ['RANTAI_PENYEBARAN', 'CEK_PENULARAN', 'EXIT']

#mengecek input sampai mengeluarkan kata 'selesai'
while input_sick != 'selesai':
    input_sick = input()
    if input_sick != 'selesai' and input_sick != '':
        list_sick_total.append(input_sick.split())

#membaca per baris
for item in list_sick_total:
    #membuat dictionary baru
    if item[0] not in dict_sickness:
        #ketika di baris tersebut hanya satu kata, maka valuenya adalah list kosong
        if len(item) == 1:
            dict_sickness[item[0]] = []
        #kata pertama = key, kata sisanya = value
        else:
            dict_sickness[item[0]] = item[1:]
    #menambahkan kata baru ketika key sudah diketahui
    else:
        dict_sickness[item[0]] += item[1:]

#menampilkan perintah yang bisa dilakukan
print('''
List perintah:
1. RANTAI_PENYEBARAN
2. CEK_PENULARAN
3. EXIT''')

#loop terus menerus
while True:
    #meminta user input
    command = input('\nMasukkan perintah: ')
    #memotong per kata dari command
    splitted_command = command.split()

    #ketika command adalah exit, maka program berhenti
    if command == 'EXIT':
        print('Goodbye~ Semoga virus KOPIT cepat berakhir.')
        exit()

    #ketika kata pertama dari command adalah rantai_penyebaran, maka masuk ke conditional ini
    elif splitted_command[0] == 'RANTAI_PENYEBARAN':
        #penyebar penyakit adalah kata kedua dari command
        spreader_wanted = splitted_command[1]
        #ketika penyebar tidak termasuk dalam dict_sickness, maka akan masuk conditional ini
        if spreader_wanted not in dict_sickness:
            print(f'Maaf, nama {spreader_wanted} tidak ada dalam rantai penyebaran.')
        #ketika isi dari penyebar hanyalah kosong, maka akan memprint dirinya sendiri
        elif dict_sickness[spreader_wanted] == []:
            print('-', spreader_wanted)
        #ketika isi dari penyebar berisi, maka akan masuk conditional ini
        else:
            print(f'Rantai penyebaran {spreader_wanted}')
            #memasukkan ke fungsi rekursi check() sehingga membentuk dict_new yang berisi koneksi-koneksi dari penyebar
            check(spreader_wanted, spreader_wanted)
            #menambahkan data dari dict_sickness ke dalam dict_new
            dict_new[spreader_wanted] += dict_sickness[spreader_wanted]
            #mengubah menjadi set sehingga tidak ada duplikat
            set_final = set(dict_new[spreader_wanted])

            #memprint isi dari set tanpa menampilkan None
            for element in set_final:
                if element != None:
                    print('-', element)
            #menambahkan dirinya sendiri
            print('-', spreader_wanted)
        
        #mereset isi dari dict_new
        dict_new.clear()

    #ketika kata pertama dari command adalah cek_penularan, maka masuk ke conditional ini
    elif splitted_command[0] == 'CEK_PENULARAN':
        #mengelompokkan kata
        infected_wanted = splitted_command[1]
        spreader_wanted = splitted_command[2]

        #ketika isi dari infected dan spreader sama akan masuk ke sini
        if infected_wanted == spreader_wanted:
            print('YA')
        #ketika spreader ada di dict_sickness maka akan masuk ke sini
        elif spreader_wanted in dict_sickness:
            #mengambil value dari key di dict_sickness
            infected_by_spreader = dict_sickness[spreader_wanted]

            #memasukkan ke fungsi rekursi check() sehingga membentuk dict_new yang berisi koneksi-koneksi dari penyebar
            check(spreader_wanted, spreader_wanted)
            #menambahkan data dari dict_sickness ke dalam dict_new
            dict_new[spreader_wanted] += dict_sickness[spreader_wanted]
            #mengubah menjadi set sehingga tidak ada duplikat
            set_final = set(dict_new[spreader_wanted])

            #mengecek apakah yang terinfeksi ada di set_final
            if infected_wanted in set_final:
                print('YA')
            elif infected_wanted not in set_final:
                print('TIDAK')
        
        #ketika spreader tidak ada di sickness maka akan masuk ke sini
        elif spreader_wanted not in dict_sickness:
            #ketika infected tidak ada juga maka akan masuk ke sini
            if infected_wanted not in dict_sickness:
                print(f'Maaf, nama {infected_wanted} dan {spreader_wanted} tidak ada dalam rantai penyebaran.')
            #tetapi ketika infected ada maka akan masuk ke sini
            elif infected_wanted in dict_sickness:
                print(f'Maaf, nama {spreader_wanted} tidak ada dalam rantai penyebaran.')

        #mereset isi dari dict_new
        dict_new.clear()
    
    #memastikan command hanyalah termasuk tiga command tadi
    else:
        print('Maaf perintah tidak dikenali. Masukkan perintah yang valid.')