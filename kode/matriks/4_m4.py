import numpy as np

P = np.array([[13,5],[1,2],[3,8]])
P_T = np.transpose(P)
print(P, "\n=========\n|tranpose| \n=========\n", P_T, "\n")
print("Dimensi matriks [P] = ", P.shape)
print("Dimensi matriks [P_T] = ",P_T.shape)