import turtle

nama = input("Namamu: ") #Meminta nama user
print("Halo, " + nama + "!" + " " + "Benny ingin membuat segi empat. \n Bantulah Benny membuat segi empat!")

sisi = int(input("Berapa panjang sisi segi empat yang kamu inginkan, " + nama +"? \n ="))#Meminta input panjang segi empat yang diinginkan user


t = turtle.Turtle() #Instansiasi​ ​objek​ ​turtle

t.pendown() #​ ​Mengaktifkan​ ​pena
t.color("orange") #​ ​Menggunakan​ ​tinta​ warna ​orange
t.forward(sisi)#​ ​Bergerak​ ​maju​ ​sejauh​ ​input pada variabel sisi
t.left(90)#Berbelok​ ke arah kiri ​sebesar​ ​90​ ​derajat
t.forward(sisi)
t.left(90)
t.forward(sisi)
t.left(90)
t.forward(sisi)

t.penup()#​ ​Menon-aktifkan​ ​pena

turtle.exitonclick()#​ ​Menutup​ ​turtle​ ​setelah​ ​di-​click
