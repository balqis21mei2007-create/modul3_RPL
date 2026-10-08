from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel

# ==========================================
# 1. PENGUJIAN BUKU MODEL (CRUD)
# ==========================================
print("==========================================")
print("          PENGUJIAN BUKU MODEL            ")
print("==========================================")

model = BukuModel()

# 1. Test Create Buku
print("\n=== Menambahkan Data Buku ===")
model.insert_buku("Last Seen By Gabriella", "ISMAAWTN", 2026)
print("Data berhasil disimpan!")

# 2. Test Read Pertama
print("\n=== Daftar Buku Setelah Insert ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# Ambil ID buku paling baru yang baru saja di-insert agar tidak error Foreign Key
id_target = daftar_buku[-1]['id_buku']

# 3. Test Update Buku (Mengubah data buku yang baru dimasukkan)
print(f"\n=== Mengubah Data Buku ID {id_target} ===")
model.update_buku(id_target, "Last Seen By Gabriella", "ISMAAWTN", 2026)
print("Data berhasil diperbarui!")

# 4. Test Read Setelah Update
print("\n=== Daftar Buku Setelah Update ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# 5. Test Delete Buku (Menghapus buku yang baru dimasukkan)
print(f"\n=== Menghapus Data Buku ID {id_target} ===")
model.delete_buku(id_target)
print("Data berhasil dihapus!")

# 6. Test Read Setelah Delete
print("\n=== Daftar Buku Setelah Delete ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")


# ==========================================
# 2. PENGUJIAN ANGGOTA MODEL (CREATE & READ)
# ==========================================
print("\n==========================================")
print("         PENGUJIAN ANGGOTA MODEL          ")
print("==========================================")

anggota_model = AnggotaModel()

# 1. Test Create Anggota
print("\n=== Menambahkan Data Anggota ===")
anggota_model.insert_anggota("Iqish", "Jl. R.E. Martadinata")
print("Data anggota berhasil disimpan!")

# 2. Test Read Anggota
print("\n=== Daftar Anggota ===")
daftar_anggota = anggota_model.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")