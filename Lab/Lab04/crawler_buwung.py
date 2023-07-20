#mengimpor modul os (operating system)
import os

#meminta nama file dari user
file_input = input('Masukkan nama file input : ')
file_output = input('Masukkan nama file output: ')

#memastikan apakah file tersebut ada atau tidak lalu memberikan output sesuai kriteria
if os.path.isfile(file_input) == True:
    file_input_size = os.path.getsize(file_input)
    #ketika size dari file = 0, file akan dianggap kosong
    if file_input_size == 0:
        print('File input ada tapi kosong :(')
        input('Program selesai. Tekan enter untuk keluar...')
        exit()
elif os.path.isfile(file_input) == False:
    print('File input tidak ada :(')
    input('Program selesai. Tekan enter untuk keluar...')
    exit()

#membaca file input apabila sudah melewati permisalan di atas
x = open(file_input, 'r')
#membuat file baru untuk output serta memberikannya izin untuk menulis
y = open(file_output, 'w')

#membuat list kosong
new_file = []

#membaca satu per satu baris lalu mengubah masing-masing kondisi ke huruf yang ditentukan
while True:
    line = x.readline()
    splitted_line = line.split()
    for i in splitted_line:
        if '@' in i:
            new_file.append('(M)')
        elif '#' in i:
            new_file.append('(H)')
        elif 'www.' in i:
            new_file.append('(U)')
        else:
            new_file.append(i)
    if splitted_line == []:
        break
    new_file.append('\n')
    
#menyatukan list menjadi string
final_new_file = ' '.join(new_file)

#menghitung banyaknya huruf yang ditentukan tadi
mention_total = final_new_file.count('(M)')
hashtag_total = final_new_file.count('(H)')
link_total = final_new_file.count('(U)')

#menuliskan output ke file output
print(final_new_file, file = y)
print(' ', file = y)
print('#'*15, file = y)
print('Mention : {0:>5}'.format(mention_total), file = y)
print('Hashtag : {0:>5}'.format(hashtag_total), file = y)
print('Url     : {0:>5}'.format(link_total), file = y)

#memberikan output ke terminal
print('Output berhasil ditulis pada {}'.format(file_output))
input('Program selesai. Tekan enter untuk keluar...')
exit()