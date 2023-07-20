#untuk memberi restriksi pada data login
import string

#membuat class User sebagai Parent class
class User() :
    def __init__(self, user_name, tipe):
        #memiliki dua variabel utama, nama dan tipe
        self._user_name = user_name
        self.tipe = tipe

    #membuat metode getter masing-masing atribut
    def get_name(self) : 
        return self._user_name

    def get_tipe(self) :
        return self.tipe

#membuat class Seller sebagai anak dari class User
class Seller(User) : 
    def __init__(self, user_name):
        #menginherit nama dan tipe dari parent
        super().__init__(user_name, tipe = 'SELLER')
        #memberikan atribut tambahan
        self.list_barang_jual = list_product
        self.pemasukan = 0

    #membuat metode getter dan setter untuk atribut pemasukan
    def get_pemasukan(self) : 
        return self.pemasukan

    def set_pemasukan(self, val) : 
        self.pemasukan += val

    #metode menambah produk yang nantinya akan menambah ke list_barang_jual dan list_product
    def tambah_product(self):
        #meminta data produk
        add_product = input('Masukkan data produk : ')
        #memotong-motongnya menjadi bagian-bagian
        splitted_add_prod = add_product.split()
        #mendefinisikan setiap bagian
        name_prod = splitted_add_prod[0]
        price_prod = splitted_add_prod[1]
        stock_prod = splitted_add_prod[2]
        #memastikan nama dari produk belum pernah terdaftar
        if get_product(name_prod) == None:
            #pembuatan objek Product yang nantinya dimasukkan ke list_product
            list_product.append([name_prod, Product(name_prod, price_prod, stock_prod, self._user_name)])
        else:
            print('Produk sudah pernah terdaftar.')

    #metode untuk melihat barang yang ingin dijual
    def lihat_produk_jualan_saya(self) : 
        #mencetak awal tabel
        print('\nBerikut merupakan barang jualan saya')
        print('-------------------------------------')
        print('  Nama Produk  |   Harga   | Stock ')
        print('-------------------------------------')

        #mensort list_barang_jual
        self.list_barang_jual.sort(key=lambda x: x[0])

        #pembacaan elemen dari atribut list_barang_jual dan menampilkannya
        for name_product, product in self.list_barang_jual : 
            print(f'{name_product:<15}|{product.price:<11}|{product.stock:<7}')
        print('-------------------------------------')

    #menampilkan menu untuk tipe Seller
    def menu(self) :
        login = True
        while login:
            #meminta input terus menerus hingga logout
            print('\nPemasukkan anda ' + str(self.get_pemasukan()) + ',')
            seller_input = input('Apa yang ingin Anda lakukan? ')
            if seller_input == '1':
                self.tambah_product()
            elif seller_input == '2':
                self.lihat_produk_jualan_saya()
            elif seller_input == '3':
                print(f'Anda telah keluar dari akun {self.get_name()}')
                login = False

