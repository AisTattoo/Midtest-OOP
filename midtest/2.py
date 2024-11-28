class Mahasiswa:
    def __init__(self, nama, nim, program_studi):
        self.nama = nama
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Program Studi: {self.program_studi}")

# Membuat objek dari kelas Mahasiswa
nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
program_studi = input("Masukkan Program Studi: ")

mahasiswa = Mahasiswa(nama, nim, program_studi)
mahasiswa.tampilkan_data()
