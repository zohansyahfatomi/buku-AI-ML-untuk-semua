class Angka :
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def tambah(self):
        return self.a + self.b

objek_angka = Angka(5,7)
print(objek_angka.tambah())