#membuat class Buyer sebagai anak dari class User
class Buyer(User) : 
    def __init__(self, user_name, saldo):
        #menginherit nama dan tipe dari parent
        super().__init__(user_name, tipe = 'BUYER')
        #memberikan atribut tambahan
        self.list_barang_beli = list()
        self.saldo = int(saldo)

    #membuat metode getter untuk atribut saldo
    def get_saldo(self):
        return self.saldo

    #fungsi melihat macam-macam produk yang sudah diperjualbelikan
    def lihat_product(self):
        #mencetak awal tabel
        print('Berikut merupakan daftar produk di Dekdepedia')
        print('------------------------------------------------')
        print('  Nama Produk  |   Harga   | Stock |  Penjual ')
        print('------------------------------------------------')
        
        #mensort list_product
        list_product.sort(key=lambda x: x[0])

        #membaca isi list_product dan membaca atributnya satu per satu
        for name_product, product in list_product:
            print(f'{name_product:<15}|{product.price:<11}|{product.stock:<7}|{product.seller:<9} ')
        print('------------------------------------------------')

    #fungsi pembelian produk
    def beli_product(self):
        #meminta input barang yang ingin dibeli
        buyer_buyying = input('Masukkan barang yang ingin dibeli : ')
        #pemanfaatan counter
        counter_prod = 0
        #membaca isi list_product
        for name_product, product in list_product:
            #memastikan produk yang ingin dipilih ada
            if buyer_buyying == product.name:
                counter_prod += 1
                #memastikan saldo pengguna
                if self.get_saldo() < product.price:
                    print(f'Maaf, saldo Anda tidak cukup untuk membeli {buyer_buyying}.')
                #memastikan stok produk
                elif product.stock <= 0:
                    print('Maaf, stok produk telah habis.')
                #syarat sempurna
                elif product.stock > 0 and self.get_saldo() >= product.price:
                    print(f'Berhasil membeli {buyer_buyying} dari {product.seller}')
                    #mengurangi stok sebesar 1
                    product.stock -= 1
                    #mengurangi saldo pengguna
                    self.saldo -= product.price
                    #menambahkan ke list_barang_beli (pencatatan nota)
                    self.list_barang_beli.append([name_product, product.price, product.seller])
                    #memberikan saldo ke penjual
                    confirm_sold = get_user(product.seller, list_user)
                    confirm_sold.set_pemasukan(product.price)
        
        #jika tidak tersentuh loopnya, maka barang tidak ditemukan
        if counter_prod == 0:
            print(f'Barang dengan nama {buyer_buyying} tidak ditemukan dalam Dekdepedia.')

    #fungsi untuk melihat list_barang_beli atau nota pembelian
    def riwayat_beli(self):
        #mencetak awal tabel
        print('Berikut merupakan barang yang saya beli')
        print('-------------------------------------')
        print('  Nama Produk  |   Harga   | Penjual ')
        print('-------------------------------------')

        #mensort list_barang_beli
        self.list_barang_beli.sort(key=lambda x: x[0])

        #membaca list_barang_beli lalu menampilkannya
        for product, price, name_seller in self.list_barang_beli:
            print(f'{product:<15}|{price:<11}|{name_seller:<9}')
        print('-------------------------------------')

    #menampilkan menu untuk tipe Buyer
    def menu(self):
        login = True
        while login:
            #meminta input terus menerus hingga logout
            print('\nSaldo anda ' + str(self.get_saldo()) + ',')
            buyer_input = input('Apa yang ingin Anda lakukan? ')
            if buyer_input == '1':
                self.lihat_product()
            elif buyer_input == '2':
                self.beli_product()
            elif buyer_input == '3':
                self.riwayat_beli()
            elif buyer_input == '4':
                print(f'Anda telah keluar dari akun {self.get_name()}')
                login = False

#membuat class product
class Product() : 
    def __init__(self, name, price, stock, seller):
        #memberikan atribut yang dimiliki product
        self.name = name
        self.price = int(price)
        self.stock = int(stock)
        self.seller = seller

    #membuat metode get_name
    def get_name(self):
        return self.name

# method get_user dan get_product tidak perlu diubah, 
# silakan manfaatkan method ini untuk mendapatkan user dan produk yang dibutuhkan
def get_user(name, list_user):
    '''
    Method untuk mengembalikan user dengan user_name sesuai parameter
    '''
    for user in list_user:
        if user.get_name() == name:
            return user
    return None

def get_product(name):
    '''
    Method untuk mengembalikan product dengan name sesuai parameter
    '''
    for temp, product in list_product:
        if product.get_name() == name:
            return product
    return None

#pembuatan data dasar
list_user = []
list_product = []
list_username_input = []

