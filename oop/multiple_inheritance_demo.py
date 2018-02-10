# Multiple Inheritance example
class Base1:
    def print(self):
        print("Base1 - Print")


class Base2:
    def print(self):
        print("Base2 - Print")


class Derived1(Base1):
    def print(self):
        print("Derived1 - Print")


class Derived2(Base2):
    def print(self):
        print("Derived2 - Print")


class Derived3(Derived1, Derived2):  # Left-to-Right order of super classes matters in MRO
    def print(self):
        print("Derived3 - Print")


class Derived4(Derived2, Derived1):  # Left-to-Right order of super classes matters in MRO
    def print(self):
        print("Derived4 - Print")


print(Derived3.__mro__)
print(Derived4.__mro__)
