#================ TP 4 ====================#
#=========== Py-Anoboard 2K17 =============#

# mengimpor modul-modul yang dibutuhkan dalam membuat program
from tkinter import *
from tkinter.font import *
from tkinter import messagebox
import os, pygame, time

# mengkonfigurasi buffer awal pygame.mixer, agar tidak terjadi sound lag delay
pygame.mixer.pre_init(22050, 16, 2, 32)
# inisiasi pygame
pygame.init()

# membuat class untuk membuat piano
class Pyano:
    # memberi attribute dalam class tentang daftar tuts dalam piano
    tuts = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C\'', 'C#', 'D#', 'F#', 'G#', 'A#', 'Db', 'Eb', 'Gb', 'Ab', 'Bb']
    # membuat konstruktor __init__
    def __init__(self, master):
        self.master = master
        # memberi judul pada window
        master.title('Py-ano!')
        # mengambil informasi terkait resolusi layar yang digunakan user
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        # mengubah ukuran window menjadi fullscreen
        master.geometry("{}x{}".format(w, h))

        #======== membuat layout pada window ========#
        # membuat frame home yang menampung semua frame lainnya
        home = Frame(master, bg = '#375ce3')
        home.pack(fill = BOTH)
        # membuat label untuk menuliskan judul program
        title = Label(home, text = 'PY-ANOBOARD 2K17!', font = ('Castellar', 25, 'bold'), fg = 'white', bg = 'black')
        # meletakkan judul di bagian paling atas
        title.pack(side = TOP, pady = 15, fill = X)
        # membuat frame untuk entry yang nantinya digunakan sebagai indikator not
        indicator_frame = Frame(home)
        # meletakkan frame indikator dibawah judul
        indicator_frame.pack(side = TOP, pady = 12)
        # membuat frame berisi entry untuk user menuliskan not secara manual serta tombol play untuk memainkannya
        entry_frame = Frame(home)
        # meletakkan frame untuk entry di bawah frame indikator
        entry_frame.pack(side = TOP, pady = 15)
        # membuat frame berisi radiobutton untuk konfigurasi oktaf
        radiobutton_frame = Frame(home)
        # meletakkan frame untuk radiobutton di bawah frame entry
        radiobutton_frame.pack(side = TOP, pady = 18)
        # membuat frame piano yang menampung frame tuts putih dan frame tuts hitam
        piano_frame = Frame(home, bg = '#0f2442')
        # meletakkan frame untuk piano di bawah frame radiobutton
        piano_frame.pack(side = TOP, fill = X, pady = 10)
        # membuat frame untuk tuts hitam, dan meletakkannya di bagian paling atas dalam frame piano
        black_tuts_frame = Frame(piano_frame)
        black_tuts_frame.pack(side = TOP)
        # membuat frame untuk tuts putih, dan meletakkannya di bawah tuts hitam
        white_tuts_frame = Frame(piano_frame)
        white_tuts_frame.pack(side = TOP)

        #========== membuat entry yang digunakan sebagai indikator not piano ==========#
        # karena hanya berfungsi sebagai indikator maka state = readonly agar user--
        # --tidak dapat mengubah-ubah isinya saat menggunakan program
        self.indicator = StringVar()
        textDisplay = Entry(indicator_frame, textvariable = self.indicator, bd = 8, insertwidth = 2,
                            font = ('Calibri', 16), justify = 'center', width = 6, state = 'readonly')
        textDisplay.pack(side = TOP)

        #========== membuat entry yang digunakan untuk menuliskan not secara manual ==========#
        self.partiture = StringVar()
        part = Entry(entry_frame, textvariable = self.partiture, bd = 8, insertwidth = 2,
                    font = ('Calibri', 16), justify = 'center', width = 80)
        # membuat default value dalam entry, sekaligus sebagai panduan awal menggunakan program
        # capslock digunakan sebagai pembeda dalam binding keyboard, agar tidak bertabrakan penggunaannya antara--
        # --saat menggunakan keyboard untuk bermain piano dengan menuliskan not secara manual di entry
        part.insert(0, "Turn on the CapsLock before typing here, turn it off to play with keyboard")
        part.pack(side = LEFT)
        # membuat button play yang terletak di sebelah kanan entry untuk memainkan not yang telah dituliskan pada entry
        play = Button(entry_frame, text = 'PLAY!', bg = '#c20e0e', fg = 'white', height = 2, width = 7,
                        relief = RIDGE, command = self.play_partiture)
        play.pack(side = LEFT)
        # mem-bind tombol 'enter' pada keyboard agar user dapat langsung memainkan not dengan mengklik--
        # --'enter' pada keyboard selain dengan mengklik tombol play di sebelahnya
        part.bind('<Return>', self.play_partiture)
        # mem-bind 'left-click mouse' agar menghilangkan kursor pada entry saat tidak digunakan dengan memindahkan focusnya
        master.bind_all("<Button-1>", lambda event : event.widget.focus_set())

        #====== membuat radiobutton untuk konfigurasi oktaf sesuai keinginan user ======#
        self.octave = IntVar()
        # mengatur default value radiobutton dengan oktaf normal pada umumnya yaitu 4
        self.octave.set(4)
        # membuat radiobutton dengan cara iterasi
        for i in range(1,8):
            Radiobutton(radiobutton_frame, text = str(i), variable = self.octave, value = i, bg = '#375ce3',
                        font = ('Helvetica', 16)).pack(side = LEFT)
        octs = self.octave.get()

        #======== membuat piano yang berisi tuts hitam, filler (celah) antar tuts serta tuts putih ========#
        # membuat default font untuk tuts hitam dan putih
        tuts_font = Font(family = 'Consolas', weight = 'bold')
        # membuat button untuk tuts hitam dan filler (celah) nya secara bergantian sesuai bentuk piano asli
        filler1 = Button(black_tuts_frame, bg = '#898874', width = 5, relief = RAISED, command = self.play_C)
        filler1.pack(side = LEFT, fill = Y)
        Cs = Button(black_tuts_frame, height = 8, width = 7, bd = 8, text = 'Db\n\n\nC#', bg = 'black',
                    fg = 'white', font = tuts_font, command = self.play_Cs)
        Cs.pack(side = LEFT)
        filler2 = Button(black_tuts_frame, bg = '#EBDCCB', width = 1, relief = RAISED, command = self.play_D)
        filler2.pack(side = LEFT, fill = Y)
        Ds = Button(black_tuts_frame, height = 8, width = 7, bd = 8, text = 'Eb\n\n\nD#', bg = 'black',
                    fg = 'white', font = tuts_font, command = self.play_Ds)
        Ds.pack(side = LEFT)
        filler3 = Button(black_tuts_frame, bg = '#6B645D', width = 6, relief = RAISED, command = self.play_E)
        filler3.pack(side = LEFT, fill = Y)
        filler4 = Button(black_tuts_frame, bg = '#C3BAAA', width = 5, relief = RAISED, command = self.play_F)
        filler4.pack(side = LEFT, fill = Y)
        Fs = Button(black_tuts_frame, height = 8, width = 7, bd = 8, text = 'Gb\n\n\nF#', bg = 'black',
                    fg = 'white', font = tuts_font, command = self.play_Fs)
        Fs.pack(side = LEFT)
        filler5 = Button(black_tuts_frame, bg = '#91818A', width = 1, relief = RAISED, command = self.play_G)
        filler5.pack(side = LEFT, fill = Y)
        Gs = Button(black_tuts_frame, height = 8, width = 7, bd = 8, text = 'Ab\n\n\nG#', bg = 'black',
                    fg = 'white', font = tuts_font, command = self.play_Gs)
        Gs.pack(side = LEFT)
        filler6 = Button(black_tuts_frame, bg = '#B2A3B5', width = 1, relief = RAISED, command = self.play_A)
        filler6.pack(side = LEFT, fill = Y)
        As = Button(black_tuts_frame, height = 8, width = 7, bd = 8, text = 'Bb\n\n\nA#', bg = 'black',
                    fg = 'white', font = tuts_font, command = self.play_As)
        As.pack(side = LEFT, fill = Y)
        filler7 = Button(black_tuts_frame, bg = '#514B53', width = 4, relief = RAISED, command = self.play_B)
        filler7.pack(side = LEFT, fill = Y)
        filler8 = Button(black_tuts_frame, bg = '#413C42', width = 12, relief = RAISED, command = self.play_C1)
        filler8.pack(side = LEFT, fill = Y)

        # menggunakan dictionary untuk membuat tuts putih dengan singkat
        # dictionary berisi warna, command serta not untuk tutsnya
        attribute = [['#898874', self.play_C], ['#EBDCCB', self.play_D], ['#6B645D', self.play_E],
                    ['#C3BAAA', self.play_F], ['#91818A', self.play_G], ['#B2A3B5', self.play_A],
                    ['#514B53', self.play_B], ['#413C42', self.play_C1]]
        whiteTuts_attr = dict(zip(self.tuts, attribute))
        # membuat button untuk tuts putih dengan cara iterasi dictionary
        for button, attr in whiteTuts_attr.items():
            Button(white_tuts_frame, bd = 8, height = 11, width = 8, text = button, font = tuts_font, fg = 'black',
                    bg = whiteTuts_attr[button][0], command = whiteTuts_attr[button][1]).pack(side = LEFT)

        #========== keyboard binding, agar dapat memainkan piano menggunakan keyboard =========#
        # sekali lagi, menggunakan dictionary
        keys = [',', '.', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'w', 'e', 't', 'y', 'u']
        acts = [self.octave_down, self.octave_up, self.play_C, self.play_D, self.play_E, self.play_F,
                self.play_G, self.play_A, self.play_B, self.play_C1, self.play_Cs, self.play_Ds,
                self.play_Fs, self.play_Gs, self.play_As]
        keyboard_bind = dict(zip(keys, acts))
        for key, val in keyboard_bind.items():
            master.bind(key, val)

    #============ membuat fungsi untuk memainkan not piano ============#
    # event = None sebagai default value, karena digunakan juga dalam keyboard binding
    # sehingga saat tidak memainkan dengan keyboard, event = None
    # namun ketika memainkan dengan keyboard, eventnya mengambil event sesuai tombol yang--
    # --ditekan pada keyboard dalam keyboard binding
    def play_C(self, event = None):
        # mengambil value oktaf dari radiobutton
        self.indicator.set('C{}'.format(self.octave.get()))
        # menggunakan pygame.mixer.Sound() untuk mengakses sound
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.C{}.wav'.format(self.octave.get())))
        # memainkan sound dengan waktu maksimal 2500 ms/ 2,5 detik
        sound.play(maxtime=2500)

    def play_D(self, event = None):
        self.indicator.set('D{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.D{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    def play_E(self, event = None):
        self.indicator.set('E{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.E{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    def play_F(self, event = None):
        self.indicator.set('F{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.F{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    def play_G(self, event = None):
        self.indicator.set('G{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.G{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    def play_A(self, event = None):
        self.indicator.set('A{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.A{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    def play_B(self, event = None):
        self.indicator.set('B{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.B{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    def play_C1(self, event = None):
        self.indicator.set('C\'')
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.C8.wav'))
        sound.play(maxtime=2500)

    def play_Cs(self, event = None):
        self.indicator.set('C#{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.Db{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    def play_Ds(self, event = None):
        self.indicator.set('D#{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.Eb{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    def play_Fs(self, event = None):
        self.indicator.set('F#{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.Gb{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    def play_Gs(self, event = None):
        self.indicator.set('G#{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.Ab{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    def play_As(self, event = None):
        self.indicator.set('A#{}'.format(self.octave.get()))
        sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'tp4_piano.zip.zip.zip',
                'Piano.mf.Bb{}.wav'.format(self.octave.get())))
        sound.play(maxtime=2500)

    #==== membuat fungsi untuk menaikkan dan menurunkan oktaf, untuk konfigurasi saat memainkan piano dengan keyboard ====#
    def octave_up(self, event = None):
        octs = self.octave.get()
        octs += 1
        self.octave.set(octs)

    def octave_down(self, event = None):
        octs = self.octave.get()
        octs -= 1
        self.octave.set(octs)

    #========== membuat fungsi untuk memainkan not piano dalam entry yang dituliskan secara manual ==========#
    def play_partiture(self, event = None):
        parts = self.partiture.get().split()
        # sekali lagi, menggunakan dictionary
        acts = [self.play_C, self.play_D, self.play_E, self.play_F, self.play_G, self.play_A, self.play_B,
                self.play_C1, self.play_Cs, self.play_Ds, self.play_Fs, self.play_Gs, self.play_As,
                self.play_Cs, self.play_Ds, self.play_Fs, self.play_Gs, self.play_As]
        play = dict(zip(self.tuts, acts))
        for notes in parts:
            try:
                # membuat selection apakah not yang dimasukkan memiliki panjang 3
                if len(notes) == 3:
                    # seleksi apakah not ada pada dictionary
                    if notes[0:2].capitalize() in self.tuts:
                        # seleksi jika not ada pada dictionary, apakah input oktafnya benar atau salah
                        # jika salah, masuk ke suite ini (memunculkan ValueError)
                        if notes[2].isdigit() == False or int(notes[2]) > 7:
                            raise ValueError
                        # jika not ada pada dictionary dan input oktafnya benar maka not dapat dimainkan
                        self.octave.set(notes[2])
                        self.indicator.set(notes)
                        # memainkan not dengan mengambil value dalam dictionary
                        play[notes[0:2].capitalize()]()
                    # jika not memiliki panjang 3 namun tidak ada pada dictionary, maka masuk ke suite else
                    else:
                        # menggunakan submodul messagebox dalam modul tkinter untuk memunculkan error window
                        # isinya memberitahukan not mana yang tidak sesuai format, ditandai dengan '***'
                        messagebox.showerror("Invalid input", self.partiture.get().replace(notes, ('***'+ notes)))
                        break
                # jika not yang dimasukkan memiliki panjang 2, maka masuk ke suite ini
                elif len(notes) == 2:
                    if notes[0].capitalize() in self.tuts:
                        if notes[1].isdigit() == False or int(notes[1]) > 7:
                            raise ValueError
                        self.octave.set(notes[1])
                        self.indicator.set(notes)
                        play[notes[0].capitalize()]()
                    else:
                        messagebox.showerror("Invalid input", self.partiture.get().replace(notes, ('***'+ notes)))
                        break
                # jika not yang dimasukkan tidak berpanjang 2 atau 3, maka input tidak sesuai format dan masuk ke suite else
                else:
                    messagebox.showerror("Invalid input", self.partiture.get().replace(notes, ('***'+ notes)))
                    break
                # meng-update perubahan pada entry setiap iterasi
                self.master.update()
                # memberi jeda tiap memainkan not yaitu 0,75 detik
                time.sleep(0.75)
            # menangkap semua jenis error jika terjadi error pada entry
            except:
                messagebox.showerror("Invalid input", self.partiture.get().replace(notes, ('***'+ notes)))
                break
#============ inisiasi GUI ============#
root = Tk()
gui = Pyano(root)
root.mainloop()
