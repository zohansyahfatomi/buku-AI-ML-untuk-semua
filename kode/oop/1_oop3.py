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

lembu = Binatang("lembu", "hitam", 2)
kambing = Binatang("kambing", "coklat", 2)

print(f'{lembu.makan()}, {lembu.bernafas()} dan {lembu.bergerak()}')
print(f'{kambing.makan()}, {kambing.bernafas()} dan {kambing.bergerak()}')