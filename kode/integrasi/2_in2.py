import math

def f(x):
    return x**2

def simpsons13(atas, bawah, n):
    langkah = (atas - bawah) / n

    x = list()
    fx = list()

    i = 0
    while i <= n:
        x.append(bawah + i * langkah)
        fx.append(f(x[i]))
        i += 1

    hasil = 0
    i = 0
    while i <= (n-1):
        if i == 0 or i == n:
            hasil += fx[i]
        elif i % 2 != 0:
            hasil += 4 * fx[i] #koefisien 4
        else:
            hasil += 2 * fx[i] #koefisien 2
        i += 1
        print("i = " + str(i) + " langkah = ", langkah,
              " fungsi ", f(bawah + i * langkah), " hasil sementara ", hasil * (langkah / 3))
    hasil = hasil * (langkah / 3)
    return hasil

bawah = 0
atas = 1
n = 10
print("Nilai Integral Simpson 1/3 adalah  ",
      "%.8f" % simpsons13(atas, bawah, n))
