import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 + x**2 - 3*x -3

x = np.arange(-2,2,0.01)
y = f(x)
axes = plt.gca()
axes.set_xlim([-1.7,-0.7])
axes.set_ylim([-0.7,0.55])
plt.plot(x,y,"k",label="$f(x) = x^3 + x^2 -3x -3$")
plt.legend()
plt.show()