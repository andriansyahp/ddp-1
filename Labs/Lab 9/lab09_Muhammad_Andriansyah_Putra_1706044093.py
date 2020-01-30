class Pegawai:
    def __init__(self,nama,rate_gaji): #konstruktor instansiasi objek
        self.nama = nama
        self.rate_gaji = rate_gaji
        self.jam_kerja = 0

    def __str__(self,divisi): #overrride fungsi print
        return '{} seorang {}, jam kerja : {}'.format(self.nama, divisi, self.jam_kerja)

    def tambah_jam_kerja(self,jam_kerja): #menambah jam kerja
        self.jam_kerja += jam_kerja

    def gajian(self): #mencetak perolehan gaji sekaligus keluar dari program
        gaji = self.jam_kerja*self.rate_gaji
        print('{} menerima gaji sebanyak Rp.{}'.format(self.nama, gaji))




class Staff(Pegawai): #membuat subclass Staff dari parent class Pegawai
    def __init__(self,nama):
        super().__init__(nama,75000) #memberi rate gaji untuk fungsi di parent class

    def __str__(self):
        return super().__str__('Staff') #memberi parameter divisi untuk fungsi di parent class

    def NGANTOR(self, jam_kerja):
        super().tambah_jam_kerja(jam_kerja)
        print('{} bekerja di kantor selama {} jam'.format(self.nama, jam_kerja))

class Filmmaker(Pegawai):
    def __init__(self,nama):
        super().__init__(nama,100000)
        
    def __str__(self):
        return super().__str__('Filmmaker')

    def PRODUKSI(self, jam_kerja):
        super().tambah_jam_kerja(jam_kerja)
        print('{} membuat konten video baru selama {} jam'.format(self.nama, jam_kerja))

class Marketing(Pegawai):
    def __init__(self,nama):
        super().__init__(nama,50000)

    def __str__(self):
        return super().__str__('Marketing')

    def PROMOSI(self, jam_kerja):
        super().tambah_jam_kerja(jam_kerja)
        print('{} mempromosikan channel Pardede Productions selama {} jam'.format(self.nama, jam_kerja))

def main():

    daftar_pegawai = {} #membuat dictionary untuk pegawai

    while True:
        masukan = input()

        if(masukan == "GAJIAN"):
            # akses semua pegawai satu per satu,
            # lalu panggil fungsi untuk melakukan gajian
            for pegawai in daftar_pegawai:
                daftar_pegawai[pegawai].gajian()
            break

        masukan_split = masukan.split(";")


        if(masukan_split[0] == "REKRUT"):
            # dapatkan nilai ini dari masukan_split sesuai indexnya (lihat format input)
            nama = masukan_split[1]
            divisi = masukan_split[2]

            # lakukan selection untuk menentukan tipe Pegawai
            if(divisi == "Staff"):
                pegawai = Staff(nama) #instansiasi objek
            elif(divisi == "Filmmaker"):
                pegawai = Filmmaker(nama)
            elif(divisi == "Marketing"):
                pegawai = Marketing(nama)

            daftar_pegawai[nama] = pegawai
            print('Pegawai dengan nama {} bergabung dengan Pardede Productions sebagai {}'.format(nama, divisi))
            # memasukkan pegawai yang sudah dibuat ke dalam dictionary
            # kemudian mencetak pesan sesuai format

        elif(masukan_split[0] == "INFO"):
            nama = masukan_split[1]
            pegawai = daftar_pegawai[nama] #mendapatkan objek pegawai berdasarkan namanya
            print(pegawai)

        else:
            # Jika masuk ke bagian ini, artinya input berupa NGANTOR,PRODUKSI, atau PROMOSI

            # dapatkan atribut dan objek yang diperlukan
            nama = masukan_split[1]
            jam_kerja = int(masukan_split[2]) # jam_kerja dalam int
            pegawai =  daftar_pegawai[nama]

            # lakukan selection menentukan perintah tipe apa
            if (masukan_split[0] == "NGANTOR"): # STAFF
                # ganti True dengan suatu pengecekan apakah pegawai merupakan instance dari Staff
                if (isinstance(pegawai,Staff)):
                    pegawai.NGANTOR(jam_kerja)

                else:
                    print('Pegawai dengan nama {} bukan seorang Staff'.format(nama))


            # lakukan hal sama untuk FILMMAKER
            elif (masukan_split[0] == "PRODUKSI"): # FILMMAKER
                if (isinstance(pegawai, Filmmaker)):
                    pegawai.PRODUKSI(jam_kerja)

                else:
                    print('Pegawai dengan nama {} bukan seorang Filmmaker'.format(nama))


            # lakukan hal sama untuk MARKETING
            elif(masukan_split[0] == "PROMOSI"): # MARKETING
                if(isinstance(pegawai, Marketing)):
                    pegawai.PROMOSI(jam_kerja)

                else:
                    print('Pegawai dengan nama {} bukan seorang Marketing'.format(nama))


if __name__ == "__main__":
    main()
