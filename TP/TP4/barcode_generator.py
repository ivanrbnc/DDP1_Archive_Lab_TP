#mengimport hal-hal yang penting
from tkinter import *
from tkinter.messagebox import showerror

#membuat class utama
class GUI:
    def __init__(self, master):
        #menentukan atribut yang diperlukan
        self.master = master
        master.title('EAN 13') #judul
        master.geometry('450x550') #luas layar
        #pembuatan stringvar untuk penangkapan value dari Entry
        self.string_barcode = StringVar()
        self.string_code = StringVar()

        #pembuatan label dan entry sesuai format
        self.file = Label(master, text = 'Save barcode to PS file [eg: EAN13.eps]').pack()
        self.field_barcode = Entry(master, textvariable = self.string_barcode, width = 40).pack()
        self.code = Label(master, text = 'Enter code (first 12 decimal digits)').pack()
        self.field_code = Entry(master, textvariable = self.string_code, width = 40).pack(pady = 10) #pady = spasi tambahan

        #menunggu user menekan "Enter" untuk melanjutkan program
        master.bind('<Return>', self.check)

        #pembuatan canvas dengan luas tertentu
        self.canvas = Canvas(master, width = 375, height = 425 , bg = 'white') 
        self.canvas.pack() #dipisah sehingga bisa dimanipulasi

    def check(self, trash): #trash = variabel yang tidak diperlukan dari hasil master.bind
        #pengecekan validasi string_barcode per kata
        invalid = 0
        for char in self.string_barcode.get():
            if char in '\/:*?"<>|':
                invalid += 1

        #pengecekan validasi sesuai ketentuan tambahan yang berlaku
        if len(self.string_code.get()) == 12 and self.string_code.get().isnumeric() and (self.string_barcode.get()[-4:] == '.eps' or self.string_barcode.get()[-3:] == '.ps') and invalid == 0:
            self.show()
        else:
            self.wrong_input()
            
    #menampilkan error ketika input yang diberikan salah
    def wrong_input(self):
        showerror(title = 'Wrong input!', message = 'Please enter correct input code.')

    #pembuatan struktur barcode berdasarkan angka pertama
    def structure(self):
        first = self.string_code.get()[0]
        group_2 = 'RRRRRR'
        if first == '0':
            group_1 = 'LLLLLL'
            return group_1, group_2
        elif first == '1':
            group_1 = 'LLGLGG'
            return group_1, group_2
        elif first == '2':
            group_1 = 'LLGGLG'
            return group_1, group_2
        elif first == '3':
            group_1 = 'LLGGGL'
            return group_1, group_2
        elif first == '4':
            group_1 = 'LGLLGG'
            return group_1, group_2
        elif first == '5':
            group_1 = 'LGGLLG'
            return group_1, group_2
        elif first == '6':
            group_1 = 'LGGGLL'
            return group_1, group_2
        elif first == '7':
            group_1 = 'LGLGLG'
            return group_1, group_2
        elif first == '8':
            group_1 = 'LGLGGL'
            return group_1, group_2
        elif first == '9':
            group_1 = 'LGGLGL'
            return group_1, group_2

    #penerjemahan angka dan struktur yang dimiliki menjadi struktur baru dengan 0 dan 1
    def translate(self, num, type):
        if num == '0' and type == 'L':
            code = '0001101'
            return code
        elif num == '0' and type == 'G':
            code = '0100111'
            return code
        elif num == '0' and type == 'R':
            code = '1110010'
            return code
        elif num == '1' and type == 'L':
            code = '0011001'
            return code
        elif num == '1' and type == 'G':
            code = '0011001'
            return code
        elif num == '1' and type == 'R':
            code = '1100110'
            return code
        elif num == '2' and type == 'L':
            code = '0010011'
            return code
        elif num == '2' and type == 'G':
            code = '0011011'
            return code
        elif num == '2' and type == 'R':
            code = '1101100'
            return code
        elif num == '3' and type == 'L':
            code = '0111101'
            return code
        elif num == '3' and type == 'G':
            code = '0100001'
            return code
        elif num == '3' and type == 'R':
            code = '1000010'
            return code
        elif num == '4' and type == 'L':
            code = '0100011'
            return code
        elif num == '4' and type == 'G':
            code = '0011101'
            return code
        elif num == '4' and type == 'R':
            code = '1011100'
            return code
        elif num == '5' and type == 'L':
            code = '0110001'
            return code
        elif num == '5' and type == 'G':
            code = '0111001'
            return code
        elif num == '5' and type == 'R':
            code = '1001110'
            return code
        elif num == '6' and type == 'L':
            code = '0101111'
            return code
        elif num == '6' and type == 'G':
            code = '0000101'
            return code
        elif num == '6' and type == 'R':
            code = '1010000'
            return code
        elif num == '7' and type == 'L':
            code = '0111011'
            return code
        elif num == '7' and type == 'G':
            code = '0010001'
            return code
        elif num == '7' and type == 'R':
            code = '1000100'
            return code
        elif num == '8' and type == 'L':
            code = '0110111'
            return code
        elif num == '8' and type == 'G':
            code = '0001001'
            return code
        elif num == '8' and type == 'R':
            code = '1001000'
            return code
        elif num == '9' and type == 'L':
            code = '0001011'
            return code
        elif num == '9' and type == 'G':
            code = '0010111'
            return code
        elif num == '9' and type == 'R':
            code = '1110100'
            return code

    #pembuatan sum untuk angka terakhir dari barcode
    def check_sum(self): 
        temp_sum_1 = 0 #temp_sum untuk angka genap
        temp_sum_2 = 0 #temp_sum untuk angka ganjil
        #counter untuk mendeskripsikan angka yang dikerjakan saat ini termasuk genap/ganjil
        counter = 1
        string_code = self.string_code.get() #menangkap keseluruhan angka
        for num in string_code:
            #mengelompokkan temp_sum berdasarkan sifat genap/ganjil-nya
            if counter % 2 == 0: #genap
                temp_sum_1 += int(num)
            elif counter % 2 == 1: #ganjil
                temp_sum_2 += int(num)
            counter += 1

        #pengerjaan sesuai rumus
        almost_sum = temp_sum_1 * 3 + temp_sum_2
        nearly_sum = almost_sum % 10
        if nearly_sum != 0:
            sum = 10 - nearly_sum
        else:
            sum = nearly_sum
        return sum

    def show(self):
        #pembuatan data dasar yang diperlukan
        list_code = []
        counter_2 = 1
        EAN = self.string_code.get()

        #memastikan canvas selalu bersih
        self.canvas.delete('all')

        #pembacaan sesuai struktur
        for group in self.structure():
            #pembacaan sesuai per huruf
            for coded in group:
                #penerjemahan dengan menyambungkan huruf dan angka sesuai struktur
                x = EAN[counter_2]
                code_translated = self.translate(x, coded)
                #memasukkannya satu per satu ke list
                list_code.append(code_translated)
                #pemutusan loop
                if counter_2 == 11:
                    break
                counter_2 += 1
            #penyimpanan struktur terakhir
            if counter_2 == 11:
                last_structure = group[-1]
            
        #melakukan check digit
        check_digit = self.check_sum()
        #menerjemahkan struktur terakhir tadi
        code_translated_last = self.translate(str(check_digit), last_structure)
        #menyimpan ke list lagi
        list_code.append(code_translated_last)

        #penambahan guard bar start, mid, dan end
        list_code.insert(0, '101')
        list_code.insert(7, '01010')
        list_code.append('101')
        
        #penambahan check digit ke EAN
        EAN += str(check_digit)

        #inisiasi barcode yang dimiliki tiap bar
        x_1 = 40
        y_1 = 70
        x_2 = 43
        y_2 = 330

        counter_3 = 0

        #penunjukkan text EAN-13 Barcode        
        self.canvas.create_text(375//2, y_1-20, text = 'EAN-13 Barcode:', font = 'Courier 20')
        #penunjukkan text angka pertama dari barcode
        self.canvas.create_text(x_1-10, y_2+15, text = EAN[0], font = 'Courier 20')

        #mengubah struktur 1 dan 0 menjadi bar hitam dan putih
        for specified in list_code:
            #pengelompokkan sesuai guard bar dan bukan
            if len(specified) == 7:
                counter_3 += 1
                #penampilan text sebelum bar dibuat
                self.canvas.create_text(x_1 + 12, y_2 + 15, text = EAN[counter_3], font = 'Courier 20')
                #pembuatan bar hitam dan putih
                for specific_code in specified:
                    if specific_code == '1':
                        self.canvas.create_rectangle(x_1, y_1, x_2, y_2, fill = 'green', outline = '')
                    elif specific_code == '0':
                        self.canvas.create_rectangle(x_1, y_1, x_2, y_2, fill = 'white', outline = '')
                    x_1 += 3
                    x_2 += 3
            else:
                #pembuatan bar hitam dan putih lebih panjang 20 pixel dari yang biasa
                for specific_code in specified:
                    if specific_code == '1':
                        self.canvas.create_rectangle(x_1, y_1, x_2, y_2 + 20, fill = 'blue', outline = '')
                    elif specific_code == '0':
                        self.canvas.create_rectangle(x_1, y_1, x_2, y_2 + 20, fill = 'white', outline = '')
                    x_1 += 3
                    x_2 += 3

        #menampilkan check digit
        self.canvas.create_text(375//2, y_2 + 50, text = f'check digit : {check_digit}', font = 'Courier 20', fill = 'orange')

        #membuat file post script
        self.canvas.postscript(file = self.string_barcode.get(), colormode = 'color')

#fungsi utama
def main():
    root = Tk()
    window = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()

#barcode standard : https://worldbarcodes.com/barcode-standards/
#899999919564