"""
program perulangan membaca buku menggunakan while
"""
jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_di_baca = 0
print(f'jumlah buku yang sudah di baca{jumlah_buku_yang_sudah_di_baca}')

while jumlah_buku_yang_sudah_di_baca < jumlah_buku:
    jumlah_buku_yang_sudah_di_baca = jumlah_buku_yang_sudah_di_baca + 1
    print(f"baca buku ke {jumlah_buku_yang_sudah_di_baca} sudah di baca")


print(f'jumlah buku yang sudah di baca{jumlah_buku_yang_sudah_di_baca}')