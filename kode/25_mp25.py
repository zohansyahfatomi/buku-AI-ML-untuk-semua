import matplotlib.pyplot as plt
import numpy as np

N = 8
t_0 = 0.
t_max = 2*np.pi

theta = np.arange(t_0, t_max, t_max/N)
radial = np.array([1,2,3,4,4,3,6,7])

plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
plt.bar(theta, radial, width=(2*np.pi/N), bottom = 0.0, color = 'k')
plt.show()
