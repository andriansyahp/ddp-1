import math #mengimpor modul math dari python

nama = (input("Halo! Namamu?: ")) #meminta input nama user
print(nama + ", " + "Masukkan angka yang diinginkan.") 
vo = float(input("Kecepatan awal (m/s): ")) #meminta input user dalam kecepatan awal, dan mengubahnya ke tipe float
alfa = float(input("Sudut (derajat): ")) 
t = float(input("Waktu (s): ")) 

alfa = math.radians(alfa) #mengubah sudut dari derajat ke radian 
vox = vo*math.cos(alfa) #rumus kecepatan horizontal
voy = vo*math.sin(alfa) #rumus kecepatan vertikal
x = vox*t #rumus jarak 
y = voy*t -(0.5*9.8*(t**2)) #rumus ketinggian
x = str(float('%.2f'%x)) #menampilkan 2 digit di belakang koma 
y = str(float('%.2f'%y)) 

print("Jarak: " + x + " meter") #mencetak hasil jarak
print("Ketinggian: " + y + " meter") #mencetak hasil ketinggian
print("Program selesai!")
