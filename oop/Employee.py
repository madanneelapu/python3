class Employee:

    #static variable
    __hraper = 25

    #static method
    @staticmethod
    def sethraper(newper):
        Employee.__hraper = newper

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary


    def get_salary(self):
        return self.__salary + self.__salary * Employee.__hraper / 100


e = Employee("Abc", 50000)
print(e.get_salary())

Employee.sethraper(40)
print(e.get_salary())