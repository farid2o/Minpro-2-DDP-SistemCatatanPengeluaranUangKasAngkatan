<div align="center">
  <h1>💰Sistem Catatan Pengeluaran Uang Kas Angkatan</h1>
  <p>Program Python berbasis terminal (CLI) untuk mencatat pengeluaran uang kas angkatan. Ini adalah Mini Project 2 mata kuliah Dasar-Dasar Pemrograman (DDP), lanjutan dari Mini Project 1 dengan tambahan sistem login dan pembagian hak akses berdasarkan role.</p>
</div>

<div align="center">
  
[![NIM](https://img.shields.io/badge/NIM-2609116003-blue?style=for-the-badge&logo=academic-cap)](https://github.com)
[![KELAS](https://img.shields.io/badge/KELAS-A'26-orange?style=for-the-badge)](https://github.com)

---

| 👨‍💻 **Informasi Pengembang** | |
| :--- | :--- |
| **Nama Lengkap** | : Awang Farid Al Buhari |
| **NIM** | : 2609116003 |
| **Kelas** | : A |
| **Mata Kuliah** | : Dasar-Dasar Pemrograman |
| **Program Studi** | : Sistem Informasi |

---

</div>



## ✨ Fitur Utama

- 🔐 **Sistem Login Aman:** Autentikasi akun menggunakan masking password (`*`) dengan batas percobaan maksimal 3 kali.
- 👥 **Multi-Role Access:** Membedakan hak akses pengguna antara **Admin** dan **User / Anggota**.
- 📋 **Manajemen Data Pengeluaran (CRUD):**
  - **Create:** Menambah catatan pengeluaran baru dengan tanggal otomatis dari sistem.
  - **Read:** Menampilkan tabel catatan pengeluaran dalam format yang rapi.
  - **Update:** Memperbarui data transaksi yang sudah ada.
  - **Delete:** Menghapus data transaksi dengan konfirmasi konfirmasi keamanan (`y/n`).
- 📊 **Perhitungan Kas Otomatis:** Mengkalkulasi total nominal pengeluaran dan jumlah transaksi kas secara instan.
- 🛡️ **Validasi & Error Handling:** Pencegahan *error/crash* saat input tidak sesuai format (misal: input teks pada kolom angka).

## 🔐 Hak Akses Role

| Fitur / Menu | Admin | User (Anggota) |
| :--- | :---: | :---: |
| Tampilkan seluruh catatan pengeluaran | ✅ | ✅ |
| Hitung total pengeluaran uang kas | ✅ | ✅ |
| Tambah catatan pengeluaran baru | ✅ | ❌ |
| Ubah data pengeluaran | ✅ | ❌ |
| Hapus data pengeluaran | ✅ | ❌ |
| Logout | ✅ | ✅ |

> [!NOTE]
> **Admin** memiliki hak akses penuh (**CRUD lengkap**), sedangkan **User** hanya memiliki akses membaca (*Read Only*) dan menghitung statistik kas.


## 🔑 Akun Demo untuk Pengujian

Gunakan kredensial berikut untuk menguji coba fitur dalam program:

| Username | Password | Role | Hak Akses |
| :--- | :--- | :---: | :--- |
| `admin` | `admin123` | **Admin** | Akses Penuh (CRUD + Total) |
| `anggota` | `anggota123` | **User** | Akses Terbatas (Lihat + Total) |

---
## Yang diterapkan

- Dictionary untuk data akun ```(data_user)``` dan data pengeluaran ```(data_pengeluaran)```
- Function untuk setiap fitur, seperti ```login()```, ```tambah_data()```, dan ```menu_admin()```
- Validasi input dengan conditional statement ```(if / elif / else)```
- Error handling dengan ```try-except``` supaya input yang salah tidak membuat program berhenti
- Library: ```pwinput``` (input password), ```os``` (bersihkan layar), ```datetime``` (tanggal dan waktu)


## 🚀 Cara Menjalankan Program

### 1. Instal library ```pwinput```

```bash
pip install pwinput
```

### 2. Eksekusi Program
```bash
python MINIPROJECT2.py
```

## Flowchart

<img width="2008" height="1594" alt="minpro2 ddp fixx drawio" src="https://github.com/user-attachments/assets/30c5c0fd-05bb-4633-a833-2cac1bd5d38e" />

## Screenshot Output

### Menu Awal
<img width="548" height="196" alt="Screenshot 2026-10-05 144308" src="https://github.com/user-attachments/assets/cb3565fc-177c-42d4-b32c-403fe4e3aaa3" />

### Pilihan menu awal tidak valid
<img width="722" height="147" alt="Screenshot 2026-10-05 153700" src="https://github.com/user-attachments/assets/d9012163-861c-4ee8-8712-28ee7f1a4960" />

### Login berhasil sebagai admin
<img width="808" height="230" alt="Screenshot 2026-10-05 144341" src="https://github.com/user-attachments/assets/24d3b6bb-e92c-4a5f-8e17-26854c04bb9a" />

### Login berhasil sebagai user
<img width="845" height="197" alt="Screenshot 2026-10-05 144936" src="https://github.com/user-attachments/assets/bf28cf69-caba-4839-997e-e65cbcf97773" />

### Login gagal (username atau password salah)
<img width="657" height="198" alt="Screenshot 2026-10-05 154127" src="https://github.com/user-attachments/assets/8c0cc6cb-b2f7-4765-9106-5eed4ac958c7" />

### Login gagal (username atau password kosong)
<img width="580" height="126" alt="Screenshot 2026-10-05 154229" src="https://github.com/user-attachments/assets/45cfc4c5-f836-4cc0-a0f4-64dd7faf834b" />

### Kesempatan login habis
<img width="637" height="137" alt="Screenshot 2026-10-05 154329" src="https://github.com/user-attachments/assets/158e4311-45ea-4aa9-b72a-c9c127ef7890" />

### Tampilan menu admin
<img width="550" height="322" alt="Screenshot 2026-10-05 144402" src="https://github.com/user-attachments/assets/6f800640-ec6d-4602-8dee-80fae6445766" />

### Pilihan menu admin tidak valid
<img width="717" height="142" alt="Screenshot 2026-10-05 160658" src="https://github.com/user-attachments/assets/735d3589-fd14-448e-beba-c8b7e06d699e" />

### Menampilkan Data
<img width="890" height="188" alt="Screenshot 2026-10-05 144424" src="https://github.com/user-attachments/assets/cd774cdb-1749-4c82-ba26-556e19374054" />

### Menambah Data
<img width="601" height="227" alt="Screenshot 2026-10-05 144509" src="https://github.com/user-attachments/assets/e924628d-eb79-49c3-b9db-df818f29cd65" />

### Mengubah Data
<img width="862" height="505" alt="Screenshot 2026-10-05 144614" src="https://github.com/user-attachments/assets/cd0829b7-9476-4c35-9b93-b83faaecba9f" />

### Menghapus Data
<img width="852" height="390" alt="Screenshot 2026-10-05 144654" src="https://github.com/user-attachments/assets/0b6817f4-65ee-44ad-b4a6-991054e284a3" />

### Hitung Total
<img width="495" height="143" alt="Screenshot 2026-10-05 144717" src="https://github.com/user-attachments/assets/ed524eb8-ff84-4a67-b3b1-e729139936c9" />

### Tampilan menu user
<img width="561" height="242" alt="Screenshot 2026-10-05 144949" src="https://github.com/user-attachments/assets/8c9c89f9-787d-4586-bdd0-9a73598e980a" />

### User melihat data dan total
<img width="851" height="192" alt="Screenshot 2026-10-05 145005" src="https://github.com/user-attachments/assets/fec0a615-1c75-48ac-8ca7-4ea8bdb81e54" />
<img width="483" height="148" alt="Screenshot 2026-10-05 145052" src="https://github.com/user-attachments/assets/7d279428-d7c2-4c21-9d59-f8f7d7390efe" />

### Keluar Dari Program 
<img width="446" height="105" alt="Screenshot 2026-10-05 145112" src="https://github.com/user-attachments/assets/2a0e95eb-5e17-47d7-bd42-a99bfcbe660c" />
