def beli_coklat(jumlah_kecil, jumlah_sedang, jumlah_besar):
    jumlah_kecil = jumlah_kecil * 5000
    jumlah_sedang = jumlah_sedang * 8000
    jumlah_besar = jumlah_besar * 12000
    total_coklat = jumlah_kecil + jumlah_sedang + jumlah_besar
    return [jumlah_kecil, jumlah_sedang, jumlah_besar, total_coklat]

def beli_mie(jumlah_single, jumlah_double):
    jumlah_single = jumlah_single * 2500
    jumlah_double = jumlah_double *3500
    total_mie = jumlah_single + jumlah_double
    return [jumlah_single, jumlah_double, total_mie]

def beli_roti_tawar(jumlah_biasa, jumlah_gandum, jumlah_kupas):
    jumlah_biasa = jumlah_biasa * 12000
    jumlah_gandum = jumlah_gandum * 15000
    jumlah_kupas = jumlah_kupas * 13500
    total_roti = jumlah_biasa + jumlah_gandum + jumlah_kupas
    return [jumlah_biasa, jumlah_gandum, jumlah_kupas, total_roti]

def checkout(total_harga):
    print("Total belanja sebesar "+str(total_harga))
