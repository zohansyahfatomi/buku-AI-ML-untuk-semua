import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

print("kolom stacking a,b,c : ", np.column_stack((a,b,c)))
print("baris stacking a,b,c : ", np.row_stack((a,b,c)))