import turtle   #mengimpor modul turtle
import random   #mengimpor modul random
from turtle import Screen   #mengimpor submodul screen dari modul turtle

user_name = turtle.textinput("Greetings!", "Hello! Welcome to Andri's Colorful Flower and Chessboard Drawer! \n Can I have your name?") #sapaan programmer kepada user
a = "Nice to meet you, " + user_name +"! \n Press 'enter' on your keyboard to proceed."
turtle.textinput("Hello!", a)

squares_rows = int(turtle.numinput("Chessboard", "How many rows (and columns) of squares do you want to make?", minval=2, maxval=15)) #meminta input user untuk jumlah baris dan kolom papan catur, dengan input minimal 2 dan maksimal 15
squares_side = int(turtle.numinput("Chessboard", "How long is the sides of squares do you prefer? (in pixel)", minval=10, maxval=20)) #meminta input user untuk panjang sisi kotak penyusun papan catur, dengan input minimal 10 dan maksimal 20
flowers_petals = int(turtle.numinput("Flower", "How many flower's petals do you wish to appear?", minval=1, maxval=50))     #meminta input user untuk jumlah kelopak bunga, dengan input minimal 1 dan maksimal 50

t = turtle.Turtle() #inisiasi objek turtle
screen = Screen() #inisiasi objek screen
screen.setup(width=.5, height=.75, startx=None, starty=None) #mengatur besar main window dari turtle, dan meletakkannya di tengah layar
t.hideturtle() #menyembunyikan turtle agar tidak terlihat saat animasi
t.speed(0) #mengatur kecepatan animasi turtle menjadi 'fastest'
t.up() #menon-aktifkan pena saat bergerak
t.goto(0, 160) #menuju koordinat (0, 160) pada layar
t.down() #mengaktifkan pena
screen.colormode(255) #mengatur jenis mode warna yang digunakan, yaitu mode RGB

for i in range(flowers_petals):     #loop untuk membuat satu petal berulang sejumlah input user
    t.pensize(2) #membesarkan ukuran pena yang digunakan menjadi 2 pixel
    heading = t.heading() #membuat objek heading berupa arah awal sebelum bergerak dari turtle
    r = random.randrange(0, 255, 10) #membuat variabel warna#
    g = random.randrange(0, 255, 10) #secara acak#
    b = random.randrange(0, 255, 10) #dengan range 0 sampai 255, dan step 10 agar perbedaan warna tampil mencolok#
    t.color(r, g, b) #mengatur warna yang digunakan secara random
    t.circle(100,60) #membuat setengah kelopak bunga berupa busur lingkaran dengan radius 100 pixel dan sudut 60 derajat
    t.left(120) #berbelok ke kiri sejauh 120 derajat
    t.circle(100,60) #membuat busur lingkaran untuk menyempurnakan setengah kelopak tadi
    t.setheading(heading) #mengembalikan heading/arah gerak turtle seperti arah awal di variabel heading
    t.left(360 / flowers_petals) #berbelok ke kiri sejauh (360 derajat dibagi jumlah kelopak dari input user), untuk membuat kelopak bunga lainnya secara simetris

t.up()
xcor, ycor = (squares_side*squares_rows)/-2, 20 #membuat variabel xcor dan ycor yang merupakan koordinat untuk papan catur
t.goto(xcor, ycor)
t.down()

n = squares_rows #membuat singkatan untuk variabel squares_rows
y = 0 #membuat variabel y sebagai titik acuan koordinat y

for i in range(n):      #loop untuk membuat kolom berdasarkan baris sejumlah input user
    for i in range(n):      #loop untuk membuat baris dari kotak berulang sejumlah input user
        t.pensize(1) #mengembalikan ukuran pena yang digunakan menjadi 1 pixel (ukuran normal)
        r = random.randrange(0, 255, 10)
        g = random.randrange(0, 255, 10)
        b = random.randrange(0, 255, 10)
        t.color(r, g, b)
        t.begin_fill() #titik mulai untuk mengisi warna pada kotak
        for i in range(4):      #loop untuk membuat satu kotak 
            t.forward(squares_side)
            t.right(90)
        t.forward(squares_side)
        t.end_fill() #titik akhir untuk mengisi warna pada kotak
    t.up()
    t.setx(xcor)     #mengembalikan posisi x ke koordinat xcor#
    y+=squares_side  #dan mengatur posisi y#
    t.sety(ycor-y)   #yang berubah seiring loop#
    t.down()

t.up()
t.goto(0, ycor-(squares_side*squares_rows)-60) #menuju titik koordinat untuk membuat tulisan
end = "Colorful Chessboard of " + str((squares_rows**2)) + " Squares and Flower of " + str(flowers_petals) + " Petals"
t.color("blue") #mengatur warna yang digunakan untuk menulis menjadi biru
t.write(end, False, align="center", font=("Calibri", 18, "normal")) #membuat tulisan dengan posisi tengah, font Calibri ukuran 18p jenis normal
turtle.exitonclick() #mengatur agar window turtle ditutup setelah diklik


 
    
    
    

