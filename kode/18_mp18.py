import matplotlib.pyplot as plt

indeks = ['A', 'B', 'C', 'D', 'E']
nilai = [5, 8, 3, 1, 2]

plt.title('Sinau Grafik Batang')
plt.bar(indeks, nilai, color='k',width = 0.1)
plt.show()
