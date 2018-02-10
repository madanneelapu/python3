# custom exception example. Create a stack like Data structure using a list.
class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("Stack is Empty!")


class Stack:
    def __init__(self):
        self.__data = []

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop()
        else:
            raise EmptyStackError()

    @property
    def length(self):
        return len(self.__data)


s = Stack()
s.push(10)
s.push(20)
print(s.length)

print(s.pop())
print(s.pop())
print(s.pop())  # might throw an error if list is empty. So we create a custom exception class and throw an error.
