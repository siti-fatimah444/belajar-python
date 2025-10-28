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