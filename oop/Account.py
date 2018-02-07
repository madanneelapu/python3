# Creating a class
class Account:
    def __init__(self, acno, holder, balance=0):  # initialization
        self.__acno = acno  # private instance variable/attribute
        self.__holder = holder
        self.__balance = balance

    def __str__(self):
        return "%d %s %f" % (self.__acno, self.__holder, self.__balance)

    def __eq__(self, other):
        return self.__acno == other.__acno

    def __gt__(self, other):
        return self.__balance > other.__balance

    # we have to return a new object. we must not change the obects which are ooperands.
    def __add__(self, other):
        return Account(self.__acno, self.__holder, self.__balance + other.__balance)

    def __del__(self):
        print("Object is being destroyed",self)

    def deposit(self, amount):
        self.__balance += int(amount)

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True

        return False

    def get_balance(self):
        return self.__balance

    def print(self):  # other method
        print(self.__acno, " ", self.__holder, " ", self.__balance)


a1 = Account(1, "Mr. James", 10000)  # creating an object
a1.print()  # calling a method

a2 = Account(2, "Mr. Jack")

a3 =  Account(1, "Mr. James", 10000)
a4 = a1

# a1._Account__balance = 25000 #accessing private variable, using cass mangling.
# a1.print()

a1.deposit(5000)
a1.print()

# print(a1.withdraw(8000))
# a1.print()

# print(a1.getBalance())

# calls str() method by passing a1 to it. which calls __str__  method. we can define it to print a string representation of an object.
print(a1)
print(str(a1))

#by default == operator compares references. we can overload == operator be defining __eq__ method
print(a1 == a2)
print(a1 == a3)
print(a1 == a4)

#!= calls the eq method and negates the result
print(a1 != a4)

# By default > operator is not supported. But we can define __gt__ method to overload > operator
print(a1 > a2)

# By default + operator is not supported. But we can define __add__ method to overload + operator.
print(a1 + a3)