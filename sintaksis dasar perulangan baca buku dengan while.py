"""
program perulangan membaca buku menggunakan while
"""
book_count = 10
print('ibu berkata, "baca semua bukumu"')
read_count =

undertstood_count = 0
print(f'jumlah buku yang sudah di baca dan di pahami{undertstood_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if undertstood_count == 9:
        print(f"baca buku ke {undertstood_count + 1} belum paham")
    else:
        undertstood_count = undertstood_count + 1
        print(f"buku ke {undertstood_count} sudah di baca dan di pahami")

print(f'jumlah buku yang sudah di baca dan dipahami{undertstood_count}')
if undertstood_count == book_count:
    print('"Bu, semua buku sudah di baca dan di pahami"')
else:
    print(f'Bu, tidak semua buku bisa di pahami budi hanya bisa memahami{undertstood_count} buku')
