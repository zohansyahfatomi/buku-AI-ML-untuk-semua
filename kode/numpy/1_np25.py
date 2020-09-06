import numpy as np
a = np.ones((4,4))
b = np.zeros((4,4))
print("array a : ",a)
print("array b : ",b)
print("a vstack b : ",np.vstack((a,b)))
print("a hstack b : ",np.hstack((a,b)))