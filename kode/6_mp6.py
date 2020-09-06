import matplotlib.pyplot as plt
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
