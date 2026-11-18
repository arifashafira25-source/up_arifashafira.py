# PROGRAM KASIR KANTIN KAMPUS

print("===================================")
print("       KASIR KANTIN KAMPUS")
print("===================================")

total_belanja = 0

# Perulangan untuk memasukkan beberapa jenis makanan
while True:
    print("\n--- Input Data Makanan ---")

    nama_makanan = input("Nama makanan  : ")
    harga = int(input("Harga makanan : Rp "))
    jumlah = int(input("Jumlah beli   : "))

    # Menghitung total harga setiap transaksi
    total_harga = harga * jumlah

    # Menambahkan ke total belanja
    total_belanja += total_harga

    print("Total harga   : Rp", total_harga)

    # Menanyakan apakah ingin menambah makanan
    pilihan = input("\nApakah ingin membeli makanan lain? (y/t): ")

    if pilihan.lower() != "y":
        break

# Menentukan diskon
if total_belanja > 100000:
    diskon = total_belanja * 10 / 100
else:
    diskon = 0

# Menghitung total pembayaran
total_pembayaran = total_belanja - diskon

# Menampilkan hasil transaksi
print("\n===================================")
print("        STRUK PEMBAYARAN")
print("===================================")
print("Total Belanja     : Rp", total_belanja)
print("Diskon 10%        : Rp", int(diskon))
print("-----------------------------------")
print("Total Pembayaran  : Rp", int(total_pembayaran))
print("===================================")
print("       TERIMA KASIH")
print("===================================")