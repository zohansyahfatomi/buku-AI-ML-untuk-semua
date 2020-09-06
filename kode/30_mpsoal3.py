import matplotlib.pyplot as plt
from pylab import randn
X = randn(200)
Y = randn(200)
print(X,Y)
plt.scatter(X,Y, color='k')
plt.xlabel("sumbu-X")
plt.ylabel("sumbu-Y")
plt.title("Nama_Anda")
plt.show()