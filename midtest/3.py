class Laptop:
    def __init__(self, merk, ram, processor):
        self.merk = merk
        self.ram = ram
        self.processor = processor

    def __del__(self):
        print(f"Laptop {self.merk} telah dihapus dari memori.")

    def tampilkan_spesifikasi(self):
        print(f"Merk: {self.merk}")
        print(f"RAM: {self.ram} GB")
        print(f"Processor: {self.processor}")

# Membuat objek dari kelas Laptop
laptop = Laptop("Asus", 16, "Intel i7")
laptop.tampilkan_spesifikasi()

# Menghapus objek secara manual (contoh destructor)
del laptop
