import numpy as np
import matplotlib.pyplot as plt

def interpolasi_langrange(titik, x):
    jumlah = 0
    n = len(titik)
    for i in range(n):
        xi, yi = titik[i]

        def L(i):
            Lvalue = 1
            for j in range(n):
                if i == j:
                    continue
                xj, yj = titik[j]
                Lvalue *= float(x - xj) / float(xi - xj)
            return Lvalue

        jumlah += yi * L(i)
    return jumlah

data = np.array([[1, 1], [3, 9], [6, 36], [10, 100], [12, 144]])
z = []  # untuk menampung data interpolasi

for i in range(13):
    z.append([i, np.round(interpolasi_langrange(data, i), 10)])

z = np.array(z)
print(z)  # hasil data interpolasi
plt.plot(data[:, 0], data[:, 1], 'ko', label="Data")
plt.plot(z[:, 0], z[:, 1], 'k', label="Interpolasi Lagrange")
plt.legend()
plt.show()