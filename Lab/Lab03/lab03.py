#meminta user untuk mengisi isi dari himpunan
#menambahkan koma sebagai parameter pengambilan string
himpunan_a = input('Masukkan input himpunan A: ') + ','
himpunan_b = input('Masukkan input himpunan B: ') + ','

#membuat string kosong untuk menampung serpihan string dari himpunan
str_from_a = ''
str_from_b = ''

#membuat string kosong untuk menampung kumpulan serpihan string
new_str = ''

#membaca karakter satu per satu
for char_a in range(len(himpunan_a)):
    #ketika karakter bukan koma, akan dimasukkan ke serpihan A, sedangkan jika koma akan berubah menjadi
    #serpihan B
    if himpunan_a[char_a] != ',':
        str_from_a += himpunan_a[char_a]
    else:
        #sama seperti looping di atas
        for char_b in range(len(himpunan_b)):
            if himpunan_b[char_b] != ',':
                str_from_b += himpunan_b[char_b]
            else:
                #ketika sudah bertemu koma di bagian B, kedua serpihan string dimasukkan ke new_str
                new_str += f'({str_from_a},{str_from_b}), '
                #mereset ulang serpihan B tersebut
                str_from_b = ''
        #mereset ulang serpihan A tersebut
        str_from_a = ''

#karena akhiran akan memiliki koma dan spasi, maka perlu dipotong memakai string slicing
#memberikan output yang diinginkan
print('A x B = {' + (new_str[:-2]) + '}')

#ACKNOWLEDGEMENT
#Saya bertanya kepada Dafi Nafidz Radhiyya (2106702564) terkait flow dari program 
#karena saya merasa kebingungan