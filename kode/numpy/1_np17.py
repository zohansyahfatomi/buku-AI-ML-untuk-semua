import numpy as np

a = np.arange(0, 9).reshape((3, 3))
print("array a : ",a)
print("array a[0,:] : ",a[0,:])
print("array a[1,:] : ",a[1,:])
print("array a[2,:] : ",a[2,:])
print("array a[:,0] : ",a[:,0])
print("array a[0:2,0:2] : ",a[0:2,0:2])