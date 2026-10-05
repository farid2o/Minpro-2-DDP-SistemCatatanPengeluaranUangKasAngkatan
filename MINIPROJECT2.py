import os
import pwinput
from datetime import datetime

data_user = {
    "admin" : {"password": "admin123", "role": "admin"},
    "anggota" : {"password": "anggota123", "role": "user"},
}

data_pengeluaran = {
    1: {"keperluan": "sewa sound system", "pj": "budi", "nominal": 500000, "tanggal": "01-09-2026"},
    2: {"keperluan": "sewa tenda", "pj": "andi", "nominal": 300000, "tanggal": "02-09-2026"}
}

def bersihkan_layar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def tekan_enter():
    input("\nTekan Enter untuk melanjutkan...")

def tampilkan_data():
    print("\n=== DATA PENGELUARAN ===")
    if len(data_pengeluaran) == 0:
        print("Belum ada data pengeluaran.")
    else:
        print(f"{'ID':<4} | {'Tanggal':<10} | {'Keperluan / Barang':<25} | {'PJ':<12} | {'Nominal (Rp)':<12}")
        print("-" * 76)
        for id_data in data_pengeluaran:
            data = data_pengeluaran[id_data]
            print(f"{id_data:<4} | {data['tanggal']:<10} | {data['keperluan']:<25} | {data['pj']:<12} | Rp{data['nominal']:,.0f}")

def tambah_data():
    print("\n--- TAMBAH CATATAN PENGELUARAN BARU ---")
    keperluan = input("Masukkan keperluan/barang: ").strip()
    pj = input("Masukkan penanggung jawab (PJ): ").strip()

    if keperluan == "" or pj == "":
        print("\n[GAGAL] Keperluan dan PJ tidak boleh kosong!")
        return

    try:
        nominal = int(input("Masukkan nominal pengeluaran (Rp): ").strip())
    except ValueError:
        print("\n[GAGAL] Nominal pengeluaran harus berupa angka!")
        return

    if nominal <= 0:
        print("\n[GAGAL] Nominal pengeluaran harus lebih dari 0!")
        return

    id_baru = 1
    for id_data in data_pengeluaran:
        if id_data >= id_baru:
            id_baru = id_data + 1

    tanggal = datetime.now().strftime("%d-%m-%Y")
    data_pengeluaran[id_baru] = {
        "keperluan": keperluan,
        "pj": pj,
        "nominal": nominal,
        "tanggal": tanggal,
    }
    print("\n[BERHASIL] Catatan pengeluaran berhasil ditambahkan.")

def ubah_data():
    print("\n--- UBAH DATA PENGELUARAN ---")
    if len(data_pengeluaran) == 0:
        print("[INFO] Tidak ada data pengeluaran untuk diubah.")
        return

    tampilkan_data()

    try:
        id_ubah = int(input("\nMasukkan ID data yang ingin diubah: ").strip())
    except ValueError:
        print("\n[GAGAL] ID harus berupa angka!")
        return

    if id_ubah not in data_pengeluaran:
        print("\n[GAGAL] ID data tidak ditemukan!")
        return

    print("\n--- MASUKKAN DATA PEMBARUAN ---")
    keperluan_baru = input("Masukkan keperluan/barang baru: ").strip()
    pj_baru = input("Masukkan PJ baru: ").strip()

    if keperluan_baru == "" or pj_baru == "":
        print("\n[GAGAL] Keperluan dan PJ tidak boleh kosong!")
        return

    try:
        nominal_baru = int(input("Masukkan nominal pengeluaran baru (Rp): ").strip())
    except ValueError:
        print("\n[GAGAL] Nominal pengeluaran harus berupa angka!")
        return

    if nominal_baru <= 0:
        print("\n[GAGAL] Nominal pengeluaran harus lebih dari 0!")
        return

    data_pengeluaran[id_ubah]["keperluan"] = keperluan_baru
    data_pengeluaran[id_ubah]["pj"] = pj_baru
    data_pengeluaran[id_ubah]["nominal"] = nominal_baru
    print("\n[BERHASIL] Data pengeluaran berhasil diubah.")

