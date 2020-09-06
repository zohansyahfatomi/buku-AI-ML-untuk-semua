import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1/(1 + x**2)

titik_x = (-12, -9, -6, -3,-1,0,1, 3, 6, 9, 12)
titik_y = (f(-12),f(-9),f(-6),f(-3),f(-1),f(0),f(1), f(3), f(6), f(9), f(12) )
plt.plot(titik_x, titik_y, 'ok')
plt.show()
#titik_x = np.array([1, 3, 6, 10, 12])
#titik_y = np.array([1, 9, 36, 100, 144])

def interpolas_newton(x, y):
    n = len(x)

    # mengkonstruksi tabel array dan menempatkan nilai xy ke kolom pertama
    P = np.zeros((n, n + 1))
    P[:, 0] = x[:]
    P[:, 1] = y[:]

    # mengisi nilai ke dalam formulasi beda hingga
    for j in range(2, n + 1):
        for k in range(j - 1, n):
            P[k, j] = (P[k, j - 1] - P[k - 1, j - 1]) / (P[k, 0] - P[k - j + 1, 0])

    q = np.zeros(n)
    for l in range(0, n):
        q[l] = P[l, l + 1]
    return q

# Evaluasi polinomial
def poly(t, x, q):
    n = len(x)
    out = q[n - 1]
    for k in range(n - 2, -1, -1):
        out = out * (t - x[k]) + q[k]
    return out

# kalkulasi koefisien
b = interpolas_newton(titik_x, titik_y)
x_val = np.linspace(min(titik_x) - 1, max(titik_x) + 1, 100)
y_val = poly(x_val, titik_x, b)

# ploting grafik
plt.plot(titik_x, titik_y, color='black', marker='o', linestyle='', label='data')
plt.plot(x_val, y_val, color='black', linestyle='-', label='Interpolasi Newton')
plt.legend(loc='best')
plt.show()
