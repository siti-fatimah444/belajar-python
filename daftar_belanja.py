# ===== LATIHAN PROGRAM DAFTAR BELANJA =====

daftar_belanja = []

def tambah_barang():
    barang = input("Masukkan nama barang yang ingin ditambahkan:")

    daftar_belanja.append(barang)
    print(f"✅ '{barang}' telah ditambahkan ke daftar belanja.\n")

def tampilkan_barang():
    if daftar_belanja:
        print(" Daftar belanja masih kosong.\n")
        return
    
    print("\n Daftar Belanja:")

    for i, barang in enumerate(daftar_belanja, start=1):
        print(f"{i}. {barang}")
    print()

def hapus_barang():
    tampilkan_barang()
    
    if not daftar_belanja:
        return
    
    barang = input("Masukkan nama barang yang ingin dihapus: ")
    if barang in daftar_belanja:
        daftar_belanja.remove(barang)
        print(f"✅ '{barang}' telah dihapus dari daftar belanja.\n")
    else:
        print(f"❌ '{barang}' tidak ditemukan dalam daftar belanja.\n")

# ===== PROGRAM UTAMA =====
while True:
    print("===== MENU DAFTAR BELANJA =====")
    print("1. Tambah Barang")
    print("2. Tampilkan Daftar Belanja")
    print("3. Hapus Barang")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        tampilkan_barang()
    elif pilihan == "3":
        hapus_barang()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program daftar belanja!")
        break
    else:
        print("Pilihan tidak valid. Silahkan coba lagi.\n")