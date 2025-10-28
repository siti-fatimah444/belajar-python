# list [] => data terstruktur di mulai index dari 0

list_siswa = [] # list kosong

# method untuk menambah data ke dalam list
# append ()

list_siswa.append ("farhan")
print(list_siswa)
list_siswa.append ("aji")
list_siswa.append ("heri")
print(list_siswa)

# insert () => spesifik index
list_siswa.insert(0, "ario")
print(list_siswa)

list_siswa.append ("farhan")
print(list_siswa)

# method untuk menghapus data dalam list
# remove ()
list_siswa.remove("farhan") # case sensitive
print(list_siswa)

# pop ()
list_siswa.pop(0) # harus tahu posisi data
print(list_siswa)

# cara akses elemen di lis
# indexing => index dari 0

print("data list: ", list_siswa)
print("data pertama: ", list_siswa [0]) # ini ambil dari posisi awal

# list slicing (memotong list)
print(list_siswa[0:2])

# set {} => himpunan

set_siswa = {'aji', 'heri', 'farhan'} # ini set kosong
print(set_siswa)

# method menambah data ke dalam set {}
# add ()

set_siswa.add("budi")
print(set_siswa)

# method menghapus data dalam set{}
set_siswa.remove("aji") # case sensitive
print(set_siswa)

# discard ()
set_siswa.discard("farhan")
print(set_siswa)

# irisan (intersection), gabungan(join), selisih
set_siswa_a = {"aji", "farhan", "heri"}
set_siswa_b = {"aji", "farhan", "ario"}

#irisan (&)
print("irisan: ", set_siswa_a & set_siswa_b)

# gabungan (|)
print("join: ", set_siswa_a | set_siswa_b)

# selisih (-)
print("selisih: ", set_siswa_a - set_siswa_b)

# dictionary => kamus, key:value

kontak_tlp = { 
    #key:value
    "aji":889,
    "farhan":887,
    "heri":886
}
print(kontak_tlp)

# indexing []
print(kontak_tlp["farhan"]) # indexing akses dictionary

# nambah data 
kontak_tlp["ario"] = 888
print(kontak_tlp)

# ubah value 
kontak_tlp["aji"] = 998
print(kontak_tlp)

# hapus data
kontak_tlp.pop("ario")
print(kontak_tlp)

# del 
del kontak_tlp["aji"]
print(kontak_tlp)

# keys () => kunci
print(kontak_tlp.keys())

# values () => nilai
print(kontak_tlp.values())

# items () => key:value
print(kontak_tlp.items())

# nested dictionary => dict bersarang
karyawan = {
    "karyawan1":{
        "nama": "ario", 
        "ttl": 2002
    }, 
    "karyawan2":{
        "nama": "farhan",
        "ttl": 2000
    }
}
print(karyawan['karyawan1']['nama']) #akses



# function => blok kode terorganisir

# contoh function
def tambah(angka1, angka2):
    return angka1 + angka2

tambah(12, 2)

# sintax/cara menulis
'''
def nama_function(nama_parameter1, nama_parameter2):
    #blok kode function

#panggil function
nama_function(isi_parameter)
'''

# 1. function tanpa parameter
def sapa():
    print("halo teman-teman semua")

# panggil function
sapa()

# 2. function dengan parameter
def sapa(nama):
    print(f"halo nama saya {nama}")

# panggil function
sapa("farhan")

# 3. function dengan return value/nilai kembali
def kali(a, b):
    return a * b

a = 5
b = 2
hasil = kali(a, b)
print(hasil)

# 4. function dengan default parameter
def sapa(nama, lokasi = "indonesia"):
    print(f"halo saya {nama}, sekarang di {lokasi}")

sapa("farhan")
sapa("aji", "german")

# looping
# for loop
for i in range(1, 11): # start, stop, step
    print(i)

# while loop
i = 1

while i <= 10:
    print(i)
    # increment
    i += 1 # i = i + 1
    
# cetak bil genap 1 - 20
for i in range(2, 21, 2):
    print("bil genap: ", i)

# timer 7 second
timer = 7

while timer > 0:
    print(timer)
    timer -= 1 # timer = timer - 1
print("lariii")

# tabel perkalian 5
for i in range(1, 11):
    print(f"5 x {i} = {i * 5}")
    