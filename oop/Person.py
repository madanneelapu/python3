# properties example
# class methods example

class Person:

    @classmethod
    def create(cls): #classmethods are much like factory method
        return Person("John Doe",30)

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self): #getter
        return self.__age

    @age.setter
    def age(self, newage): #setter
        if newage < 0 or newage > 125:
            raise ValueError("Invalid Age")
        else:
            self.__age = newage

    def get_age(self):
        return self.__age

    def set_age(self, newage):
        if newage < 0 or newage > 125:
            raise ValueError("Invalid Age")
        else:
            self.__age = newage

    def __str__(self):
        return "%s %s" % (self.__name, self.__age)

p = Person("Bill Gates", 62)

p.set_age(65)
print(p.get_age())

p.age = 70 #accessing setter
print(p.age) #accessing getter

john = Person.create() #creating an object using classmethod
print(john)