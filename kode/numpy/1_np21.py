import numpy as np

q = np.random.random((4,4))
print("array q : ",q)
print("q < .5 : ",q < .5)
print("q[q < .5] : ",q[q < .5])