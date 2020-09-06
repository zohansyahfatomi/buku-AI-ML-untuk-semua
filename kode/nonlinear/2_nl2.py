import numpy as np

def dx(fung,x):
    return abs(0-fung(x))

def fung(x):
    return np.sin(x) * x - np.exp(x)

def dfung(x):
    return x*np.cos(x)+np.sin(x)-np.exp(x)

def newtonraphson(fung, dfung, x0, e):
    i = 0
    delta = dx(fung, x0)
    while delta > e:
        x0 = x0 - fung(x0)/dfung(x0)
        delta = dx (fung, x0)
        i = i + 1
        print('{:2d}    {:3.4f}    {:3.4f}    {:3.4f}     {:3.4f}'
              .format(i, x0, fung(x0), dfung(x0), fung(x0)/dfung(x0)))
    print("Hasil akarnya adalah :", round(x0,4))

x0 = 3.0
eps = 1e-4

print("Hasil Metode Newton-Raphson :")
print(" i      x0      fung(x0)  dfung(x0) fung(x0)/ dfung(x0)")
newtonraphson(fung, dfung, x0, eps)