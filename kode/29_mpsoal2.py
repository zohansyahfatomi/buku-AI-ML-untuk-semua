import matplotlib.pyplot as plt
x = ['Python', 'PHP', 'Java', 'C#', 'C++', 'Javascript', 'Fortran']
popularity = [17.4, 8.8, 22.2 , 8, 9, 10, 7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, 0.3, color='k')
plt.xlabel("Bahasa Pemrograman")
plt.ylabel("Popularitas")
plt.title("Nama_Anda")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()