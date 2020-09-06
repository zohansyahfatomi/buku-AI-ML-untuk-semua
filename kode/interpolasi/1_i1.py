import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)
xvals = np.linspace(0, 2*np.pi, 100)
yinter = np.interp(xvals,x,y)

plt.plot(x,y,"ko")
plt.plot(xvals, yinter, "--k")
plt.show()
