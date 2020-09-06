from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1/(1 + x**2)

x = (-9, -6, -3,-1,0,1, 3, 6, 9)
y = (f(-9),f(-6),f(-3),f(-1),f(0),f(1), f(3), f(6), f(9))

cs = CubicSpline(x, y)
xs = np.arange(-9, 9, 0.1)

plt.plot(x, y, 'ok', label='Data')
plt.plot(xs, f(xs), 'k', label='$f(x) = \\frac{1}{1+x^{2}}$')
plt.plot(xs, cs(xs), 'k--', label="Interpolasi Spline-Kubik")

plt.xlim(-10, 10)
plt.legend(loc='best')
plt.show()