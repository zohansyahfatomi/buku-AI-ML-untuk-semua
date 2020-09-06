import numpy as np
P = np.arange(10,19).reshape((3,3))
print("array P : ",P)

for i in P.flat:
    print(i)