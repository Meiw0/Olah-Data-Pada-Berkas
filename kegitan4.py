import shelve

NAMA_FILE_SHELVE = "faiz" 

data_shelve = shelve.open(NAMA_FILE_SHELVE)

print("Nama    :", data_shelve['nama'])
print("NIM     :", data_shelve['nim'])
print("Tanggal :", data_shelve['tanggal'])
print("Kota    :", data_shelve['kota'])

data_shelve.close()