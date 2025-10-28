# data tipe

# tipe data string/teks
nama = "aji" # tipe data string/teks
print(type(nama))

# tipe data int(bil bulat)
umur = 23 # tipe data int
print(type(umur))

# bolean (true/false)
suka_python = True
print(type(suka_python))

# tipe data sequences = urutan

# tipe data list = daftar => []
nama_siswa = [] # list kosong
nama_siswa = ["aji", "farhan", "heri", 12, 5.5, True]
print(type(nama_siswa))
print(nama_siswa[0]) # ini indexing => urutan 0

# tuple data tipe = ()
nama_hari = ("senin", "selasa", "rabu")
print(type(nama_hari))
print(nama_hari[0]) # ini index 0 ('senin')

# range (rentang)
angka = range(1, 10, 2) # start, stop, step
angka = range(10) # start = 0, stop, step = 1

# set = himpunan {}
hobi_siswa = {"mancing", "main game", "berenang", "bernyanyi"}
print(type(hobi_siswa))
print(hobi_siswa)

# dictionary => key:value
kontak_telepon = {
    "aji":880,
    "farhan":850,
    "heri":830
}
print(type(kontak_telepon))



