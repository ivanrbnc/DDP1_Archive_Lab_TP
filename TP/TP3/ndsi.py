# -*- coding: utf-8 -*-
import string
import matplotlib.pyplot as plt

# lengkapi fungsi berikut
def load_stop_words(filename):
    """
    Parameters
    ----------
    filename : string
        nama file yang menyimpan daftar stopwords.
        Di soal, nama default-nya adalah stopwords.txt

    Returns
    -------
    stop_words : set
        himpunan stopwords (unik)

    Fungsi menerima nama file yang berisi daftar stopwords,
    kemudian memuat semua stopwords ke dalam struktur data
    set. Perhatikan bahwa semua stopwords yang ada di dalam
    file sudah dalam bentuk huruf kecil semua.
    """
    #membuat data dasar
    list_stop = []
    
    #membaca file name serta menangkap per baris
    stop_words = open(filename, 'r')
    stop_content = stop_words.readlines()
    stop_words.close()

    #membaca per baris, lalu memasukkannya ke list berisi stop words
    for stop_lines in stop_content:
        stop_word = stop_lines.lower().split()
        list_stop += stop_word

    #membuatnya menjadi set
    stop_words = set(list_stop)

    return stop_words

# lengkapi fungsi berikut
def count_words(filepath, stop_words):
    """
    Parameters
    ----------
    filepath : string
        path atau lokasi dari file yang berisi sekumpulan
        kalimat-kalimat yang memiliki polaritas sentiment,
        yaitu rt-polarity.neg atau rt-polarity.pos

    stop_words : set
        himpunan stopwords

    Returns
    -------
    word_freq : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut.

    Fungsi ini akan scan semua baris (semua kalimat) yang
    ada di file dan kemudian mengakumulasikan frekuensi dari
    setiap kata yang muncul pada file tersebut.

    Contoh
    ------
    Jika isi dari file adalah:

        I just watched a good movie
        wow! a good movie
        a good one

    Fungsi akan mengembalikan dictionary:
        {'i':1, 'just':1, 'watched':1, 'a':3, 'good':3,
         'movie':2, 'wow!':1, 'one':1}

    Notes
    -----
    1. stopwords diabaikan
    2. karakter tanda baca seperti , . / dan sebagainya juga
       diabaikan (gunakan string.punctuation di library string)
    """
    #membuat data dasar
    word_freq = {}
    list_input = []
    list_input_final = []

    #membaca file name serta menangkap per baris
    file_input = open(filepath, 'r', encoding = 'utf-8')
    input_content = file_input.readlines()
    file_input.close()

    #membaca per baris, lalu memasukkannya ke list berisi stop words
    for input_lines in input_content:
        input_word = input_lines.lower().split()
        list_input += input_word

    #mengeliminasi punctuation serta kata yang berada di stop words lalu masukkan ke list_input_final
    for char in list_input:
        strip_input = char.strip(string.punctuation)
        if strip_input not in stop_words:
            input_word_final = strip_input.split()
            list_input_final += input_word_final

    #membuat dictionary berdasarkan list_input_final
    for word in list_input_final:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

    return word_freq

# lengkapi fungsi berikut
def compute_ndsi(word_freq_pos, word_freq_neg):
    """
    Parameters
    ----------
    word_freq_pos : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut. Frekuensi dari kata dihitung dari
        file rt-polarity.pos
    word_freq_neg : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut. Frekuensi dari kata dihitung dari
        file rt-polarity.neg

    Returns
    -------
    word_ndsi : dictionary
        sebuah dictionary, dimana key merupakan kata (string)
        dan value adalah NDSI score (float)

    Notes
    -----
    NDSI dari sebuah kata dihitung dengan:

              word_freq_pos[word] - word_freq_neg[word]
              -----------------------------------------
              word_freq_pos[word] + word_freq_neg[word]

    Jika kata tidak ditemukan pada salah satu dictionary,
    frekuensi kata tersebut adalah 0.

    Contoh
    ------
    Jika word_freq_neg = {'bad':10, 'worst':5, 'good':1} dan
         word_freq_pos = {'good':20, 'nice':5, 'bad':2},

    maka word_ndsi = {'bad':-0.67, 'worst':-1, 'good':0.90, 'nice':1}

    """
    #kata : value
    word_ndsi = {}
    
    #membaca dictionary
    for word in word_freq_pos:
        #membandingkan dua dictionary lalu membuat dictionary baru berdasarkan rumus
        if word in word_freq_neg:
            numerator = word_freq_pos[word] - word_freq_neg[word]
            denominator = word_freq_pos[word] + word_freq_neg[word]
            word_ndsi[word] = numerator / denominator
        else:
            numerator = word_freq_pos[word]
            denominator = word_freq_pos[word]
            word_ndsi[word] = numerator / denominator
    
    #membaca dictionary
    for word in word_freq_neg:
        #membandingkan dua dictionary lalu membuat dictionary baru berdasarkan rumus
        if word not in word_freq_pos:
            numerator = word_freq_neg[word]
            denominator = word_freq_neg[word]
            word_ndsi[word] = -(numerator / denominator)

    return word_ndsi

# Fungsi berikut sudah selesai. Anda tidak perlu implementasikan
def show_ndsi_histogram(word_ndsi):
    """
    Parameters
    ----------
    word_ndsi : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah NDSI score (float) dari kata tersebut.

    Returns
    -------
    None.

    Plot histogram dari semua NDSI scores yang dihasilkan

    """
    ndsi_scores = [score for _, score in word_ndsi.items()]
    plt.hist(ndsi_scores, 100, facecolor = 'g', alpha = 0.75)
    plt.yscale("log")
    plt.xlabel('NDSI score')
    plt.ylabel('Frekuensi')
    plt.savefig("ndsi-hist.pdf")

if __name__ == "__main__":

    # memuat stop words ke sebuah set
    stop_words = load_stop_words("stopwords.txt")

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment positif
    word_freq_pos = count_words("./sent-polarity-data/rt-polarity.pos", stop_words)

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment negatif
    word_freq_neg = count_words("./sent-polarity-data/rt-polarity.neg", stop_words)

    # hitung NDSI untuk semua kata-kata pada kedua jenis dictionary berisi
    # word frequency
    word_freq_ndsi = compute_ndsi(word_freq_pos, word_freq_neg)

    # tampilkan histogram dari nilai-nilai NDSI yang dihasilkan
    show_ndsi_histogram(word_freq_ndsi)

    # LENGKAPI BAGIAN INI
    # urutkan pasangan kata dan skor ndsi yang ada
    # di word_freq_ndsi berdasarkan nilai ndsi saja, dari terkecil
    # ke yang terbesar

    #membuat dictionary kosong
    sorted_ndsi = {}
    
    #membuat list dari dictionary word_freq_ndsi key berdasarkan value
    sorted_list = sorted(word_freq_ndsi, key = word_freq_ndsi.get)

    #mengubah list tadi menjadi dictionary
    for word in sorted_list:
        sorted_ndsi[word] = word_freq_ndsi[word]

    # LENGKAPI BAGIAN INI
    # simpan daftar kata-kata dan nilai ndsi yang sudah diurutkan tadi ke
    # file ndsi.txt
    ndsi_filename = "ndsi.txt"

    #memberi akses menulis file
    file_ndsi = open(ndsi_filename, 'w')

    #membaca sorted_ndsi lalu dituliskan sesuai format
    for key, value in sorted_ndsi.items(): 
        file_ndsi.write(f'{key} {value}\n')

    #menutup file dan program
    file_ndsi.close()
    exit()
