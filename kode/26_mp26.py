from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)

nilai_x = np.arange(-2, 2, 0.1)
nilai_y = np.arange(-2,2, 0.1)
nilai_x,nilai_y = np.meshgrid(nilai_x,nilai_y)

def f(nilai_x, nilai_y):
    return (np.sin(nilai_x) ** 2 + np.cos(nilai_y) ** 2)

ax.plot_surface(nilai_x,nilai_y,f(nilai_x,nilai_y),rstride=1,cstride=1,color='k')
plt.show()