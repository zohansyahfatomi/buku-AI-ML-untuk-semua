waktu = {"detik":1, "menit":60, "jam":3600, "hari":86400}
print("panjang komponen dict waktu : ",len(waktu))

biner = {0:"benar", 1:"salah"}
print("Cek! Apakah semua komponen nilai dict biner bernilai True? ",all(biner))

print("Cek! Apakah ada salah satu komponen nilai dict biner bernilai True? ",any(biner))

print("waktu terurut, dari besar ke kecil :", sorted(waktu))

print("waktu terurut, dari kecil ke besar :", sorted(waktu, reverse = True))

print("waktu terurut, dari besar ke kecil (beserta nilainya):", sorted(waktu.items()))




