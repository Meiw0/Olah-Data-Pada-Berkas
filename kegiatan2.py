NIM = "L200250202"       
KOTA_LAHIR = "Sukoharjo" 

file = open(NIM, "a")
file.write(KOTA_LAHIR)
file = open(NIM, "r")

nim_baca = file.readline().strip()  #NIMmu
tgl_baca = file.readline().strip() #tanggal lahirmu
nama_baca = file.readline().strip() # namamu

file.close()

tanggal, bulan, tahun = tgl_baca.split("-") #yang awalnya 31-03-2007 displit menjadi (31, 03, 2007) jadi 03/31/2007
tgl_baru = f"{bulan}/{tanggal}/{tahun}"

print(nama_baca)
print(f"{KOTA_LAHIR}, {tgl_baru}")
print(nim_baca)