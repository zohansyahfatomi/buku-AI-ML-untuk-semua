import numpy as np

P = np.array([[3,1,2,4],[4,10,19,11],[1,2,4,9],[1,13,1,16]])
d_P = np.linalg.inv(P)
print(P, "\n=========\n|invers| \n=========\n", d_P, "\n")

