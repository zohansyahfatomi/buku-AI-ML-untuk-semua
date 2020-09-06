class Wayang :
    def __init__(self, nama):
        self.nama = nama 
    
    def cetak_nama(self):
        print(f'Wayang ini namanya : {self.nama}')
    
class Pandawa (Wayang):
    def cetak_nama(self):
        print(f'Wayang ini namanya : {self.nama}')

class Kurawa (Wayang):
    def cetak_nama(self):
        print(f'Kurawa ini namanya : {self.nama}')
    
arjuna = Pandawa("arjuna")
dursasana = Kurawa("dursasana")
arjuna.cetak_nama()
dursasana.cetak_nama()