import numpy as np

def fung(x):
    return (x**3 + x**2 -3)/3

def fixpoint(x0, e):
    i = 0
    while (abs(fung(x0)-x0) > e):
        i = i + 1
        x0 = fung(x0)
        print('{:2d}    {:3.4f}    {:3.4f}    '
              .format(i, x0, fung(x0)))
    return x0

a = -1.7
tol = 1e-04

print("Hasil Metode Regula-Falsi:")
print(" i       x0      fung(x0)")
hasil = fixpoint(a, tol)
print("Hasil akarnya adalah :", round(hasil, 4))
