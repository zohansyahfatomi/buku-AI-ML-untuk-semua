import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return -3*x+3

def g(x):
    return 3*x

x = np.arange(-10,10.1,0.1)
y = f(x)
y1 = g(x)
#plt.grid(True)
plt.plot(x,y,"k",label="f(x)")
plt.plot(x,y1,"k",label="g(x)")
plt.text(2.5,-2,"Solusi: \n $x = 0.53$ \n $y = 1.56$" )
plt.scatter([0.53],[1.56],color='k')
plt.show()