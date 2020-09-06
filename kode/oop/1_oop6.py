class Private :
    def __init__(self):
        self.__private = "variabel private"
        self.bukanprivate = "bukan variabel private"
    
    def cetak_var(self): #enkapsulasi
        print(f'{self.__private} digunakan hanya dalam sebuah kelas')

coba = Private()
print(coba.bukanprivate)
print(coba.__dict__)
print(coba.cetak_var()) 
print(coba.__private)