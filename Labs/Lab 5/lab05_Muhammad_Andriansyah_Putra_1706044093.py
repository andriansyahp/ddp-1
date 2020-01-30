file_in = open("lab05input.txt", "r") #membuka lab05input.txt mode membaca
file_out = open("lab05output.txt", "w") #membuat lab05output.txt mode overwrite

for char in file_in:        #membersihkan file dari titik dan membuatnya case-insensitive dengan membuat semua menjadi huruf kecil
    char = char.replace(".", "")
    char = char.lower()
    print(char, file=file_out)

file_in.close() #menutup file input
file_out.close() #menutup file output 

benny = 0 #membuat variabel benny, william dan pardede
william = 0
pardede = 0
file_out = open("lab05output.txt", "r") 
for word in file_out: #men-split text dalam file dan menghitung yang terbanyak
    word = word.split(" ")
    for i in word:
        if i == "benny":
            benny+=1
        elif i == "william":
            william+=1
        elif i == "pardede":
            pardede+=1
    b = {"Benny":benny, "William":william, "Pardede":pardede}
    c = max(b, key = b.get)
    d = max(benny, william, pardede)

file_out = open("lab05output.txt", "w")

print("Orang terfamous 2K17 adalah {} dengan {} suara".format(c,d), file=file_out)  #mencetak hasil
print("{:<10s} mendapat {:>5d} jumlah suara".format("Benny", benny), file = file_out)
print("{:<10s} mendapat {:>5d} jumlah suara".format("William", william), file = file_out)
print("{:<10s} mendapat {:>5d} jumlah suara".format("Pardede", pardede), file = file_out)
file_out.close()
