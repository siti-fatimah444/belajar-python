# buble sort function
def bubble_sort(arr):
    # mulai
    panjang_list = len(arr) # ambil pjg list/arr
    # lakukan looping sepanjang array/list
    for i in range(0, panjang_list - 1):
        # lakukan looping dalam list/array untuk membandingkan data
        for j in range(0, panjang_list - i - 1):
            # cek apakah data bersebelahan sudah sesuai atau belum
            if arr[j] > arr[j + 1]:
                # swap/tuker data yang belum sesuai
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr 

# cara penggunaan
data_gaji = [1000, 3400, 2000, 6000, 900, 600]
hasil_data_urut = bubble_sort(data_gaji)

print("data gaji sebelum di sorting: ", data_gaji)
print("data gaji setelah di bubble sort: ", hasil_data_urut)

# sistem pengelolaan nilai siswa

"""
menu utama yang harus ada
1. tampilkan daftar nilai
2. urutkan berdasarkan nilai (bubble sort)
3. urutkan berdasarkan nama (bubble sort)
4. tambah nilai siswa
5. keluar
"""

# data nilai siswa

siswa = [
    {"nama": "farhan", "nilai":88}, # dictionary dalam list 
    {"nama": "aji", "nilai":75},
    {"nama": "heri", "nilai":92},
    {"nama": "ario", "nilai":60},
    {"nama": "budi", "nilai":80},
]

# function tampilkan daftar nilai
def tampilkan_nilai(siswa):
    print("\ndaftar nilai siswa:")
    for s in siswa:
        print(f"- {s['nama']}: {s['nilai']}")

# bubble sort by nilai

def bubble_sort_by_nilai(siswa):
    n = len(siswa)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if siswa[j]['nilai'] > siswa[j + 1]['nilai']:    
                siswa[j], siswa[j + 1] = siswa[j + 1], siswa[j]   
    return siswa


# bubble sort by nama

def bubble_sort_by_nama(siswa):
    n = len(siswa)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if siswa[j]['nama'] > siswa[j + 1]['nama']:
                siswa[j], siswa[j + 1] = siswa[j + 1], siswa[j]
    return siswa

# menu utama
def main():

    while True:
        print("\n=== menu pengelolaan nilai siswa ===")
        print("1. tampilkan daftar nilai")
        print("2. urutkan berdasarkan nilai")
        print("3. urutkan berdasarkan nama")
        print("4. tambah nilai siswa")
        print("5. keluar")
        pilihan = input("pilih menu (1 - 5): ")

        if pilihan == "1":
            tampilkan_nilai(siswa)
        elif pilihan == "2":
            hasil = bubble_sort_by_nilai(siswa)
            tampilkan_nilai(hasil)
        elif pilihan == "3":
            hasil = bubble_sort_by_nama(siswa)
            tampilkan_nilai(hasil)
        elif pilihan == "4":
            nama = input("masukan nama siswa: ")
            nilai = int(input("masukan nama siswa: "))
            siswa.append({"nama": nama, "nilai":nilai})
            print("data berhasil ditambahkan")
        elif pilihan == "5":
            print("terima kasih, program selesai")
            break
        else:
            print("pilihan tidak valid")


main()

