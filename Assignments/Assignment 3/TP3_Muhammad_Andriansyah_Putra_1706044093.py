# membuat class
class PardedeFinance:
    # membuat konstruktor
    def __init__(self, name, account_type, balance, transaction):
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.transaction = transaction

        # memberi attribute masing-masing instance sesuai tipe akun
        if (account_type == 'Pelajar'):
            self.transaction_limit = 25
            self.savings_limit = 150
            self.transaction_fee = 0

        elif (account_type == 'Reguler'):
            self.transaction_limit = 100
            self.savings_limit = 500
            self.transaction_fee = 5

        elif (account_type == 'Bisnis'):
            self.transaction_limit = 500
            self.savings_limit = 2000
            self.transaction_fee = 15

        elif (account_type == 'Elite'):
            self.transaction_limit = 10000
            self.savings_limit = 100000
            self.transaction_fee = 50

        # mencetak sesuai format
        print('Akun atas nama {} telah terdaftar dengan paket {}'.format(self.name, self.account_type))

    # membuat method setor tabungan
    def SETOR(self, amount_of_money, currency):
        # mengubah nominal uang yang disetor sesuai rate mata uang yang ada di dictionary mata uang
        Ben_Currency = float(amount_of_money//currencies[currency])
        # membuat kondisi jika tabungan sudah mencapai batas tabungan dari tipe akunnya
        if (self.balance == self.savings_limit):
            print('Akun {} sudah memenuhi kapasitas'.format(self.name))

        # membuat kondisi jika saldo tabungan setelah penyetoran melebihi batas tabungan dari tipe akunnya
        elif ((self.balance + Ben_Currency) > self.savings_limit):
            # mengubah jumlah BenCoin yang disetor menjadi selisih batas tabungan dengan jumlah tabungannya agar tidak melebihi batas tabungan akun
            Ben_Currency = float(self.savings_limit - self.balance)
            self.balance += Ben_Currency
            print('Akun {} telah bertambah {} BenCoin'.format(self.name, Ben_Currency))
            self.transaction.append('SETOR {} {} {}'.format(currency, amount_of_money, Ben_Currency))        

        # jika tidak bermasalah, maka masuk ke suite di else
        else:
            self.balance += Ben_Currency
            print('Akun {} telah bertambah {} BenCoin'.format(self.name, Ben_Currency))
            self.transaction.append('SETOR {} {} {}'.format(currency, amount_of_money, Ben_Currency))

    # membuat method penarikan tabungan
    def TARIK(self, amount_of_BenCoin, currency):
        # membuat kondisi jika tidak memiliki saldo di tabungan untuk ditarik
        if (self.balance == 0):
            print('Akun {} tidak cukup untuk melakukan penarikan'.format(self.name))

        # membuat kondisi jika jumlah uang yang ditarik setelah terkena biaya transaksi melebihi saldo tabungan
        elif ((self.balance - amount_of_BenCoin) < 0):
            # mengubah jumlah yang ditarik menjadi sisa saldo
            amount_of_BenCoin = self.balance
            # membuat jumlah bersih setelah dikurangi biaya transaksi, kemudian mengkonversi menjadi uang sesuai rate mata uang di dictionary mata uang
            half_netto = (amount_of_BenCoin-self.transaction_fee)
            netto_amount = half_netto*currencies[currency]
            self.balance -= amount_of_BenCoin
            self.transaction.append('TARIK {} {} {}'.format(self.name, netto_amount, half_netto))
            print('Penarikan {} dari akun {} berhasil!'.format(netto_amount, self.name))

        # membuat kondisi jika nominal penarikan melebihi batas transaksi
        elif (amount_of_BenCoin > self.transaction_limit):
            # mengubah jumlah yang ditarik menjadi batas transaksi
            amount_of_BenCoin = self.transaction_limit
            # membuat jumlah bersih setelah dikurangi biaya transaksi, kemudian mengkonversi menjadi uang sesuai rate mata uang di dictionary mata uang
            half_netto = (amount_of_BenCoin-self.transaction_fee)
            netto_amount = half_netto*currencies[currency]
            self.balance -= amount_of_BenCoin
            self.transaction.append('TARIK {} {} {}'.format(self.name, netto_amount, half_netto))
            print('Penarikan {} dari akun {} berhasil!'.format(netto_amount, self.name))

        # jika tidak bermasalah, maka masuk ke suite di else
        else:
            half_netto = (amount_of_BenCoin-self.transaction_fee)
            netto_amount = half_netto*currencies[currency]
            self.balance -= amount_of_BenCoin
            self.transaction.append('TARIK {} {} {}'.format(self.name, netto_amount, half_netto))
            print('Penarikan {} dari akun {} berhasil!'.format(netto_amount, self.name))

    # membuat method transfer uang antar nasabah
    def TRANSFER(self, receiver, amount_of_BenCoin):
        # membuat jumlah biaya yang dibutuhkan, yaitu nominal transfer ditambah biaya transaksi
        fee = amount_of_BenCoin + self.transaction_fee
        # membuat kondisi jika pengirim transfer tidak memiliki saldo untuk ditransfer
        if (self.balance == 0):
            print('Akun {} tidak cukup untuk melakukan transfer'.format(self.name))

        # membuat kondisi jika saldo penerima telah mencapai batas tabungan akunnya
        elif (receiver.balance == receiver.savings_limit):
            print('Akun {} sudah memenuhi kapasitas'.format(receiver.name))

        # membuat kondisi jika saldo tabungan penerima setelah transfer melebihi batas tabungan akunnya
        elif ((receiver.balance + amount_of_BenCoin) > receiver.savings_limit):
            # mengubah jumlah BenCoin yang ditransfer menjadi selisih batas tabungan akun dengan saldo akun sehingga tidak melebihi batas tabungan
            amount_of_BenCoin = receiver.savings_limit - receiver.balance
            receiver.balance += amount_of_BenCoin
            # fee sebagai biaya bagi pengirim, yaitu jumlah BenCoin yang ditransfer dengan biaya transaksi
            fee = amount_of_BenCoin + self.transaction_fee
            self.balance -= fee
            print('{} berhasil mentransfer {} BenCoin kepada {}'.format(self.name, amount_of_BenCoin, receiver.name))
            self.transaction.append('MENTRANSFER {} {}'.format(receiver.name, amount_of_BenCoin))
            receiver.transaction.append('DITRANSFER {} {}'.format(self.name, amount_of_BenCoin))

        # membuat kondisi jika saldo tabungan pengirim tidak cukup untuk melakukan transfer
        elif ((self.balance - fee) <= 0):
            # mengubah jumlah yang ditransfer menjadi selisih saldo pengirim dengan biaya transaksi
            amount_of_BenCoin = self.balance - self.transaction_fee
            receiver.balance += amount_of_BenCoin
            fee = amount_of_BenCoin + self.transaction_fee
            self.balance -= fee
            print('{} berhasil mentransfer {} BenCoin kepada {}'.format(self.name, amount_of_BenCoin, receiver.name))
            self.transaction.append('MENTRANSFER {} {}'.format(receiver.name, amount_of_BenCoin))
            receiver.transaction.append('DITRANSFER {} {}'.format(self.name, amount_of_BenCoin))

        # membuat kondisi jika jumlah BenCoin yang ditransfer melebihi batas transaksi dari pengirim
        elif (fee > self.transaction_limit):
            # mengubah jumlah BenCoin yang ditransfer menjadi batas transaksi pengirim
            amount_of_BenCoin = self.transaction_limit
            receiver.balance += amount_of_BenCoin
            fee = amount_of_BenCoin + self.transaction_fee
            self.balance -= fee
            print('{} berhasil mentransfer {} BenCoin kepada {}'.format(self.name, amount_of_BenCoin, receiver.name))
            self.transaction.append('MENTRANSFER {} {}'.format(receiver.name, amount_of_BenCoin))
            receiver.transaction.append('DITRANSFER {} {}'.format(self.name, amount_of_BenCoin))

        # jika tidak bermasalah, maka masuk ke suite di else
        else:
            self.balance -= fee
            receiver.balance += amount_of_BenCoin
            print('{} berhasil mentransfer {} BenCoin kepada {}'.format(self.name, amount_of_BenCoin, receiver.name))
            self.transaction.append('MENTRANSFER {} {}'.format(receiver.name, amount_of_BenCoin))
            receiver.transaction.append('DITRANSFER {} {}'.format(self.name, amount_of_BenCoin))

    # meng-override fungsi print untuk mencetak info akun sesuai format
    def __str__(self):
        nm = ('Nama : {}'.format(self.name))
        acc_tp = 'Jenis Akun : {}'.format(self.account_type)
        svngs = 'Jumlah BenCoin : {}'.format(self.balance)
        trnsctn = 'Transaksi :\n{}'.format('\n'.join(self.transaction))
        return nm + '\n' + acc_tp + '\n' + svngs + '\n' + trnsctn

# membuat dictionary untuk menampung nasabah Pardede Finance
Pardede_clients = {}
# membuat dictionary untuk menampung mata uang dengan valuenya berupa rate mata uang
currencies = {}

# judul program
print('\n---------------\nPARDEDE FINANCE\n---------------')
while (True):
    command = input('\n>>> ').split()
    try:
        if (command[0].upper() == 'DAFTAR'):
            # membuat kondisi jika mendaftarkan nama yang sudah pernah terdaftar sebelumnya
            if (command[1].capitalize() in Pardede_clients):
                print('Akun {} sudah pernah terdaftar sebelumnya'.format(command[1].capitalize()))

            # membuat kondisi jika salah memasukkan tipe akun
            elif ((command[2].capitalize() != 'Pelajar') and (command[2].capitalize() != 'Reguler') and (command[2].capitalize() !='Bisnis') and (command[2].capitalize() !='Elite')):
                print('Tidak ada tipe akun berupa {}'.format(command[2].capitalize()))

            else:
                client_name = command[1].capitalize()
                accnt_type = command[2].capitalize()
                init_savings = 0
                init_transaction = []
                # menginstansiasi akun ke dalam class PardedeFinance
                account = PardedeFinance(client_name, accnt_type, init_savings, init_transaction)
                # memasukkan nasabah ke dalam dictionary nasabah Pardede Finance
                Pardede_clients[client_name] = account

        elif (command[0].upper() == 'SETOR'):
            # membuat kondisi jika akun nasabah belum pernah terdaftar sebelumnya
            if command[1].capitalize() not in Pardede_clients:
                print('Akun {} belum pernah terdaftar sebelumnya'.format(command[1].capitalize()))

            # membuat kondisi jika mata uang belum pernah terdaftar
            elif (command[3].upper() not in currencies):
                print('Mata uang {} tidak ada'.format(command[3].upper()))

            else:
                Pardede_clients[command[1].capitalize()].SETOR(int(command[2]), command[3].upper())

        elif (command[0].upper() == 'TARIK'):
            # membuat kondisi jika akun nasabah belum pernah terdaftar sebelumnya
            if (command[1].capitalize() not in Pardede_clients):
                print('Akun {} belum pernah terdaftar sebelumnya'.format(command[1].capitalize()))

            # membuat kondisi jika mata uang belum terdaftar
            elif (command[3].upper() not in currencies):
                print('Mata uang {} tidak ada'.format(command[3].upper()))

            else:
                Pardede_clients[command[1].capitalize()].TARIK(int(command[2]), command[3].upper())

        elif (command[0].upper() == 'TRANSFER'):
            # membuat kondisi jika akun nasabah pengirim belum pernah terdaftar sebelumnya
            if (command[1].capitalize() not in Pardede_clients):
                print('Akun {} belum pernah terdaftar sebelumnya'.format(command[1].capitalize()))

            # membuat kondisi jika akun nasabah penerima belum pernah terdaftar sebelumnya
            if (command[2].capitalize() not in Pardede_clients):
                print('Akun {} belum pernah terdaftar sebelumnya'.format(command[2].capitalize()))

            # membuat kondisi jika mentransfer ke diri sendiri
            elif (command[1].capitalize() == command[2].capitalize()):
                print('Tidak dapat mentransfer ke diri sendiri')

            else:
                Pardede_clients[command[1].capitalize()].TRANSFER(Pardede_clients[command[2].capitalize()], int(command[3]))

        elif (command[0].upper() == 'TAMBAH'):
            currencies[command[1].upper()] = int(command[2])
            print('Mata uang {} telah ditambahkan dengan rate {} per BenCoin'.format(command[1].upper(), command[2]))

        elif (command[0].upper() == 'UBAH'):
            # membuat kondisi jika mata uang belum pernah ditambahkan
            if (command[1].upper() not in currencies):
                print('Mata uang {} tidak ada'.format(command[1].upper()))

            else:
                currencies[command[1].upper()] = int(command[2])
                print('Rate mata uang {} berubah menjadi {} per BenCoin'.format(command[1].upper(), command[2]))

        elif (command[0].upper() == 'INFO'):
            # membuat kondisi jika akun nasabah belum pernah terdaftar sebelumnya
            if (command[1].capitalize() not in Pardede_clients):
                print('Akun {} belum pernah terdaftar sebelumnya'.format(command[1].capitalize()))

            else:
                print(Pardede_clients[command[1].capitalize()])

        # perintah tambahan, untuk keluar dari program
        elif (command[0].upper() == 'QUIT'):
            for name in Pardede_clients:
                print(Pardede_clients[name], '\n')
            print('---------------\nPROGRAM SELESAI\n---------------\n')
            exit()

        # membuat kondisi jika perintah yang dimasukkan tidak sesuai dengan yang tersedia
        else:
            print('Perintah yang Anda masukkan bukan perintah yang tersedia')

    # membuat kondisi jika input tidak sesuai format
    except IndexError:
        print('Input yang Anda masukkan tidak sesuai format')
