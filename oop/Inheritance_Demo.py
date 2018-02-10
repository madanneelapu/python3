#Single Inheritance and multi-level inheritance example
class Base:
    def print(self):
        print("Base - Print")


class Derived(Base):
    def print(self):
        print("Derived - Print")


class Derived1(Base):  # Derived1 class extending Base class
    pass
    # def print(self):
    #     print("Derived1 - Print")


class Derived2(Derived1):
    pass
    # def print(self):
    #     print("Derived2 - Print")


obj = Derived2()
obj.print()

print(Derived2.__mro__)
print(Derived.__mro__)
print(Derived2.__bases__)