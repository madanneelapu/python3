# MRO in Multiple Inheritance with Diamond problem
class Base:
    def print(self):
        print("Base - Print")

class Base1(Base):
    def print(self):
        print("Base1 - Print")

class Base2(Base):
    def print(self):
        print("Base2 - Print")


class Derived(Base1, Base2):
    def print(self):
        print("Derived - Print")

print(Derived.__mro__) # the most important point here is... A base class must not be called before derived class. This is taken care by c3 algorithm