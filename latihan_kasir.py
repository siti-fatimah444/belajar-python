daftar_belanja = []

while True:
    print("===== MENU DAFTAR BELANJA =====")
    print("1. Tambah Barang")
    print("2. Tampilkan Daftar Belanja")
    print("3. Hapus Barang")
    print("4. Pembayaran & Cetar Struk")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        barang = input("Masukkan nama barang yang ingin ditambahkan:")
        daftar_belanja.append(barang)
        print(f"✅ '{barang}' telah ditambahkan ke daftar belanja.\n")
    elif pilihan == "2":
        if not daftar_belanja:
            print(" Daftar belanja masih kosong.\n")
        else:
            print("\n Daftar Belanja:")
            for i, barang in enumerate(daftar_belanja, start=1):
                print(f"{i}. {barang}")
            print()
    elif pilihan == "3":
        if not daftar_belanja:
            print(" Daftar belanja masih kosong.\n")
        else:
            barang = input("Masukkan nama barang yang ingin dihapus: ")
            if barang in daftar_belanja:
                daftar_belanja.remove(barang)
                print(f"✅ '{barang}' telah dihapus dari daftar belanja.\n")
            else:
                print(f"❌ '{barang}' tidak ditemukan dalam daftar belanja.\n")
    elif pilihan == "4":
        if not daftar_belanja:
            print(" Daftar belanja masih kosong. Tidak ada yang bisa dibayar.\n")
        else:
            total_barang = len(daftar_belanja)
            print("\n===== STRUK BELANJA =====")
            for i, barang in enumerate(daftar_belanja, start=1):
                print(f"{i}. {barang}")
            print(f"\nTotal Barang: {total_barang}")
            print("Terima kasih telah berbelanja!\n")
            daftar_belanja.clear()  # Kosongkan daftar setelah pembayaran
    elif pilihan == "5":
        print("Terima kasih telah menggunakan program daftar belanja!")
        break
    else:
        print("Pilihan tidak valid. Silahkan coba lagi.\n")

    