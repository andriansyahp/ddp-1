print("Selamat Datang di Andri's Decryptor!") #Sapaan programmer kepada user
while True: #untuk membuat program terus meminta input
    encrypted = input("Pesan: ") #meminta input pada user untuk kata yang ingin didekripsi
    key = int(input("Key: ")) #meminta input pada user untuk key dalam enkripsi

    masterkey=key #untuk meng-assign nilai masterkey sama dengan nilai key, yang akan digunakan dalam loop
    m=0 #untuk acuan dalam awal loop 
    for i in encrypted: #membuat loop untuk dekripsi 
        decrypted = (encrypted[m:key]) #mendekripsi dengan cara slice
        key+=masterkey #membuat key bertambah seiring loop
        m+=masterkey #membuat acuan dalam slicing bergeser sejauh m yang berubah seiring loop
        print(decrypted[::-1], end="") #mencetak hasil dekripsi
    print() #membuat baris baru, agar membantu readability

    
    
