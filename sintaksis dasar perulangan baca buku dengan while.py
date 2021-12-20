"""
program perulangan membaca buku menggunakan while
"""
jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')
jumlah_baca  = 0

jumlah_buku_yang_sudah_di_baca_dan_di_pahami = 0
print(f'jumlah buku yang sudah di baca{jumlah_buku_yang_sudah_di_baca_dan_di_pahami}')

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_buku_yang_sudah_di_baca_dan_di_pahami == 9:
        print(f"baca buku ke {jumlah_buku_yang_sudah_di_baca_dan_di_pahami + 1} belum paham")
    else:
        jumlah_buku_yang_sudah_di_baca_dan_di_pahami = jumlah_buku_yang_sudah_di_baca_dan_di_pahami + 1
        print(f"buku ke {jumlah_buku_yang_sudah_di_baca_dan_di_pahami} sudah di baca dan di pahami")

print(f'jumlah buku yang sudah di baca dan dipahami{jumlah_buku_yang_sudah_di_baca_dan_di_pahami}')
if jumlah_buku_yang_sudah_di_baca_dan_di_pahami == jumlah_buku:
    print('"Bu, semua buku sudah di baca dan di pahami"')
else:
    print(f'Bu, tidak semua buku bisa di pahami. '
         f'budi hanya bisa memahami{jumlah_buku_yang_sudah_di_baca_dan_di_pahami}')
