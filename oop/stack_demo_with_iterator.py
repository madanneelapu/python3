# making the stack iterable
class Stack:

    def __init__(self):
        self.__data = []

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        return self.__data.pop()

    @property
    def length(self):
        return len(self.__data)

    def __iter__(self):  # method that will be first called when we try to iterate over the object of stack.
        self.pos = len(self.__data)
        return self  # should return an/any object that has __next__ method defined in it

    def __next__(self):  # method that will be called for every iteration
        if self.pos == 0:
            raise StopIteration  # notifies to stops the iteration
        else:
            self.pos -= 1  # update the position
            return self.__data[self.pos]  # Return  the value


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

for n in s:
    print(n)

# we are not modifying the stack. we can check that by reprinting the stack

for n in s:
    print(n)
