class Hewan:
    def suara(self):
        print("Hewan bersuara.")

class Kucing(Hewan):
    def suara(self):
        print("Meong!")

class Anjing(Hewan):
    def suara(self):
        print("Guk Guk!")

# Membuat objek dari kelas Kucing dan Anjing
kucing = Kucing()
anjing = Anjing()

# Memanggil metode suara
kucing.suara()
anjing.suara()
