import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-3*np.pi, 3*np.pi, 0.1)
y0 = np.sin(5*x)/x
y1 = np.sin(3*x)/x
y2 = np.sin(x)/x
y3 = np.sin(.3*x)/x
plt.plot(x,y0,'k', label = 'y0') #solid
plt.plot(x,y1,'r:', label = 'y1') #dashed
plt.plot(x,y2,'g-.', label = 'y2')#line-dashed
plt.plot(x,y3,'m--', label = 'y3')#semi-dashed
plt.legend()
plt.show()

