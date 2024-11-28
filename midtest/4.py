class AkunBank:
    def __init__(self, nomor_rekening, saldo):
        self.__nomor_rekening = nomor_rekening
        self.__saldo = saldo

    # Getter untuk saldo
    def get_saldo(self):
        return self.__saldo

    # Setter untuk saldo
    def set_saldo(self, saldo_baru):
        self.__saldo = saldo_baru

    # Metode untuk menambah saldo
    def tambah_saldo(self, jumlah):
        self.__saldo += jumlah
        print(f"Saldo berhasil ditambah. Saldo saat ini: {self.__saldo}")

    # Metode untuk menarik saldo
    def tarik_saldo(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Saldo berhasil ditarik. Saldo saat ini: {self.__saldo}")
        else:
            print("Saldo tidak mencukupi.")

# Membuat objek AkunBank
akun = AkunBank("123456789", 1000000)
akun.tambah_saldo(500000)
akun.tarik_saldo(300000)
print(f"Saldo akhir: {akun.get_saldo()}")
