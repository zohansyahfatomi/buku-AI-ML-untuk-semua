import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 + x**2 - 3*x -3

x = np.arange(-2,2,0.01)
y = f(x)
plt.plot(x,y,"k",label="$f(x) = x^3 + x^2 -3x -3$")
plt.legend()
plt.show()