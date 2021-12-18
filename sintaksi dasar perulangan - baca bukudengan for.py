"""
program perulangan baca buku
"""
jumlah_buku = 100
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_yang_sudah_di_baca = 0
print(f'jumlah buku Yang sudah di baca {jumlah_buku_yang_sudah_di_baca}')

print('dengn "for"')
for jumlah_buku_yang_sudah_di_baca in range(1, jumlah_buku+1):
    print(f"buku ke {jumlah_buku_yang_sudah_di_baca} sudah di baca")

print(f'jumlah buku yang sudah di baca {jumlah_buku_yang_sudah_di_baca}')

# tanpa for
print ('tanpa "for"')
print("membaca buku ke 1")
print("membaca buku ke 2")
print("membaca buku ke 3")
print("membaca buku ke 4")
print("membaca buku ke 5")
print("membaca buku ke 6")
print("membaca buku ke 7")
print("membaca buku ke 8")
print("membaca buku ke 9")
print("membaca buku ke 10")

