#Static variable and static methods
#count number of objects
class Employee:
    # static variable
    __hraper = 25

    __objectcount = 0 #for counting number of objects

    __emplist = [] #list to hold employee names
    __totalsalary=0

    # static method
    @staticmethod
    def sethraper(newper):
        Employee.__hraper = newper

    @staticmethod
    def get_objectcount():
        return Employee.__objectcount

    @staticmethod
    def get_emp_list():
        return Employee.__emplist,Employee.__totalsalary

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        Employee.__objectcount += 1 #increment count
        Employee.__emplist.append(name) #add employee name to list upon creation
        Employee.__totalsalary += salary

    def get_salary(self):
        return self.__salary + self.__salary * Employee.__hraper / 100

    def __del__(self):
        Employee.__objectcount -= 1 #decrement count
        Employee.__emplist.remove(self.__name) #remove employee name upon deletion
        Employee.__totalsalary -= self.__salary


e = Employee("Abc", 50000)
e2 = Employee("Pqr", 20000)
print(e.get_salary())
Employee.sethraper(40)
print(e.get_salary())
print(Employee.get_objectcount())
print(Employee.get_emp_list())
del e
print(Employee.get_objectcount())
print(Employee.get_emp_list())