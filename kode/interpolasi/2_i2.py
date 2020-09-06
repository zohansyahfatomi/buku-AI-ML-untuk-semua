from scipy.interpolate import lagrange
import numpy as np

x = np.array([1,3,6,10,12])
y = np.array([1,9,36,100,144])
print(y)
def fung(x,y):
    poli = lagrange(x,y)
    return poli

print(fung(x,y))

def f(x):
    return 8.882e-16*x**3 + 1 *x**2 - 1.421e-14 *x + 3.553e-15

print(f(11))