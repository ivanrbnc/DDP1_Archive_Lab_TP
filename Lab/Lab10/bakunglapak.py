import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter.messagebox import askretrycancel, showinfo, showwarning

#class produk untuk menyatukan banyak atribut di satu objek
class Product(object):
    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def set_stok(self, jumlah):
        self.__stok -= jumlah

#class buyer untuk menyatukan banyak atribut di satu objek
class Buyer(object):
    def __init__(self):
        self.__daftar_beli = {}

    def add_daftar_beli(self, produk, jumlah):
        if produk in self.__daftar_beli:
          self.__daftar_beli[produk] += jumlah
        else :
          self.__daftar_beli[produk] = jumlah

    def get_daftar_beli(self):
      return self.__daftar_beli

# GUI Starts from here

# Toplevel adalah sebuah class yang mirip dengan Frame namun akan terbuka
# secara terpisah dengan Window utama (jadi membuat top-level window yang
# terpisah)
class WindowLihatBarang(tk.Toplevel):
    def __init__(self, product_dict, master = None):
        #atribut bawaan
        super().__init__(master)
        self.product_dict = product_dict
        self.wm_title("Daftar Barang")
        self.create_widgets()

    #pembuatan widget yang dibutuhkan
    def create_widgets(self):
        #pembuatan label tiap elemen yang diperlukan
        self.lbl_judul = tk.Label(self, text = 'Daftar Barang Yang Tersedia').grid(row = 0, column = 1)
        self.lbl_nama = tk.Label(self, text = 'Nama Produk').grid(row = 1, column = 0)
        self.lbl_harga = tk.Label(self, text = 'Harga').grid(row = 1, column = 1)
        self.lbl_stok = tk.Label(self, text = 'Stok Produk').grid(row = 1, column = 2)

        #pengisian tabel sesuai 'grid'
        i = 2
        for nama, barang in sorted(self.product_dict.items()):
            tk.Label(self, text = f"{nama}").grid(row = i, column= 0)
            tk.Label(self, text = f"{barang.get_harga()}").grid(row = i, column= 1)
            tk.Label(self, text = f"{barang.get_stok()}").grid(row = i, column= 2)
            i += 1

        #pembuatan button exit
        self.btn_exit = tk.Button(self, text = "EXIT", command = self.destroy).grid(row = i, column=1)

#class terbuka untuk beli barang
class WindowBeliBarang(tk.Toplevel):
    def __init__(self, buyer, product_dict, master = None):
        #atribut bawaan
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict
        self.wm_title("Beli Barang")
        self.geometry("280x120")
        self.create_widgets()

    #pembuatan widget yang diperlukan
    def create_widgets(self):
        #memberikan label judul
        self.judul_form = tk.Label(self, text = 'Form beli barang').grid(row = 1, column = 4)

        #pembuatan stringvar untuk menyimpan nama dan jumlah
        self.string_nama_barang = tk.StringVar()
        self.string_jumlah_barang = tk.StringVar()

        #meminta input user
        self.title_name = tk.Label(self, text = "Nama Barang").grid(row = 2, column = 3)
        self.ent_nama_barang = tk.Entry(self, textvariable = self.string_nama_barang)
        self.ent_nama_barang.grid(row = 2, column = 4)
        self.title_quan = tk.Label(self, text = "Jumlah").grid(row = 3, column = 3)
        self.ent_jumlah = tk.Entry(self, textvariable = self.string_jumlah_barang)
        self.ent_jumlah.grid(row = 3, column = 4)
        
        #pembuatan button untuk beli dan exit
        self.button_purchase_beli = tk.Button(self, text = "Beli", command = self.beli_barang).grid(row = 4, column = 4)
        self.button_exit_beli = tk.Button(self, text = "EXIT", command = self.destroy).grid(row = 5, column = 4)
    
    #ketika button yang dipencet adalah beli
    def beli_barang(self):
        #menangkap value dari stringvar
        nama_barang = self.string_nama_barang.get()
        jumlah = int(self.string_jumlah_barang.get())

        #memberikan restriksi sesuai yang dibutuhkan
        if nama_barang == "":
            #menunjukkan retry cancel ketika nama barang yang diberikan kosong
            response = askretrycancel(title = 'BarangNotFound', message= "Nama barang tidak boleh kosong") 
            if response : #ketika memilih retry
                pass #nothing happened
            else: #ketika memilih cancel
                self.destroy()
        
        elif nama_barang not in self.product_dict:
            #menunjukkan retry cancel ketika barang tidak ditemukan
            response_2 = askretrycancel(title = 'BarangNotFound', message= f"Barang dengan nama {nama_barang} tidak ditemukan dalam \nBakungLapak.") 
            if response_2 : #ketika memilih retry
                pass #nothing happened
            else: #ketika memilih cancel
                self.destroy()

        elif self.product_dict[nama_barang].get_stok() - jumlah < 0 or jumlah < 0:
            #menunjukkan warning bahwa stok habis
            showwarning(title = 'StokEmpty', message = 'Maaf, stok produk telah habis.')

        else :
            #pembuatan dictionary lalu mengeksekusi pembelian
            barang = self.product_dict[nama_barang]
            buyer.add_daftar_beli(barang, jumlah)
            barang.set_stok(jumlah)
            #penghilangan Entry dari widget beli ketika berhasil membeli
            self.ent_nama_barang.delete(0, tk.END)
            self.ent_jumlah.delete(0, tk.END)
            #menunjukkan info bahwa pembeli berhasil membeli barang
            tkmsg.showinfo("Berhasil!", f"Berhasil membeli {nama_barang} sejumlah {jumlah}")

