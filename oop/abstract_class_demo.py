# abstract classes and methods
from abc import ABC, abstractmethod  # import the module ABC (Abstract Base Class)


class MyAbstractClass(ABC):  # extend ABC
    @abstractmethod  # decorate abstract methods
    def process(self):
        pass

    @abstractmethod
    def prepare(self):
        print("MyAbstractClass - prepare")  # abstract methods can have body


class MyConcreteClass(MyAbstractClass):
    def process(self):  # abstract method needs to be overriden. If not then an error is thrown
        print("MyConcreteClass - process")

    def prepare(self):
        super().prepare()  # invoking abstract method is super class
        print("MyConcreteClass - prepare")


obj = MyConcreteClass()
obj.process()
obj.prepare()
