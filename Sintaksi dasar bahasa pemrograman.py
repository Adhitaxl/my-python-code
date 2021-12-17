"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. sequential: langkah berurutan
2. percabangan: langkah melompat jika kondisi terpenuhi
3. perulangan: mengulang langkah yang sama berkali-kali sampai kondisi terpenuhi
"""

# Sequential
print('Ibu berkata, "pergi ke toko"')
print('Budi menjawab, "Baik apa yang harus saya lakukan pergi ke toko"')
print('Ibu menjawab, "Beli 1 botol susu, dan beli telur 6 butir"')
print('Budi menjawab, "OK"')
print("Maka Budi berangkat ke toko, dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 177
jumlah_telur = 459
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} telur ")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    print("Budi membeli 1 botol susu")
if jumlah_telur == 0:
    print("Budi mengecek harganya, dan ternyata uangnya masih cukup")
    print("Budi membeli 6 butir telur")
else:
    print("Budi membeli semua yang di perintah oleh Ibu")
    print("Budi pulang ke rumah")
    print("Menyampaikan hasilnya ke ibu")



