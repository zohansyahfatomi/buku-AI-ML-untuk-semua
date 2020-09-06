from scipy.special import hermite

import matplotlib.pyplot as plt
import numpy as np

min = -2.0
max = 2.0
langkah = 0.1

def f0(x):
    return 1

def f1(x):
    return 2*x

def f2(x):
    return 4*x**2 -2

def f3(x):
    return 16*x**4 - 48*x**2 + 12

x0 = np.arange(min,max+langkah,langkah)
y0 = f0(x0)
plt.plot(x0,y0, label="P0(x)")

x1 = np.arange(min,max+langkah,langkah)
y1 = f1(x1)
plt.plot(x1,y1, label="P1(x)")




plt.xlim(-2.0,2.0)
plt.ylim(-3.0,3.0)

plt.savefig('2_hermite.png')
plt.legend()
plt.show()