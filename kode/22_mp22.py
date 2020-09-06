import matplotlib.pyplot as plt
import numpy as np

label = ['Padi','Jagung','Sagu','Ketela']
nilai = [60, 20, 15, 5]
warna = ['blue','red','green','yellow']
plt.title('Sinau Grafik Lingkarang')
plt.pie(nilai, labels=label, colors=warna)
plt.axis('equal')
plt.show()
