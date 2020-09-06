import numpy as np
data = np.random.random(16).reshape((4,4))
print("array data : ",data)

np.save('simpan',data)
print("data telah disimpan !")