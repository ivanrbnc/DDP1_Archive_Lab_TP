#mengimpor modul string untuk membantu menghilangkan punctuation (!+. dst)
import string

#mengimpor modul dari file html_functions.py
from html_functions import make_HTML_word, make_HTML_box, print_HTML_file

#menampilkan judul
print('''Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.\n''')

#meminta nama file input yang diinginkan
nama_file_input = str(input('Silakan masukan nama file: '))

#menampilkan sub judul
print('\n' + nama_file_input + ' :\n56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan\n(jumlah:kata)\n')

#membuat list kosong
list_input = []
list_input_final = []
list_stop = []

#membaca stopwords.txt
stop_words = open('stopwords.txt', 'r')
stop_content = stop_words.readlines()

#membaca file dari nama file yang diinginkan
file_input = open(nama_file_input, 'r')
input_content = file_input.readlines()

#membuat list kata yang berisi stopword yang tidak dibolehkan
for stop_lines in stop_content:
    stop_word_lower = stop_lines.lower()
    stop_word = stop_word_lower.split()
    list_stop += stop_word

#membuat list kata dari konten input yang diinginkan 
for input_lines in input_content:
    input_word_lower = input_lines.lower()
    input_word = input_word_lower.split()
    list_input += input_word

#mengeliminasi kata-kata yang terdapat di list_stop dan menghilangkan punctuation
for char in list_input:
    strip_input = char.strip(string.punctuation)
    if strip_input not in list_stop:
        input_word_final = strip_input.split()
        list_input_final += input_word_final

#menunjukkan frekuensi per kata, bisa juga menggunakan Counter.
counts = {}
for word in list_input_final:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

#mengurutkan kata-kata tadi berdasarkan value lalu key (key : value)
#pemakaian lambda berarti membuat def kosong sementara
#x[1], x[0] berarti mengurutkan x[1] (value) lalu x[0] (key)
sorted_counts = sorted(counts.items(), key = lambda x: (x[1],x[0]), reverse = True)

#menampilkan 56 tertinggi dari frekuensi tadi
top = sorted_counts[:56]

#memberikan kolom maksimal
max_column = 0

#menampilkan kata dan frekuensi munculnya kata tersebut dengan maksimum empat kolom
for word, value in top:
    print(f'{value:2}:{word:14}', end = ' ')
    max_column += 1
    if max_column % 4 == 0:
        print('\n')

#mengurutkan variabel top berdasarkan abjad
sorted_top = sorted(top)

#membuat total span yang kosong
span_total = ''

#membaca satu per satu value dari kata dan menjadikannya string html lalu memasukkan ke span_total
#[0][1] list nest pertama, lalu dibaca valuenya, [-1][1] list nest terakhir, lalu dibaca valuenya
for word,value in sorted_top:
    span_temp = make_HTML_word(word, value, top[0][1], top[-1][1])
    span_total += ' ' + span_temp

#membuat box berdasarkan span_total
box = make_HTML_box(span_total)

#membuat html file baru berdasarkan box
print_HTML_file(box, nama_file_input)

#meminta enter dari user untuk keluar dari program
input('Tekan Enter untuk keluar …')
exit()

#acknowledgement
#line 61 : https://stackoverflow.com/questions/7742752/sorting-a-dictionary-by-value-then-by-key