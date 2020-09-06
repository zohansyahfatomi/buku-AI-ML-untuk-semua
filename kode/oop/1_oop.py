class Binatang :
    hidup = True #atribut kelas
    
    def __init__(self, nama, warna, umur): #konstruktor
        self.nama = nama #atribut objek
        self.warna = warna
        self.umur = umur 
    
    def makan(self):
        return"{} sedang makan".format(self.nama)

    def bernafas(self):
        return"{} sedang bernafas".format(self.nama)
    
    def bergerak(self):
        return"{} sedang bergerak".format(self.nama)