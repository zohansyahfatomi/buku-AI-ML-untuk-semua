import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,4,6,8,10,12,14])
y = np.array([1,2,3,4,5,6,7])
axes = plt.gca()
axes.set_xlim([0,15])
axes.set_ylim([0,8])
plt.scatter(x,y,color="black",label="data kecepatan partikel $\zeta$")
plt.xlabel("waktu (s)")
plt.ylabel("kecepatan ( $\\times10^8$ m/s)")
plt.legend(loc=2)
plt.show()