import numpy as np

P = np.array([[3,1,2,4],[4,10,19,11],[1,2,4,9],[1,13,1,16]])
d_P = np.linalg.det(P)
print(P, "\n=========\n|determinan| \n=========\n", d_P, "\n")
print("Dimensi matriks [P] = ", P.shape)