#fungsi utama yang akan dijalankan
def main():
    while True:
        #penampilan perintah yang tersedia dan meminta input user
        print('\nSelamat datang di Dekdepedia!')
        print('Silakan memilih salah satu menu di bawah:')
        print('1. Sign Up')
        print('2. Log In')
        print('3. Exit')
        pilih = input('Pilihan Anda: ')

        if (pilih == '1') : 
            #meminta input jumlah looping yang digunakan
            banyak_user = int(input('Jumlah akun yang ingin didaftarkan : '))
            print('Data akun: ')
            #meloop data sebanyak banyak_user yang diberikan
            for i in range (banyak_user) : 
                data_user = input(str(i+1)+'. ')
                #membuat pecahan dari data_user
                splitted_data_user = data_user.split()
                if len(splitted_data_user) < 2 or len(splitted_data_user) > 3:
                    print('Akun tidak valid')
                else:
                    #mengelompokkan pecahan dari splitted_data user
                    initiate = splitted_data_user[0]                   
                    user_name_sign_up = splitted_data_user[1]
                    #huruf-huruf yang tidak direstriksi
                    not_restricted = string.ascii_letters + '1234567890_-'
                    #pemanfaatan counter
                    counter_let = 0
                    #membaca per huruf untuk memastikan counter
                    for letter in user_name_sign_up:
                        if letter not in not_restricted:
                            counter_let += 1
                            break
                    #mengkategorikan sesuai soal (BUYER dan SELLER) dan memasukannya ke list_user
                    if user_name_sign_up not in list_username_input and counter_let == 0 :
                        if initiate == 'BUYER' and len(splitted_data_user) == 3 and splitted_data_user[2].isnumeric() and int(splitted_data_user[2]) > 0:
                            list_username_input.append(user_name_sign_up)
                            list_user.append(Buyer(user_name_sign_up, splitted_data_user[2]))               
                        elif initiate == 'SELLER' and len(splitted_data_user) == 2:
                            list_username_input.append(user_name_sign_up)
                            list_user.append(Seller(user_name_sign_up))                    
                        #ketika tidak masuk kriteria, data akan dianggap tidak valid
                        else:
                            print('Akun tidak valid.')
                    elif initiate == 'BUYER' and len(splitted_data_user) != 3:
                        print('Akun tidak valid.')
                    elif user_name_sign_up in list_username_input:
                        print('Username sudah terdaftar.')
                    else:
                        print('Akun tidak valid.')

        elif (pilih == '2') :
            #meminta input jumlah looping yang digunakan
            user_name_login = input('user_name : ')
            #memastikan user_logged_in nyata
            user_logged_in = get_user(user_name_login, list_user)
            if user_logged_in != None:
                #memastikan tipe dari user
                job = user_logged_in.get_tipe()
                #menampilkan nama user dan tipe user
                print(f'Anda telah masuk dalam akun {user_name_login} sebagai {job}\n')
                #mengelompokkan perintah sesuai tipe
                if job == 'BUYER':
                    print(f'Selamat datang {user_name_login},')
                    print('berikut menu yang bisa Anda lakukan:')
                    print('1. LIHAT_SEMUA_PRODUK')
                    print('2. BELI_PRODUK')
                    print('3. RIWAYAT_PEMBELIAN_SAYA')
                    print('4. LOG_OUT')
                    #menampilkan menu buyer
                    user_logged_in.menu()
                elif job == 'SELLER':
                    print(f'Selamat datang {user_name_login},')
                    print('berikut menu yang bisa Anda lakukan:')
                    print('1. TAMBAHKAN_PRODUK')
                    print('2. LIHAT_DAFTAR_PRODUK_SAYA')
                    print('3. LOG_OUT')        
                    #menampilkan menu seller
                    user_logged_in.menu()
            #ketika user_logged_in tidak nyata
            else:
                print(f'Akun dengan username {user_name_login} tidak ditemukan')
                
        elif (pilih == '3') : 
            #menghentikan program
            print('Terima kasih telah menggunakan Dekdepedia!')
            exit()

if __name__ == '__main__':
    main()