import matplotlib.pyplot as plt
import numpy as np
nilai_x = np.arange(-3*np.pi, 3*np.pi, 0.1)
nilai_y0 = np.sin(5*nilai_x)/nilai_x
nilai_y1 = np.sin(3*nilai_x)/nilai_x
nilai_y2 = np.sin(nilai_x)/nilai_x
plt.plot(nilai_x,nilai_y0,'k',label='nilai_y0:hitam')
plt.plot(nilai_x,nilai_y1,'r',label ='nilai_y1:merah')
plt.plot(nilai_x,nilai_y2,'g',label='nilai_y2:hijau')
plt.legend()
plt.show()

