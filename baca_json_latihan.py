import json
import os
import shutil

def load_data(file_path):
    # Pastikan file ada
    if not os.path.exists(file_path):
        print(f"❌ File tidak ditemukan: {file_path}")
        return None

    try:
        # Buka dan baca isi file JSON
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        print("❌ Format file JSON tidak valid.")
        return None
    
    if not isinstance(data, list):
        print("❌ Format JSON tidak sesuai (harus berupa list).")
        return None
    if data and isinstance(data[0], dict) and "Nama" in data[0] and "Alamat" in data[0]:    
        if "fullName" in data[0].values() or "address" in data[0].values():
            data = data[1:]
    return data 

def save_data(file_path, data):
    if os.path.exists(file_path):
        backup_path = file_path + ".bak"
        try:
            shutil.copyfile(file_path, backup_path)
        except Exception as e:
            print(f"❌ Gagal membuat backup file: {e}")
            return False

def tampilkan_data_json(file_path):
    # Pastikan file ada
    if not os.path.exists(file_path):
        print(f"❌ File tidak ditemukan: {file_path}") #HINT parameter
        return

    try:
        # Buka dan baca isi file JSON
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("❌ Format file JSON tidak valid.")
        return

    # Pastikan data berupa list
    if not isinstance(data, list):
        print("❌ Format JSON tidak sesuai (harus berupa list).")
        return

    # Lewati baris pertama jika merupakan header
    if data and isinstance(data[0], dict) and "Nama" in data[0] and "Alamat" in data[0]:
        if "fullName" in data[0].values() or "address" in data[0].values():
            data = data[1:] #HINT ambil data ke 1 sampai terakhir

    # Tampilkan data ke layar
    if not data:
        print("📭 Tidak ada data untuk ditampilkan.")
        return

    print(f"📋 Total data ditemukan: {len(data)}\n") #HINT jumlah data ditemukan

    for i, item in enumerate(data, start=1):
        print(f"Data ke-{i}:")
        print(f"Nama           : {item.get('Nama', '-')}")
        print(f"Alamat         : {item.get('Alamat', '-')}")
        print(f"NIK            : {item.get('NIK', '-')}")
        print(f"Mobile         : {item.get('Mobile', '-')}")
        print(f"Tanggal Lahir  : {item.get('Tanggal Lahir', '-')}")
        print("-" * 40)
        
def cari_data_by_nik(file_path):
    nik_cari = input("Masukkan NIK yang ingin dicari: ").strip()

    # Pastikan file ada
    if not os.path.exists(file_path):
        print(f"❌ File tidak ditemukan: {file_path}")
        return

    try:
        # Buka dan baca isi file JSON
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("❌ Format file JSON tidak valid.")
        return

    # Cari data berdasarkan NIK
    hasil_cari = [item for item in data if item.get("NIK") == nik_cari]

    if not hasil_cari:
        print(f"🔍 Data dengan NIK {nik_cari} tidak ditemukan.")
        return

    print(f"📋 Data ditemukan untuk NIK {nik_cari}:\n")
    for item in hasil_cari:
        print(f"Nama           : {item.get('Nama', '-')}")
        print(f"Alamat         : {item.get('Alamat', '-')}")
        print(f"NIK            : {item.get('NIK', '-')}")
        print(f"Mobile         : {item.get('Mobile', '-')}")
        print(f"Tanggal Lahir  : {item.get('Tanggal Lahir', '-')}")
        print("-" * 40)
# === Program utama ===
if __name__ == "__main__":
    file_path = input("Masukkan path file JSON (contoh: C:\\data\\pasien.json): ").strip()
   # tampilkan_data_json(file_path) #HINT variabel

    while True:
        print("\n====== MENU UTAMA ======")
        print("1. Tampilkan Seluruh Data")
        print("2. Cari Data Berdasarkan NIK")
        print("3. Exit")

        pilihan = input("Pilih Menu (1/2/3): ")

        if pilihan == "1":
            tampilkan_data_json(file_path)
        elif pilihan == "2":
            cari_data_by_nik(file_path)
        elif pilihan == "3":
            print("Program selesai. Terima kasih! 👋")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")
