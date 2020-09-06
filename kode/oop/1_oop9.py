class A : 
    def mt(self):
        print("Method kelas A terakses")

class B(A):
    def mt2(self):
        print("Method kelas B terakses")

class C(A):
    def mt3(self):
        print("Method kelas C terakses")

class D(B,C):
    def mt4(self):
        print("Method kelas D terakses")
    
p = D()
p.mt()
p.mt2()
p.mt3()
p.mt4()
