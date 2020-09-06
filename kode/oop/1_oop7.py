class Makhluk_hidup:
    def __init__(self):
        print("Konstruktor kelas Makhluk_hidup")
    
    def hidup(self):
        print("Method kelas Makhluk_hidup")

class Manusia(Makhluk_hidup):
    def __init__(self):
        print("Konstruktor kelas Manusia")
    
    def berpikir(self):
        print("Method kelas Manusia")

class Hewan(Makhluk_hidup):
    def __init__(self):
        print("Konstruktor kelas Hewan")

    def setia_kawan(self):
        print("Method kelas Hewan")

makhluk = Makhluk_hidup()

makhluk.hidup()

fisikawan = Manusia()

fisikawan.berpikir()

fisikawan.hidup()

lembu = Hewan()

lembu.setia_kawan()

lembu.hidup()