#class terbuka untuk checkout
class WindowCheckOut(tk.Toplevel):
    def __init__(self, buyer, master = None):
        #atribut bawaan
        super().__init__(master)
        self.wm_title("Daftar Barang")
        self.daftar_dibeli = buyer.get_daftar_beli()
        self.create_widgets()

    #pembuatan widget yang diperlukan
    def create_widgets(self):
        #pembuatan label dengan grid sebagai 'keterangan tabel'
        self.label_0_checkout = tk.Label(self, text = 'Keranjangku').grid(row = 1, column = 2)
        self.label_1_checkout = tk.Label(self, text = 'Nama Produk').grid(row = 2, column = 1)
        self.label_2_checkout = tk.Label(self, text = 'Harga Barang').grid(row = 2, column = 2)
        self.label_3_checkout = tk.Label(self, text = 'Jumlah').grid(row = 2, column = 3)

        #menunjukkan barang apa saja yang telah dibeli sekaligus keterangannya
        counter = 3
        #melakukan sort terhadap self.daftar_beli sehingga yang ditampilkan sesuai yang diinginkan
        for barang in sorted(self.daftar_dibeli.keys(), key=lambda product: product.get_nama()):
            quantity = self.daftar_dibeli[barang]
            self.label_dibeli_barang_nama = tk.Label(self, text = barang.get_nama()).grid(row = counter, column = 1)
            self.label_dibeli_barang_harga = tk.Label(self, text = barang.get_harga()).grid(row = counter, column = 2)
            self.label_quantity = tk.Label(self, text = quantity).grid(row = counter, column = 3)
            counter += 1

        #ketika daftar_dibeli kosong, akan menunjukkan label seperti di bawah
        if self.daftar_dibeli == {}: #zonk
            self.checkout_none = tk.Label(self, text = 'Belum ada barang yang dibeli :(').grid(row = 3, column = 2)
        
        self.button_exit_checkout = tk.Button(self, text = "EXIT", command = self.destroy).grid(row = counter + 1, column = 2)

#class untuk jendela utama
class MainWindow(tk.Frame):
    def __init__(self, buyer, product_dict, master = None):
        #atribut bawaan
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict
        self.pack()
        self.create_widgets()

    #pembuatan widget yang diperlukan
    def create_widgets(self):
        #penampilan label judul
        self.label = tk.Label(self, text = 'Selamat datang di BakungLapak. Silahkan pilih Menu yang tersedia')

        #pembuatan tombol-tombol
        self.btn_lihat_daftar_barang = tk.Button(self, text = "LIHAT DAFTAR BARANG", command = self.popup_lihat_barang)
        self.btn_beli_barang = tk.Button(self, text = "BELI BARANG", command = self.popup_beli_barang)
        self.btn_check_out = tk.Button(self, text = "CHECK OUT", command = self.popup_check_out)
        self.btn_exit = tk.Button(self, text = "EXIT", command = self.quit)

        #pengemasan masing-masing label dan button
        self.label.pack()
        self.btn_lihat_daftar_barang.pack()
        self.btn_beli_barang.pack()
        self.btn_check_out.pack()
        self.btn_exit.pack()

    # semua barang yand dijual
    def popup_lihat_barang(self):
        WindowLihatBarang(self.product_dict)

    # menu beli barang
    def popup_beli_barang(self):
        WindowBeliBarang(self.buyer, self.product_dict)

    # menu riwayat barang yang dibeli
    def popup_check_out(self):
        WindowCheckOut(self.buyer)

#fungsi utama
if __name__ == "__main__":
    #pembuatan buyer
    buyer = Buyer()

    #produk yang ingin dijual
    product_dict = {"Kebahagiaan" : Product("Kebahagiaan", 999999, 1),
                    "Kunci TP3 SDA" : Product("Kunci TP3 SDA", 1000000, 660)}

    m = MainWindow(buyer, product_dict)
    m.master.title("BakungLapak")
    m.master.mainloop()