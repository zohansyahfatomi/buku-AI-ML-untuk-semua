class Segi_empat:
    def __init__(self, p, l):
        self.p = p 
        self.l = l
    
    def luas(self):
        return self.p * self.l

class Persegi(Segi_empat):
    def __init__(self, p):
        super().__init__(p, p)

persegi = Persegi(5)
print(persegi.luas())