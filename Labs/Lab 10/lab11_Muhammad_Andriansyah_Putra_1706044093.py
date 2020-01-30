from tkinter import *

class Kalkulator():
    def __init__(self, master):
        # Membuat title window menjadi "Kalkulator Sederhana"
        self.master = master
        master.title('Kalkulator Sederhana')

        # Membuat Label, Entry, Button,
        # dan komponen-komponen lain yang dibutuhkan.
        self.in_num1 = StringVar()
        self.in_num2 = StringVar()
        Label(master, text = 'Bilangan 1: ', bg = 'black', fg = 'white').grid(row = 1, column = 1)
        Entry(master, textvariable = self.in_num1).grid(row = 1, column = 2, columnspan = 4)
        Label(master, text = 'Bilangan 2: ', bg = 'black', fg = 'white').grid(row = 2, column = 1)
        Entry(master, textvariable = self.in_num2).grid(row = 2, column = 2, columnspan = 4)

        # button untuk operasi
        plus = Button(master, text = 'tambah', command = self.tambah, bg = 'black', fg = 'white').grid(row = 3, column = 1)
        difference = Button(master, text = 'kurang', command = self.kurang, bg = 'black', fg = 'white').grid(row = 3, column = 2)
        multiply = Button(master, text = 'kali', command = self.kali, bg = 'black', fg = 'white').grid(row = 3, column = 3)
        divide = Button(master, text = 'bagi', command = self.bagi, bg = 'black', fg = 'white').grid(row = 3, column = 4)

        # label untuk output hasil
        self.out_num = Label(master, text = 'Hasil :\n ')
        self.out_num.grid(row = 4, column = 2)

    # membuat method tambah, kurang kali dan bagi dan memberi output pada Label
    def tambah(self):
        try:
            self.out_num['text'] = 'Hasil :\n{}'.format(str(float(self.in_num1.get()) + float(self.in_num2.get())))
        except ValueError:
            self.out_num['text'] = 'Operasi gagal;\nInput tidak sesuai'
        # mengimplementasikan fungsi tambah


    def kurang(self):
        try:
            self.out_num['text'] = 'Hasil :\n{}'.format(str(float(self.in_num1.get()) - float(self.in_num2.get())))
        except ValueError:
            self.out_num['text'] = 'Operasi gagal;\nInput tidak sesuai'
        # mengimplementasikan fungsi kurang


    def kali(self):
        try:
            self.out_num['text'] = 'Hasil :\n{}'.format(str(float(self.in_num1.get()) * float(self.in_num2.get())))
        except ValueError:
            self.out_num['text'] = 'Operasi gagal;\nInput tidak sesuai'
        # mengimplementasikan fungsi kali

    def bagi(self):
        try:
            self.out_num['text'] = 'Hasil :\n{}'.format(str(float(self.in_num1.get()) / float(self.in_num2.get())))
        except ValueError:
            self.out_num['text'] = 'Operasi gagal;\nInput tidak sesuai'
        except ZeroDivisionError:
            self.out_num['text'] = 'Operasi gagal;\nPembagian dengan nol'
        # mengimplementasikan fungsi bagi

root = Tk()
gui = Kalkulator(root)
root.mainloop()
