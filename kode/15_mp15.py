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
plt.xticks([-3*np.pi,-2*np.pi,-np.pi,0, np.pi, 2*np.pi, 3*np.pi],
           [r'$-3\pi$',r'$-2\pi$',r'$-\pi$', 0, r'$\pi$', r'$2\pi$', r'$3\pi$'])
plt.legend()
plt.show()

