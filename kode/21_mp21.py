import matplotlib.pyplot as plt
import numpy as np

indeks = np.arange(5)
nilai1 = [4,6,2,5,7]
nilai2 = [1,2,3,4,5]
nilai3 = [2,4,3,5,7]

bw = 0.1

plt.title('Sinau Grafik Batang Multiserial')
plt.bar(indeks, nilai1, bw, color='k', label='data-1')
plt.bar(indeks+bw, nilai2, bw, color='g', label='data-2')
plt.bar(indeks+2*bw, nilai3, bw, color='r', label='data-3')
plt.xticks(indeks + .1,['A','B','C','D','E'])
plt.legend()
plt.show()