#Static variable and static methods
#count number of objects
class Employee:
    # static variable
    __hraper = 25

    __objectcount = 0 #for counting number of objects

    # static method
    @staticmethod
    def sethraper(newper):
        Employee.__hraper = newper

    @staticmethod
    def get_objectcount():
        return Employee.__objectcount

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        Employee.__objectcount += 1 #increment count

    def get_salary(self):
        return self.__salary + self.__salary * Employee.__hraper / 100

    def __del__(self):
        Employee.__objectcount -= 1 #decrement count

print(Employee.get_objectcount())
e = Employee("Abc", 50000)
print(e.get_salary())
print(Employee.get_objectcount())
Employee.sethraper(40)
print(e.get_salary())
print(Employee.get_objectcount())
del e
print(Employee.get_objectcount())