def hapus_data():
    print("\n--- HAPUS DATA PENGELUARAN ---")
    if len(data_pengeluaran) == 0:
        print("[INFO] Tidak ada data pengeluaran untuk dihapus.")
        return

    tampilkan_data()

    try:
        id_hapus = int(input("\nMasukkan ID data yang ingin dihapus: ").strip())
    except ValueError:
        print("\n[GAGAL] ID harus berupa angka!")
        return

    if id_hapus not in data_pengeluaran:
        print("\n[GAGAL] ID data tidak ditemukan!")
        return

    nama = data_pengeluaran[id_hapus]["keperluan"]
    konfirmasi = input(f"Yakin ingin menghapus '{nama}'? (y/n): ").strip().lower()

    if konfirmasi == "y":
        del data_pengeluaran[id_hapus]
        print(f"\n[BERHASIL] Data pengeluaran '{nama}' berhasil dihapus.")
    else:
        print("\n[INFO] Penghapusan data dibatalkan.")

def hitung_total():
    print("\n--- TOTAL PENGELUARAN UANG KAS ---")
    if len(data_pengeluaran) == 0:
        print("[INFO] Tidak ada data pengeluaran untuk dihitung.")
    else:
        total = 0
        for id_data in data_pengeluaran:
            total = total + data_pengeluaran[id_data]["nominal"]

        print(f"Total transaksi pengeluaran  : {len(data_pengeluaran)} Transaksi")
        print(f"Total pengeluaran uang kas   : Rp{total:,.0f}")

def login():
    kesempatan = 3
    print("\n--- LOGIN ---")

    while kesempatan > 0:
        username = input("Username : ").strip()
        password = pwinput.pwinput("Password : ", mask="*").strip()

        if username == "" or password == "":
            print("\n[GAGAL] Username dan password tidak boleh kosong!\n")
        elif username in data_user and password == data_user[username]["password"]:
            waktu = datetime.now().strftime("%d-%m-%Y %H:%M")
            print(f"\n[BERHASIL] Login berhasil pada {waktu}. Selamat datang, {username}!")
            return username
        else:
            kesempatan = kesempatan - 1
            print(f"\n[GAGAL] Username atau password salah! Sisa kesempatan: {kesempatan}\n")

    print("[GAGAL] Kesempatan login habis. Kembali ke menu awal.")
    return ""

def menu_admin(username):
    while True:
        bersihkan_layar()
        print("=" * 48)
        print("SISTEM CATATAN PENGELUARAN UANG KAS ANGKATAN")
        print(f"MENU ADMIN - Login sebagai: {username}")
        print("=" * 48)
        print("1. Tampilkan seluruh catatan pengeluaran")
        print("2. Tambah catatan pengeluaran baru")
        print("3. Ubah data pengeluaran")
        print("4. Hapus data pengeluaran")
        print("5. Hitung total pengeluaran uang kas")
        print("6. Logout")
        print("=" * 48)
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            hitung_total()
        elif pilihan == "6":
            print("\nLogout berhasil. Kembali ke menu awal.")
            tekan_enter()
            break
        else:
            print("\n[GAGAL] Pilihan menu tidak valid! Silakan pilih menu antara 1-6.")

        tekan_enter()

def menu_user(username):
    while True:
        bersihkan_layar()
        print("=" * 48)
        print("SISTEM CATATAN PENGELUARAN UANG KAS ANGKATAN")
        print(f"MENU USER - Login sebagai: {username}")
        print("=" * 48)
        print("1. Tampilkan seluruh catatan pengeluaran")
        print("2. Hitung total pengeluaran uang kas")
        print("3. Logout")
        print("=" * 48)
        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            hitung_total()
        elif pilihan == "3":
            print("\nLogout berhasil. Kembali ke menu awal.")
            tekan_enter()
            break
        else:
            print("\n[GAGAL] Pilihan menu tidak valid! Silakan pilih menu antara 1-3.")

        tekan_enter()

while True:
    bersihkan_layar()
    print("=" * 48)
    print("SISTEM CATATAN PENGELUARAN UANG KAS ANGKATAN")
    print("=" * 48)
    print("1. Login")
    print("2. Keluar")
    print("=" * 48)
    pilihan = input("Pilih menu (1-2): ").strip()

    if pilihan == "1":
        username = login()
        tekan_enter()

        if username != "":
            role = data_user[username]["role"]
            if role == "admin":
                menu_admin(username)
            elif role == "user":
                menu_user(username)

    elif pilihan == "2":
        print("\nTerima kasih telah menggunakan sistem catatan pengeluaran uang kas.")
        break

    else:
        print("\n[GAGAL] Pilihan menu tidak valid! Silakan pilih menu antara 1-2.")
        tekan_enter()