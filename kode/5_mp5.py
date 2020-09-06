import matplotlib.pyplot as plt
plt.xlabel("Sumbu-X", color = 'gray') #sumbu-X-teredit
plt.ylabel("Sumbu-Y", color = 'gray') #sumbu-Y-teredit
plt.title("Sinau Title",fontsize=20) #judul_grafik-teredit
plt.axis([0,6,0,20]) #limitasi_sumbu
plt.plot([1,1,2,3,5,8,13,21,34,55],color='black')
plt.show()
