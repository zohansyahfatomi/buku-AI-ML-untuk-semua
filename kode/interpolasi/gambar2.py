import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,14])
y = np.array([1,7])
axes = plt.gca()
axes.set_xlim([0,15])
axes.set_ylim([0,8])
plt.scatter(x,y,color="black")
plt.plot(x,y,color="black")
plt.show()