import numpy as np

a = np.arange(0,9).reshape(3,3)
b = np.ones((3,3))
hasil = np.dot(a,b)

print("array a : ", a)
print("array b : ", b)
print("hasil a dot b : ", hasil)
