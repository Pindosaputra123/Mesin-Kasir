# Fungsi Untuk Daftar Menu Makanan
def makanan():
    global total_makan, jumlah_porsi, nama_makanan

# Fungsi Untuk Daftar Menu Minuman
def minuman():
    global total_minum, jumlah_gelas, nama_minuman

# Daftar Makanan
print("|==================================|")
print("|        Pilih Menu Makanan        |")
print("|==================================|")
print("| 1 | Nasi Goreng         Rp.12000 |")
print("| 2 | Ayam Geprek         Rp.12000 |")
print("| 3 | Mie Goreng/Rebus    Rp.5000  |")
print("| 4 | Ketoprak            Rp.7000  |")
print("| 5 | Ikan Bakar          Rp.20000 |")
print("|==================================|")
menu_makanan = int(input("Pilih Menu (1/2/3/4/5) : "))
jumlah_porsi = int(input("Berapa Porsi : "))

if menu_makanan == 1:
    total_makan = jumlah_porsi * 12000
    print("Nasi Goreng",jumlah_porsi,"Prosi : Rp.",total_makan)
    nama_makanan = ("Nasi Goreng")
elif menu_makanan == 2:
    total_makan = jumlah_porsi * 12000
    print("Ayam Geprek",jumlah_porsi,"Prosi : Rp.",total_makan)
    nama_makanan = ("Ayam Geprek")
elif menu_makanan == 3:
    total_makan = jumlah_porsi * 5000
    print("Mie Goreng/Rebus",jumlah_porsi,"Prosi : Rp.",total_makan)
    nama_makanan = ("Mie Goreng/Rebus")
elif menu_makanan == 4:
    total_makan = jumlah_porsi * 7000
    print("Ketoprak",jumlah_porsi,"Prosi : Rp.",total_makan)
    nama_makanan = ("Ketoprak")
elif menu_makanan == 5:
    total_makan = jumlah_porsi * 20000
    print("Ikan Bakar",jumlah_porsi,"Prosi : Rp.",total_makan)
    nama_makanan = ("Ikan Bakar")
else:
    print("Pilihan Tidak Tersedia")


# Daftar Minuman
print()
print("|==================================|")
print("|        Pilih Menu Minuman        |")
print("|==================================|")
print("| 1 | Es Teh               Rp.4000 |")
print("| 2 | Es Jeruk             Rp.4000 |")
print("| 3 | Soda Gembira         Rp.5000 |")
print("| 4 | Kopi Susu            Rp.5000 |")
print("|==================================|")
menu_minuman = int(input("Pilih Menu (1/2/3/4) : "))
jumlah_gelas = int(input("Berapa Gelas : "))

if menu_minuman == 1:
    total_minum = jumlah_gelas * 4000
    print("Es Teh",jumlah_gelas,"Gelas : Rp.", total_minum)
    nama_minuman = ("Es Teh")
elif menu_minuman == 2:
    total_minum = jumlah_gelas * 4000
    print("Es Jeruk",jumlah_gelas,"Gelas : Rp.", total_minum)
    nama_minuman = ("Es Jeruk")
elif menu_minuman == 3:
    total_minum = jumlah_gelas * 5000
    print("Soda Gembira",jumlah_gelas,"Gelas : Rp.", total_minum)
    nama_minuman = ("Soda Gembira")
elif menu_minuman == 4:
    total_minum = jumlah_gelas * 5000
    print("Kopi Susu",jumlah_gelas,"Gelas : Rp.", total_minum)
    nama_minuman = ("Kopi Susu")
else:
    print("Pilihan Tidak Tersedia")

# Proses Menghitung Semua Harga Yang Harus Dibayar
makanan()
minuman()
jumlah_semuanya = total_makan + total_minum

# Daftar Pembelian
print()
print("|================================|")
print("|        Daftar Pembelian        |")
print("|================================|")
print("| Makanan :",nama_makanan,"\t |")
print("| Porsi   :",jumlah_porsi,"\t\t\t |")
print("| Minuman :",nama_minuman,"\t\t |")
print("| Gelas   :",jumlah_gelas,"\t\t\t |")
print("|================================|")
print("|        Total Pembayaran        |")
print("|================================|")
print("|\t     ",jumlah_semuanya,"\t\t |")
print("|================================|")
print()