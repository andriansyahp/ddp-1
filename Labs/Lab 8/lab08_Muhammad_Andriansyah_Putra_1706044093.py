# membuat class Manusia
class Manusia:
    # membuat konstruktor instance
    def __init__(self, nama, stamina):
        self.nama = nama
        self.stamina = stamina
        print("{} telah dihidupkan dengan stamina {}".format(self.nama, self.stamina))

    # membuat method sapa
    def sapa(self, manusia_lain):
        self.stamina += 20
        manusia_lain.stamina += 10
        print("{} sapa {} dengan senang gembira".format(self.nama, manusia_lain.nama))
        print("{} mempunyai stamina sebesar {}".format(self.nama, self.stamina))
        print("{} mempunyai stamina sebesar {}".format(manusia_lain.nama, manusia_lain.stamina))
        # Tambahkan stamina masing-masing manusia

    # membuat method makan
    def makan(self, nama_makanan, jumlah_kalori):
        self.stamina += jumlah_kalori
        print("{} makan {} dengan kalori {}".format(self.nama, nama_makanan, jumlah_kalori))
        print("{} mempunyai stamina sebesar {}".format(self.nama, self.stamina))
        # Tambahkan stamina sesuai dengan ketentuan

    # membuat method tidur
    def tidur(self, jam_tidur):
        self.stamina += 15*jam_tidur
        print("{} tidur  selama {} jam".format(self.nama, jam_tidur))
        print("{} mempunyai stamina sebesar {}".format(self.nama, self.stamina))
        # Tambahkan stamina sesuai dengan ketentuan
        
    # membuat method olahraga
    def olahraga(self, jam_olahraga):
        self.stamina -= 10*jam_olahraga
        print("{} olahraga selama {} jam".format(self.nama, jam_olahraga))
        print("{} mempunyai stamina sebesar {}".format(self.nama, self.stamina))
        # Kurangi stamina sesuai dengan ketentuan
        
    # meng-override function print
    def __str__(self):
        return self.nama + " mempunyai stamina sebesar " + str(self.stamina)
        # Mengembalikan string sesuai format
        # Digunakan saat ingin mencetak data stamina

# Dictionary dengan key nama manusia, dan value object manusia
para_manusia = {}

while (True):
    # meng-split input berdasarkan whitespace
    perintah = input().split()
    if (perintah[0] == 'leave'):
        for nama_manusia in para_manusia:
            print(para_manusia[nama_manusia])
        break
    elif (perintah[0] == 'hidupkan'):
        nama_manusia = perintah[1]
        stamina = int(perintah[-1])
        manusia = Manusia(nama_manusia, stamina)
        para_manusia[nama_manusia] = manusia
    elif (perintah[0] == 'cetak'):
        print(para_manusia[perintah[1]])
    else:
        if (perintah[1] == 'sapa'):
            para_manusia[perintah[0]].sapa(para_manusia[perintah[2]])
        elif (perintah[1] == 'makan'):
              para_manusia[perintah[0]].makan(perintah[2], int(perintah[-1]))
        elif (perintah[1] == 'tidur'):
              para_manusia[perintah[0]].tidur(int(perintah[3]))
        elif (perintah[1] == 'olahraga'):
              para_manusia[perintah[0]].olahraga(int(perintah[3]))
