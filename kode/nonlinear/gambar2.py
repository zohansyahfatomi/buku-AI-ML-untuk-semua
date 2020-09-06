import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x*np.sin(x)-np.exp(x)

x = np.arange(-2,1,0.01)
y = f(x)
#plt.grid(True)
plt.plot(x,y,"k",label="f(x) = x*sin(x)-exp(x)")
plt.legend()
plt.show()