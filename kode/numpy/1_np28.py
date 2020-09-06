import numpy as np
i = np.arange(16).reshape((4,4))
print("array i : ",i)

[i1, i2, i3] = np.split(i,[1, 3], axis=0)

print("array i1 : ",i1)
print("array i2 : ",i2)
print("array i3 : ",i3)

[j1, j2, j3] = np.split(i,[1, 3], axis=0)

print("array j1 : ",j1)
print("array j2 : ",j2)
print("array j3 : ",j3)
