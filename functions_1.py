# Functions
def add(a, b):
    return a + b


print(add(1, 2))
print(add("abc", "def"))


# Deafult Argument Values
def sum(a, b=10):
    return a + b


print(sum(20, 30))
print(sum(20))


def multiply(a=5, b=10):
    return a * b


print(multiply(10, 20))
print(multiply(25))
print(multiply())
# When accessed with name of the parameter, order doesn't matter
print(multiply(b=8, a=4))


# Non-Default parameter must not be used after default parameters.
# def myFn(a=5,b=10,c):
#    return a + b + c

#It is possible to return mutliple values at once from a function
def square_cube(a):
    return a ** 2, a ** 3


print(square_cube(4)) #returns a tuple
sq,cb = square_cube(4) #unpacking
print(sq,cb)