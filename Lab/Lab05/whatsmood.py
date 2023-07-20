#mengimpor modul operating system
import os

#menentukan perhitungan melalui fungsi
def hap_point(count):
    global happy, sad, anger
    happy += 9 * count
    sad -= 6 * count

def sad_point(count):
    global happy, sad, anger
    sad += 10 * count
    anger -= 8 * count

def ang_point(count):
    global happy, sad, anger
    anger += 13 * count
    happy -= 5 * count

#meminta nama file ke user
file_input = input('Masukkan nama file input: ')

#memastikan apakah file tersebut ada atau tidak lalu memberikan output sesuai kriteria
if os.path.isfile(file_input) == True:
    file_input_size = os.path.getsize(file_input)
    #ketika size dari file = 0, file akan dianggap kosong
    if file_input_size == 0:
        print('File input ada tapi kosong :(')
        exit()
elif os.path.isfile(file_input) == False:
    print('File input tidak ada :(')
    exit()

#memberikan izin untuk membaca file dan membedakannya ke dua variabel yang berbeda
file = open(file_input, 'r')
rep_file = open(file_input, 'r')

#membaca seluruh teks, lalu mengganti beberapa string ke emoji
rep = rep_file.read()
rep_1 = rep.replace('(smile)', '\U0001f603')
rep_2 = rep_1.replace('(sad)', '\U0001f622')
rep_3 = rep_2.replace('(angry)', '\U0001f621')

#membuat list kosong untuk keperluan pengelompokkan
list_depe = []
list_pak = []

#membaca seluruh teks per kalimat, lalu mengelompokkannya berdasarkan dek depe dan pak chanek
for line in file_input:
    line = file.readline()
    if 'Dek Depe: ' in line:
        list_depe += line
    elif 'Pak Chanek: ' in line:
        list_pak += line

#menyatukan masing-masing list dari kedua kelompok, walau yang dipakai hanya list pak chanek
x = ''.join(list_depe)
y = ''.join(list_pak)

#menghitung banyaknya perasaan dari chat pak chanek 
smile_count = y.count('(smile)')
sad_count = y.count('(sad)')
angry_count = y.count('(angry)')

#menentukan nilai perasaan dasar
happy = sad = anger = 50

#menghitung menggunakan fungsi yang tersedia
hap_point(smile_count)
sad_point(sad_count)
ang_point(angry_count)

#memberikan range maksimum dan minimum untuk setiap perasaan
if happy > 100:
    happy = 100
elif happy < 0:
    happy = 0

if sad > 100:
    sad = 100
elif sad < 0:
    sad = 0

if anger > 100:
    anger = 100
elif anger < 0:
    anger = 0

#memberikan output
#menuliskan ulang chat dengan emoji yang sudah berubah
print('\n' + rep_3)

#memberikan kalkulasi dari ketiga perasaan
print('\nMengukur suasana hati....\n')
print('##### Hasil Pengukuran #####')
print(f'Happiness = {happy} | Sadness = {sad} | Anger = {anger}')

#mengevaluasi serta menampilkan kesimpulan
print('\n##### Kesimpulan #####')
if happy > sad and happy > anger:
    print('Pak Chanek sedang bahagia.')
elif sad > happy and sad > anger:
    print('Pak Chanek sedang sedih.')
elif anger > happy and anger > sad:
    print('Pak Chanek sedang marah.')
elif happy == sad and happy > anger:
    print('Pak Chanek sedang bahagia atau sedih.')
elif happy == anger and happy > sad:
    print('Pak Chanek sedang bahagia atau marah.')
elif sad == anger and sad > happy:
    print('Pak Chanek sedang sedih atau marah.')
elif happy == sad == anger:
    print('Kesimpulan tidak ditemukan.')

#menutup program
exit()