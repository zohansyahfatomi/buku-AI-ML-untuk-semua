import numpy as np

P = np.array([[1,3,2],[-4,7,8],[6,7,0]])
Q = np.array([[1,2,3,1],[4,5,6,2],[11,3,6,3]])
R = np.dot(P,Q)
print(P, "\nx\n", Q, "\n=\n", R)
