def hitung_rata_rata(nilai1, nilai2, nilai3):
    rata_rata = (nilai1 + nilai2 + nilai3) / 3
    return rata_rata

def tentukan_kategori(rata):
    if rata >= 90:
        kategori = "A"
    elif rata >= 80:
        kategori = "B"
    elif rata >= 70:
        kategori = "C"
    elif rata >= 60:
        kategori = "D"
    else:
        kategori = "E"
    return kategori

print("=== Sistem Penilaian Sederhana ===")

nama = input("Masukkan nama siswa: ")

nilai1 = float(input("Masukkan nilai mata pelajaran 1: "))
nilai2 = float(input("Masukkan nilai mata pelajaran 2: "))          
nilai3 = float(input("Masukkan nilai mata pelajaran 3: "))  

rata = hitung_rata_rata(nilai1, nilai2, nilai3)

kategori = tentukan_kategori(rata)

print("\n ===== Hasil Penilaian =====")
print("Nama:", nama)
print("Rata-rata nilai:", rata)
print("Kategori nilai:", kategori)

    
     