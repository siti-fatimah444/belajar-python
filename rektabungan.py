class Rekening:
    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Setor berhasil. Saldo sekarang: Rp{self.saldo:,}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup.")
        else:
            self.saldo -= jumlah
            print(f"Tarik berhasil. Saldo sekarang: Rp{self.saldo:,}")

    def hitung_bunga(self, bunga):
        bunga_didapat = self.saldo * bunga
        self.saldo += bunga_didapat
        print(f"Bunga{bunga*100:.1f}% telah ditambahkan. Saldo sekarang: Rp{self.saldo:,}")

    def cek_saldo(self):
        print(f"Nomor Rekening: {self.no_rekening}")
        print(f"Nama Pemilik : {self.nama}")
        print(f"Saldo        : Rp{self.saldo:,}")

# ===== PROGRAM UTAMA =====
def main():
    rekening = None # belum ada rekening

    while True:
        print("\n===== MENU BANK =====")
        print("1. Buka Rekening")
        print("2. Setor Tabungan")
        print("3. Tarik Tabungan")
        print("4. Bunga")
        print("5. Cek Saldo")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            if rekening:
                print("Rekening sudah dibuat.")
            else:
                no_rek = input("Masukkan nomor rekening: ")
                nama = input("Masukkan nama pemilik: ")
                saldo_awal = float(input("Masukkan saldo awal: "))
                rekening = Rekening(no_rek, nama, saldo_awal)
                print("Rekening berhasil dibuat!")

        elif pilihan == "2":
            if rekening:
                jumlah = float(input("Masukkan jumlah setor: "))
                rekening.setor(jumlah)
            else:
                print("Belum ada rekening. Silahkan buka rekening dahulu.")

        elif pilihan == "3":
            if rekening:
                jumlah = float(input("Masukkan jumlah tarik: "))
                rekening.tarik(jumlah)
            else:
                print("Belum ada rekening. Silahkan buka rekening dahulu.")

        elif pilihan == "4":
            if rekening:
                bunga = float(input("Masukkan persen bunga (misal 0.05 untuk 5%): "))
                rekening.hitung_bunga(bunga)
            else:
                print("Belum ada rekening. Silahkan buka rekening dahulu.")

        elif pilihan == "5":
            if rekening:
                rekening.cek_saldo()
            else:
                print("Belum ada rekening. Silahkan buka rekening dahulu.")

        elif pilihan == "6":
            print("Terima kasih telah menggunakan layanan kami.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi")

# Jalankan program
if __name__ == "__main__":
    main()


