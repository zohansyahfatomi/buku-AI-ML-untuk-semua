import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2.0, 2.0, 0.01)
y = np.arange(-2.0, 2.0, 0.01)

X, Y = np.meshgrid(x,y)

def f(x,y):
        return(np.sin(x)**2  +  np.cos(y)**2)

C = plt.contour(X, Y, f(X,Y), colors='k')
plt.clabel(C, inline=1, fontsize = 10)
plt.show()
