while True: #membuat program terus meminta input hingga user ingin keluar
    print("Halo! Program ini adalah Andri Converter.") #greetings dari pembuat program terhadap user, dan panduan dalam menggunakan program
    print("Format input: [base]* [number]")
    print("              (*dengan binary atau octal sebagai base)")
    print("Ketik 'sudah selesai' untuk keluar.")

    masukan = input("") #meminta input dari user
    masukan_split = masukan.split(" ") #memisahkan basis dengan angka
    base_input = masukan_split[0] #[base]
    convert_input = masukan_split[1] #[number]

    total=0
    
    if base_input == str("binary"): #membuat blok kondisi jika ingin mengonversi binary
        n = len(convert_input)-1 #untuk mengetahui pangkat tertinggi berdasarkan input
        y =0 #untuk membuat program mengeksekusi index base_input yang pertama
        while n>=0: #membuat program berjalan selama n tidak kurang dari 0   
            x = int(convert_input[y])*(2**n) #mendapatkan nilai hasil kali angka index[y] dengan dua pangkat n, dan merubahnya menjadi tipe integer
            total+=x #untuk membuat nilai total terus bertambah seiring loop
            n-=1 #untuk membuat nilai n terus berkurang hingga 0
            y+=1 #untuk membuat nilai y terus bertambah hingga kondisi n-=1 mencapai n<0 
        print(total) #untuk mencetak hasil konversi
    elif base_input == str("octal"): #membuat blok kondisi jika ingin mengonversi octal
        n = len(convert_input)-1
        y =0
        while n>=0:    
            x = int(convert_input[y])*(8**n)
            total+=x
            n-=1
            y+=1
        print(total)
    elif convert_input == str("selesai"): #membuat blok kondisi jika ingin keluar
        print("Program selesai.") #mencetak bahwa program sudah selesai
        print("="*50) #untuk menambah hiasan
        print()
        exit()
    print("Program selesai.")
    print("="*50)
    print()

