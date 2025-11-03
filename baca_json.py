import json
import os
import shutil

def load_data(file_path):
    
    if not os.path.exists(file_path):
        print(f"File tidak ditemukan: {file_path}")
        return None
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Format file JSON tidak valid.")
        return None
    if not isinstance(data, list):
        print("Format JSON tidak sesuai (harus berupa list).")
        return None
    
    if data and isinstance(data[0], dict) and "Nama" in data[0] and "Alamat" in data[0]:
        if "fullName" in data [0].values() or "address" in data[0].values():
            data = data[1:]
    
    return data

def save_data(file_path, data):
    
    if os.path.exists(file_path):
        backup_path = file_path + ".bak"
        try:
            shutil.copyfile(file_path, backup_path)
        except Exception as e:
            print(f"Gagal membuat backup: {e}")
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            return True
    except Exception as e:
        print(f"Gagal menyimpan file: {e}")
        return False
    
def tampilkan_data_json(file_path):
    data = load_data(file_path)
    if data is None:
        return
    
    if not data:
        print("Tidak ada data untuk ditampilkan.")
        return
    
    print(f"\nTotal data ditemukan: {len(data)}\n")
    for i, item in enumerate(data, start=1):
        print(f"Data ke-{i}:")
        print(f"Nama    : {item.get('Nama', '-')}")
        print(f"Alamat  : {item.get('Alamat', '-')}")
        print(f"NIK     : {item.get('NIK', '-')}")
        print(f"Mobile  : {item.get('Mobile', '-')}")
        print(f"Tanggal Lahir : {item.get('Tanggal Lahir', '-')}")
        print("-" * 40)

def cari_data_by_nik(file_path):
    nik_cari = input("Masukkan NIK yang ingin dicari: ").strip()
    if not nik_cari:
        print("NIK kosong, silahkan coba lagi.")
        return
    
    data = load_data(file_path)
    if data is None:
        return
    
    hasil_cari = [item for item in data if str(item.get("NIK")) == nik_cari]

    if not hasil_cari:
        print(f"Data di temukan untuk NIK {nik_cari} tidak di temukan.")
        return
    
    print(f"\n Data ditemukan untuk NIK {nik_cari}:\n")
    for item in hasil_cari:
        print(f"Nama    : {item.get('Nama', '-')}")
        print(f"Alamat  : {item.get('Alamat', '-')}")
        print(f"NIK     : {item.get('NIK', '-')}")
        print(f"Mobile  : {item.get('Mobile', '-')}")
        print(f"Tanggal Lahir : {item.get('Tanggal Lahir', '-')}")
        print("-" * 40)

def tambah_data(file_path):

    data = load_data(file_path)
    if data is None:
        return
    
    print("\n===== Tambah Data Baru =====")
    nama = input("Masukkan Nama         : ").strip()
    alamat = input("Masukkan Alamat       : ").strip()
    nik = input("Masukkan NIK          : ").strip()
    mobile = input("Masukkan Mobile       : ").strip()
    tgl = input("Masukkan Tanggal Lahir: ").strip()

    if not nik:
        print("NIK tidak boleh kosong.")
        return
    
    exist = any(str(item.get("NIK")) == nik for item in data)
    if exist:
        print("NIK sudah terdaftar. Gunakan NIK lain atau hapus data lama terlebih dahulu.")
        return
    
    new_item = {
        "Nama": nama or "-",
        "Alamat": alamat or "-",
        "NIK": nik or "-",
        "Mobile": mobile or "-",
        "Tanggal Lahir": tgl or "-"
    }

    data.append(new_item)
    if save_data(file_path, data):
        print("Data berhasil ditambahkan dan disimpan.")
    else:
        print("Terjadi kesalahan saat menyimpan data.")

def hapus_data_by_nik(file_path):
    nik_hapus = input("Masukkan NIK yang ingin dihapus: ").strip()
    if not nik_hapus:
        print("NIK kosong.")
        return
    
    data = load_data(file_path)
    if data is None:
        return
    
    matches = [item for item in data if str(item.get("NIK")) == nik_hapus]
    if not matches:
        print(f"Tidak ditemukan data dengan NIK {nik_hapus}.")
        return
    
    print(f"\nDitemukan {len(matches)} record dengan NIK {nik_hapus}:")
    for i, item in enumerate(matches, start=1):
        print(f"[{i}] Nama: {item.get('Nama', '-')}, Alamat: {item.get('Alamat', '-')}")
    
    confirm = input("Yakin ingin menghapus data ini? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Penghapusan dibatalkan.")
        return
    
    new_data = [item for item in data if str(item.get("NIK")) != nik_hapus]

    if save_data(file_path, new_data):
        print(f"Data dengan NIK {nik_hapus} berhasil dihapus.")
    else:
        print("Gagal menyimpan perubahan setelah dihapus.")

if __name__ == "__main__":
    file_path = input("Masukkan path file JSON (contoh: C:\\data\\pasien.json): ").strip()

    while True:
        print("\n====== MENU UTAMA ======")
        print("1. Tampilkan Seluruh Data")
        print("2. Cari Data Berdasarkan NIK")
        print("3. Tambah Data Baru")
        print("4. Hapus Data Berdasarkan NIK")
        print("5. Exit")

        pilihan = input("Pilih Menu (1/2/3/4/5): ").strip()

        if pilihan == "1":
            tampilkan_data_json(file_path)
        elif pilihan == "2":
            cari_data_by_nik(file_path)
        elif pilihan == "3":
            tambah_data(file_path)
        elif pilihan == "4":
            hapus_data_by_nik(file_path)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silahkan coba lagi.")


    
              

    