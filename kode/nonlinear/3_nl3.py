import numpy as np

def fungsi(x):
    return np.sin(x) * x - np.exp(x)

def secant(x0, x1, tol):
    i = 0
    x_temp = x0
    while abs(fungsi(x_temp)) > tol :
        i = i + 1
        if fungsi(x1) - fungsi(x0) == 0:
            return x1
        x_temp = x1 - (fungsi(x1) * (x1 - x0) * 1.0) / (fungsi(x1) - fungsi(x0))
        x0 = x1
        x1 = x_temp
        print('{:2d}    {:3.4f}    {:3.4f}    {:3.4f}     {:3.4f}'
              .format(i, x0, x1, x_temp, fungsi(x1)))
    return x1

x0 = -2
x1 = 3
tol = 1e-04
print("Hasil Metode Secant :")
print("i      x0         x1       x_temp    fung(x1)")
hasil = secant(x0, x1, tol)
print("Hasil akarnya adalah :", round(hasil, 4))