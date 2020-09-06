import matplotlib.pyplot as plt
plt.grid(True) #grid
plt.text(1.2,12.1,r'$y = \frac{(x_1^n - x_2^n)}{\sqrt{5}}$',fontsize=20,bbox={'facecolor':'yellow',
'alpha':0.2}) #Teks_LaTeX
plt.text(1,1.3,'Pertama') #Teks_1
plt.text(2,2.3,'Kedua') #Teks_2
plt.text(3,3.3,'Ketiga') #Teks_3
plt.text(4,5.3,'Keempat') #Teks_4
plt.text(5,8.3,'Kelima') #Teks_5
plt.xlabel("Sumbu-X", color = 'gray') #sumbu-X-teredit
plt.ylabel("Sumbu-Y", color = 'gray') #sumbu-Y-teredit
plt.title("Sinau Title",fontsize=20) #judul_grafik-teredit
plt.axis([0,6,0,20]) #limitasi_sumbu
plt.plot([1,1,2,3,5,8,13,21,34,55],'ko')
plt.show()
