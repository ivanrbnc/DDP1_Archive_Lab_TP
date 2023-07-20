#menampilkan judul dan hanya sekali
print('Selamat datang! Silakan masukkan jadwal KA:')

#membuat data yang dibutuhkan
schedule = []
input_schedule = ''
destination_list = []
price_list = []
class_dict = {'1' : 'Eksekutif', '2' : 'Bisnis', '3' : 'Ekonomi'}
possible_ans = ['INFO_TUJUAN', 'TUJUAN_KELAS', 'TUJUAN_KELAS_TERMURAH', 'TUJUAN_JAM', 'TUJUAN_JAM_TERMURAH', 'EXIT']

#memastikan jawaban dari input_schedule tidak berkata selesai dan/atau string kosong
while input_schedule != 'selesai':
    input_schedule = input()
    if input_schedule != 'selesai' and input_schedule != '':
        schedule.append(input_schedule.split())

#menampilkan daftar perintah
print('''
Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>
4. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
5. TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>
6. EXIT''')

#membuat looping untuk membuat program terus berjalan
while True:
    command = input('\nMasukkan perintah: ')
    splitted_command = command.split()

    #ketika tidak ada satu pun kata dari splitted_command yang beririsan dengan possible_ans, 
    #program akan meminta kembali command
    while set(splitted_command) & set(possible_ans) == False:
        command = input('Perintah yang dimasukkan tidak valid.\nMasukkan perintah: ')

    #ketika command bernilai EXIT, program akan berhenti
    if command == 'EXIT':
        print('Terima kasih sudah menggunakan program ini!')
        exit()

    #ketika command bernilai INFO_TUJUAN, maka program akan menjalankan if ini
    elif command == 'INFO_TUJUAN':
        print('KA di stasiun ini memiliki tujuan akhir:')
        #iterasi isi dari schedule dan mengumpulkan destination ke destination_list
        for train_num, destination, depart, price in schedule:
            destination_list.append(destination)
        #mengubah list tadi menjadi set agar tidak ada duplikat
        destination_only = set(destination_list)

        #melakukan iterasi set dan mencetak isinya
        for destination_specific in destination_only:
            print(destination_specific)

    #ketika command terdiri dari 3 kata dan kata pertama adalah TUJUAN_KELAS, 
    #maka program akan menjalankan if ini
    elif len(splitted_command) == 3 and splitted_command[0] == 'TUJUAN_KELAS':
        counter = 0
        #melakukan iterasi pada schedule
        for train_num, destination, depart, price in schedule:
            #mengubah isi dari variabel train_num menjadi kata yang ada di dictionary
            if int(train_num)//100 == 1:
                train_class = class_dict['1']
            elif int(train_num)//100 == 2:
                train_class = class_dict['2']
            elif int(train_num)//100 == 3:
                train_class = class_dict['3']

            #ketika pada iterasi bersesuaian dengan kriteria dari kereta yang diinginkan,
            #maka program akan menampilkan daftar kereta yang memenuhi kriteria
            if splitted_command[1] == destination and splitted_command[2] == train_class:
                print(f'KA {train_num} berangkat pukul {depart} dengan harga tiket {price}')
                counter += 1

        #ketika counter tidak disentuh, maka ditentukan bahwa tidak ada jadwal yang sesuai
        if counter == 0:
            print('Tidak ada jadwal KA yang sesuai.')

    elif len(splitted_command) == 3 and splitted_command[0] == 'TUJUAN_KELAS_TERMURAH':
        counter = 0
        #melakukan iterasi pada schedule
        for train_num, destination, depart, price in schedule:
            #mengubah isi dari variabel train_num menjadi kata yang ada di dictionary
            if int(train_num)//100 == 1:
                train_class = class_dict['1']
            elif int(train_num)//100 == 2:
                train_class = class_dict['2']
            elif int(train_num)//100 == 3:
                train_class = class_dict['3']

            #ketika pada iterasi bersesuaian dengan kriteria dari kereta yang diinginkan,
            #maka program akan menyimpan harga
            if splitted_command[1] == destination and splitted_command[2] == train_class:
                price_list.append(price)
        
        #mencari harga termurah
        if price_list != []:
            cheapest_price = min(price_list)

        #melakukan iterasi pada schedule
        for train_num, destination, depart, price in schedule:
            #mengubah isi dari variabel train_num menjadi kata yang ada di dictionary
            if int(train_num)//100 == 1:
                train_class = class_dict['1']
            elif int(train_num)//100 == 2:
                train_class = class_dict['2']
            elif int(train_num)//100 == 3:
                train_class = class_dict['3']

            #ketika pada iterasi bersesuaian dengan kriteria dari kereta yang diinginkan,
            #maka program akan menampilkan daftar kereta yang memenuhi kriteria
            if splitted_command[1] == destination and splitted_command[2] == train_class and price == cheapest_price:
                print(f'KA {train_num} berangkat pukul {depart} dengan harga tiket {price}')
                counter += 1

        #ketika counter tidak disentuh, maka ditentukan bahwa tidak ada jadwal yang sesuai
        if counter == 0:
            print('Tidak ada jadwal KA yang sesuai.')
        
        #mereset isi dari price_list
        price_list.clear()

    elif len(splitted_command) == 3 and splitted_command[0] == 'TUJUAN_JAM':
        counter = 0
        #melakukan iterasi pada schedule
        for train_num, destination, depart, price in schedule:
            #ketika pada iterasi bersesuaian dengan kriteria dan jam dari kereta yang diinginkan,
            #maka program akan menampilkan daftar kereta yang memenuhi kriteria
            if splitted_command[1] == destination and int(splitted_command[2]) >= int(depart):
                print(f'KA {train_num} berangkat pukul {depart} dengan harga tiket {price}')
                counter += 1

        #ketika counter tidak disentuh, maka ditentukan bahwa tidak ada jadwal yang sesuai
        if counter == 0:
            print('Tidak ada jadwal KA yang sesuai.')

    elif len(splitted_command) == 3 and splitted_command[0] == 'TUJUAN_JAM_TERMURAH':
        counter = 0
        #melakukan iterasi pada schedule
        for train_num, destination, depart, price in schedule:
            #ketika pada iterasi bersesuaian dengan kriteria dan jam dari kereta yang diinginkan,
            #maka program akan menyimpan harga
            if splitted_command[1] == destination and int(splitted_command[2]) >= int(depart):
                price_list.append(price)

        #mencari harga termurah
        if price_list != []:
            cheapest_price = min(price_list)

        #melakukan iterasi pada schedule
        for train_num, destination, depart, price in schedule:
            #ketika pada iterasi bersesuaian dengan kriteria dari kereta yang diinginkan,
            #maka program akan menampilkan daftar kereta yang memenuhi kriteria
            if splitted_command[1] == destination and int(splitted_command[2]) >= int(depart) and price == cheapest_price:
                print(f'KA {train_num} berangkat pukul {depart} dengan harga tiket {price}')
                counter += 1

        #ketika counter tidak disentuh, maka ditentukan bahwa tidak ada jadwal yang sesuai
        if counter == 0:
            print('Tidak ada jadwal KA yang sesuai.')
        
        #mereset isi dari price_list
        price_list.clear()

    #memastikan kembali isi dari command
    else:
        print('Perintah yang dimasukkan tidak valid.')