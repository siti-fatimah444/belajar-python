# data tipe

# tipe data string/teks
nama = "aji" # tipe data string/teks
print(type(nama)) 


# tipe data int (bil bulat)
umur = 23 # tipe data int
print(type(umur))

tinggi_badan = 179.5 # tipe data float (bil desimal)
print(type(tinggi_badan))

# bolean (true/false)
suka_python = True
print(type(suka_python))

# sequences = urutan

# tipe data list = daftar pakai [
nama_siswa = [] # list kosong
nama_siswa = ["aji", "farhan", "hery", 12, 5.5, True]
print(type(nama_siswa))
print(nama_siswa [0]) # ini indexing urutan 0


# tuple data tipe = ()
nama_hari = ("senin", "selasa", "rabu")
print(type(nama_hari))
print(nama_hari[0]) # ini index 0 ('senin')

# range (rentang)
angka = range (1, 10, 2) # star, stop, step
angka = range (10) # star = 0, stop, step = 1

# set = himpunan {
hobi_siswa = {"mancing", "baca"}
print(type(hobi_siswa))
print(hobi_siswa) 


# dictionary, key:value
kontak_telp = {"aji":889, "farhan":887, "hery":886}
print(type(kontak_telp))


# string
nama = "aji"
print("nama saya adalah", nama)
teks = "aji ya suka belajar python programming"

# akses huruf tertentu menggunakan index
print(teks[0]) # index awal

# string slicing/memotong
print(teks[0:8]) # start:stop(batas atas)
print(teks[4:]) # start - selesai


# string format
nama = "aji"
hobi = "main ps"

print("hallo nama saya", "aji")
print("hobi saya: ", hobi)

# format (f"") {variable}
print(f"nama saya {nama} hobi saya {hobi}")


# input
nama = input("masukkan nama kamu: ")
usia = int(input("masukkan usia kamu: "))
hobi = input("apa hobi kamu: ")

# \n new line
print(f"data diri\nnama: {nama}\nusia:{usia}\nhobi:{hobi}")


# control flow
# aritmatika
a = 10
b = 8 
print(a + b) # operator tambah (+)
print(a - b) # operator kurang (-)
print(a / b) # operator bagi (/)
print(a * b) # operator kali (*)
print(a ** b) # operator pangkat (**)
print(a % b) # operator sisa hasil bagi/modulus (%)

phi = 3.14
r = 7
luas_lingkaran = phi * (r ** 2)
print(luas_lingkaran)

# operator comparison
print(a > b) # true
print(a < b) # False
print(a >= b) # true
print(a <= b) # false
print(a == b) # false
print(a != b) # true


# logical operator (and , or , not)
print(a > b and a >= b) # true and true
print(a > b and a < b) # true and false
print(a > b or a < b) # true atau false
print(not(a > b and a >= b)) # ini akan false






