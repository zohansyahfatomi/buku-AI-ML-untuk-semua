import numpy as np

print("Hasil Metode Bisection :")
def fungsi(x):
    return np.sin(x)*x-np.exp(x)

def metode_bisection(atas, bawah, toleransi):
    i = 0
    if fungsi(atas) * fungsi(bawah) > 0:
        print("Fungsi Tidak Memiliki Akar.")
    else:
        while (bawah - atas) / 2.0 > toleransi:
            titik_tengah = (atas + bawah) / 2.0
            i = i + 1
            print('{:2d}    {:3.4f}    {:3.4f}    {:3.4f}     {:3.4f}'
                  .format(i, bawah, atas, titik_tengah, fungsi(titik_tengah)))
            if fungsi(titik_tengah) == 0:
                return (titik_tengah)
            elif fungsi(atas) * fungsi(titik_tengah) < 0:
                bawah = titik_tengah
            else:
                atas = titik_tengah
        return (titik_tengah)

print("i       a          b         c         f(c)")
print("1    3.0000    -2.0000    0.5000     -1.4090")
hasil = metode_bisection(-2, 3, 1e-4)

print("Hasil akarnya adalah :", round(hasil, 4))
