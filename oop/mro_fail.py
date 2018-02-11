# fail case of python MRO based on C3 algorithm
class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D(A, C):
    pass


print(D.__mro__)
