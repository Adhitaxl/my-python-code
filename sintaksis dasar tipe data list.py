daftar_buku = ['Seven Habist', 'How to Influence People', 'First Things First', '4DX']
print('Tampilkan_variable_daftar_buku')
print(daftar_buku)

print('\nProses semua dengan fon in ')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indexs tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'kenji volume 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habist', 'How to Influence People', 'First Things First', '4DX']
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTanmbah satu buku')
daftar_buku = ['Seven Habist', 'How to Influence People', 'First Things First', '4DX']
daftar_buku.append('matematika')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti Elemen Pertama')
daftar_buku = ['Seven Habist', 'How to Influence People', 'First Things First', '4DX']
daftar_buku[0] = 'Eight Habist'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke 1')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang di ambil tadi')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1')
daftar_buku = ['Seven Habist', 'How to Influence People', 'First Things First', '4DX']
daftar_buku.pop(-3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['Seven Habist', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])







