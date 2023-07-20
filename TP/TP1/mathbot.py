#mengimpor module random
import random

#menampilkan judul
print('Halo, selamat datang di Mathbot') 

#CHECKPOINT PERTAMA
while True: 
    #menampilkan pilihan-pilihan mode
    print('Pilih Mode: ')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Campur')
    print('4. Akhiri program\n')

    #meminta input user untuk pemilihan mode
    mode = input('Masukkan perintah: ') 
    #memastikan input user hanya di sekitar 1, 2, 3, dan 4
    while mode not in ['1', '2', '3', '4']: 
        mode = input('''Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari
perintah yang tersedia.\nMasukkan perintah: ''')

    #menamai masing-masing mode
    if mode == '1':
        nama_mode = 'penjumlahan'
    elif mode == '2':
        nama_mode = 'pengurangan'
    elif mode == '3':
        nama_mode = 'campur'
    elif mode == '4':
        print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
        exit() #menghentikan paksa program

    #menampilkan ulang nama mode
    print(f'\nBaik, pilih mode {nama_mode} ya, sekarang pilih jenis kuis apa?') 

    #CHECKPOINT KEDUA
    while True:
        #menampilkan pilihan-pilihan kuis 
        print('Pilih kuis:')
        print('1. Kuis Lepas')
        print('2. Kuis 5')
        print('3. Ganti mode')
        print('4. Akhiri Program\n')

        #meminta input user untuk pemilihan jenis dari kuis
        jenis = input('Masukkan jenis kuis: ') 
        #memastikan input user hanya di sekitar 1, 2, 3, dan 4
        while jenis not in ['1', '2', '3', '4']: 
            jenis = input('''Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari
perintah yang tersedia.\nMasukkan jenis kuis: ''')

        #ketika user ingin mengganti mode, program akan mundur ke checkpoint pertama
        if jenis == '3':
            break
        #ketika user memilih akhiri program, program akan otomatis berhenti
        elif jenis == '4': 
            print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
            exit() #menghentikan paksa program

        #memberikan maksimal ronde untuk kuis 5 serta mereset ulang poin
        ronde = 1
        poin = 0
        max_ronde = 6
        
        #CHECKPOINT KETIGA
        while True:
            #memberikan value untuk kedua angka secara acak
            num_1 = random.randrange(0, 11) 
            num_2 = random.randrange(0, 11)
            #awal mula operasi untuk membantu mode campur
            rand_op = '+-'
            #memilih acak dari salah satu operasi rand_op
            chosen_op = random.choice(rand_op)

            #menetapkan operasi yang dipilih ketika pilihan mode ialah 1 atau 2
            if mode == '1': 
                chosen_op = '+'
            elif mode == '2':
                chosen_op = '-'
            
            #menentukan peletakan angka pada soal agar tidak bisa minus pada operasi pengurangan
            if num_1 > num_2:
                soal = f'Berapa {num_1} {chosen_op} {num_2}'           
            elif num_2 > num_1:
                soal = f'Berapa {num_2} {chosen_op} {num_1}'
            elif num_2 == num_1:
                soal = f'Berapa {num_1} {chosen_op} {num_2}'
            
            #format penamaan soal
            if jenis == '1':
                print(soal, ' ?')
            elif jenis == '2':
                print(f'Pertanyaan {ronde}: ', soal, ' ?')
            
            #membuat kunci jawaban dari soal
            correct_answer = eval(soal[7:])

            #meminta input user terkait jawaban dari soal
            answer = input('Jawab: ')

            #menentukan reaksi program berdasarkan input user
            if answer == 'akhiri kuis' and jenis == '1': 
                print(' ')              
                break #kembali checkpoint kedua
            elif answer == 'akhiri kuis' and jenis == '2':
                print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat.\n')
            elif answer.isalpha() or answer == '': #mempastikan bahwa jawaban user termasuk bilangan bulat
                print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat.\n')
            elif int(answer) == correct_answer:
                print('Hore benar!\n')
                poin += 20
            else:
                print(f'Masih kurang tepat, ya. Jawabannya adalah {correct_answer} \n')

            #menambah ronde agar looping bisa menjadi False
            ronde += 1

            #memberikan output poin untuk jenis 'kuis 5' serta akan berhenti ketika menyentuk ronde maksimal
            if jenis == '2':
                if ronde == max_ronde:
                    print(f'Score kamu: {poin} \n')
                    break #kembali ke checkpoint kedua