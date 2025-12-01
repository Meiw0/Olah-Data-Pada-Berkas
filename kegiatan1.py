NIM = "L200250202"           
NAMA = "Muhammad Nur Faiz"      
TGL_LAHIR = "31-03-2007"   

file = open(NIM, "w")

file.write(NIM + "\n")
file.write(TGL_LAHIR + "\n")
file.write(NAMA + "\n")

file.close()

print(f"Sukses! File berkas teks bernama '{NIM}' berhasil dibuat.")