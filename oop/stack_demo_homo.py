# making the stack Homogeneous
class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("Stack is Empty!")


class Stack:

    def __init__(self):
        self.__data = []
        self.__type_of_stack = None

    def push(self, value):
        if self.__type_of_stack is None:
            self.__type_of_stack = type(value)

        if isinstance(value, self.__type_of_stack):
            self.__data.append(value)
        else:
            raise ValueError("not allowed!")

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
s.push("abc")

