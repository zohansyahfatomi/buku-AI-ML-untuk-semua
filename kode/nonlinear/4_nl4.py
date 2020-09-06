import numpy as np

def fung(x):
    return np.sin(x) * x - np.exp(x)

def regulafalsi(atas, bawah, e):
    if fung(atas) * fung(bawah) >= 0:
        print("Inputan anda tidak memenuhi syarat metode numerik Regulafalsi \n"
              "Silahkan masukan inputan yang benar dimana memenuhi : "
              "\nfung(atas) * fung(bawah) < 0")

        return -1

    c = atas
    i = 0

    while fung(c) > e:
        i = i + 1
        c = (atas * fung(bawah) - bawah * fung(atas)) / (fung(bawah) - fung(atas))

        if fung(c) == 0:
            break

        elif fung(c) * fung(atas) < 0:
            bawah = c
        else:
            atas = c
        print('{:2d}    {:3.4f}    {:3.4f}    {:3.4f}     {:3.4f}'
              .format(i, bawah, atas, c, fung(c)))
    return c

batas_atas = -2.0
batas_bawah = 3.0
tol = 1e-04

print("Hasil Metode Regula-Falsi:")
print("i      x0         x1       x_temp    fung(x_temp)")
hasil=regulafalsi(batas_atas, batas_bawah, tol)
print("Hasil akarnya adalah :", round(hasil, 4))