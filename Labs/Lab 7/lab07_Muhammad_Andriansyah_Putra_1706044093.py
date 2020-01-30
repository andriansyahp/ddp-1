def main():
    # membuat dictionary untuk menampung matkul dan NPM
    matkul = {}                         
    while True:
        masukkan = input(">>> ")
        # keluar dari program jika user menginput 'selesai'
        if masukkan == "selesai":       
            print("Program berhenti!")
            exit()
            
        # memisahkan input user
        masukkan_split = masukkan.split(" ")    

        # menambahkan matkul ke dalam dictionary
        if (masukkan_split[0] == "tambah"):     
            nama_matkul = masukkan_split[1]
            npm_semua = set(int(i) for i in masukkan_split[2:])
            matkul[nama_matkul] = npm_semua
            print(masukkan_split[1],"Berhasil Ditambahkan !")

        # membuat union dari pengambil matkul berdasarkan input user
        elif (masukkan_split[0] == "gabungan"):     
            print(matkul[masukkan_split[1]] | matkul[masukkan_split[2]])

        # mengambil intersection pengambil matkul berdasarkan input user
        elif (masukkan_split[0] == "pengambil"):    
            print(matkul[masukkan_split[1]] & matkul[masukkan_split[2]])

        # mengambil difference dari peserta matkul berdasarkan input user        
        elif(masukkan_split[0] == "hanya"):         
            print(matkul[masukkan_split[1]] - matkul[masukkan_split[2]])

        # mencetak sesuai input user dengan metode selection
        elif (masukkan_split[0] == "cetak"):        
            if masukkan_split[1] == "matkul":
                for k,v in matkul.items():
                    print(k,":", v)                    
            elif masukkan_split[1] != "matkul":
                print(masukkan_split[1], ":", matkul[masukkan_split[1]])            

        else:
            print("Perintah salah !")

main()
