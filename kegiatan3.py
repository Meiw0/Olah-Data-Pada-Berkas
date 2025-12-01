import shelve

NIM = "L200250202"
NAMA_FILE_SHELVE = "faiz"

file = open(NIM, "r")
nim_baca = file.readline().strip()
tgl_baru = file.readline().strip()
nama_baca = file.readline().strip()
kota_baca = file.readline().strip()
file.close()

data_shelve = shelve.open(NAMA_FILE_SHELVE)

data_shelve['nim'] = nim_baca
data_shelve['tanggal'] = tgl_baru
data_shelve['nama'] = nama_baca
data_shelve['kota'] = kota_baca

data_shelve.close()

print(f"Sukses! Data berhasil dipindah ke file shelve: {NAMA_FILE_SHELVE}")