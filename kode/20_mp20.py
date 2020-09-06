import matplotlib.pyplot as plt
import numpy as np

indeks = np.arange(5)
nilai1 = [4,6,2,5,7]

plt.title('Sinau Grafik Batang Horizontal')
plt.barh(indeks, nilai1, color='k', label='data', height=0.1)
plt.yticks(indeks,['A','B','C','D','E'])
plt.legend(loc=5)
plt.show()