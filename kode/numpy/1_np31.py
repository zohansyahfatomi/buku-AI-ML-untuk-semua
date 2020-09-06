import numpy as np
data = np.genfromtxt('data_tes.csv', delimiter =',', names=True)
print("hasil pembacaan data : ",data)

print("data[0]: ", data[0])
print("data['id']: ", data['id'])
print("data['nilai2']: ", data['nilai2'])
print("data['nilai3']: ", data['nilai3'])