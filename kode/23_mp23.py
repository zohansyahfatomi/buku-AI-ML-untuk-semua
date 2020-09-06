import matplotlib.pyplot as plt
import numpy as np

label = ['Padi','Jagung','Sagu','Ketela']
nilai = [60, 20, 15, 5]
warna = ['blue','red','green','yellow']
pisah = [0, 0, 0, .3]
plt.pie(nilai, labels=label, colors=warna, explode=pisah,
        shadow= True, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
plt.show()
