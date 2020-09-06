import numpy as np
P = np.array([[1, 3, 2],[-4, 7, 8]])
Q = np.array([[1, 3, 2],[4, 5, 6]])
R1 = np.add(P,Q)
R2 = np.subtract(P,Q)
print(P, "\n+\n", Q, "\n=\n", R1)
print("=====================")
print(P, "\n-\n", Q, "\n=\n", R2)
