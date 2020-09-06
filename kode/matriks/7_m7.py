import numpy as np

Q = np.array([[-3,-2],[-1,-4]])
ne, ve = np.linalg.eig(Q)
print(Q, "\n=========\n"
         "|nilai eigen| "
         "\n=========\n"
         ,ne,"\n"
         "|vektor eigen| "
         "\n=========\n"
        ,ve, "\n")