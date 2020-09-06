import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 36-x**2

x = np.arange(-10,10,0.01)
y = f(x)
#plt.grid(True)
plt.plot(x,y,"k",label="f(x)=$36-x^2$")
plt.show()