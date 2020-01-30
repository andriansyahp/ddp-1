import bennymart
print("Selamat datang di BennyMart !")
print("Format input: beli [barang] [x] [y] [z]")
input_belanja = input("\n = ")
input_split = input_belanja.split(" ")
barang = input_split[1]
jenis1 = int(input_split[2])
jenis2 = int(input_split[3])
jenis3 = int(input_split[4])

total_harga_coklat = bennymart.beli_coklat(jenis1, jenis2, jenis3)
total_harga_mie = bennymart.beli_mie(jenis1, jenis2)
total_harga_roti = bennymart.beli_roti_tawar(jenis1, jenis2, jenis3)

if barang == "coklat":
    if jenis1 != 0:
        print("Membeli coklat kecil sebanyak", jenis1, "seharga", total_harga_coklat[0])
    elif jenis1 == 0:
        print(end='')
    if jenis2 != 0:
        print("Membeli coklat sedang sebanyak", jenis2, "seharga", total_harga_coklat[1])
    elif jenis2 == 0:
        print(end='')
    if jenis3 != 0:
        print("Membeli coklat besar sebanyak", jenis3, "seharga", total_harga_coklat[2])
    elif jenis3 == 0:
        print(end='')
elif barang == "mie":
    if jenis1 != 0:
        print("Membeli mie single sebanyak", jenis1, "seharga", total_harga_mie[0])
    elif jenis1 == 0:
        print(end='')
    if jenis2 != 0:
        print("Membeli mie double sebanyak", jenis2, "seharga", total_harga_mie[1])
    elif jenis2 == 0:
        print(end='')
elif barang == "roti":
    if jenis1 != 0:
        print("Membeli roti tawar biasa sebanyak", jenis1, "seharga", total_harga_roti[0])
    elif jenis1 == 0:
        print(end='')
    if jenis2 != 0:
        print("Membeli roti tawar gandum sebanyak", jenis2, "seharga", total_harga_roti[1])
    elif jenis2 == 0:
        print(end='')
    if jenis3 != 0:
        print("Membeli roti tawar kupas sebanyak", jenis3, "seharga", total_harga_roti[2])
    elif jenis3 == 0:
       print(end='')
total_harga = total_harga_coklat[3] + total_harga_mie[2] +total_harga_roti[3]
bennymart.checkout(total_harga)
