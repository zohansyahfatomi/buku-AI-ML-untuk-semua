import numpy as np

i = np.arange(16).reshape((4,4))
print("array i : ", i)

[a,b] = np.hsplit(i,2)
print("array a : ",a)
print("array b : ",b)

[c,d] = np.vsplit(i,2)
print("array c : ",c)
print("array d : ",d)