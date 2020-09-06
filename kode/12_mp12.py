import matplotlib.pyplot as plt
import numpy as np
nilai_x = np.arange(-3*np.pi, 3*np.pi, 0.1)
nilai_y = np.sin(5*nilai_x)/nilai_x
plt.plot(nilai_x,nilai_y,'k')
plt.show()

