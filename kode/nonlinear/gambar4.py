import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x**3 + x**2 -3)/3

def g(x):
    return x

x = np.arange(-2,2,0.01)
y = f(x)
y1 = g(x)
axes = plt.gca()
axes.set_xlim([-1.9,-.9])
axes.set_ylim([-1.9,-.9])
plt.plot(x,y,"k",label="$g(x) = (x^3 + x^2 -3)/3$")
plt.plot(x,y1,"k--",label="$y(x) = x$")
plt.legend()
plt.show()