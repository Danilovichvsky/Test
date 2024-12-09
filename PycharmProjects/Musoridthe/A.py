import random
from itertools import count


class A:
    cl_name = []

    def __init__(self, name=[]):
        self.name = name

    @classmethod
    def add(cls, other):
        cls.cl_name.extend(other)
        return cls.cl_name


o = A([3,4,5])
o.add(["bulya",1])

o2 = A()
print(o2.add([2]))

def sum(a,b):
    res = a+b
    return res

print(sum)

class F(type):
    def summa(self):
        return 55 + 44

    def __init__(cls, name, bases, attrs):
        cls.__init__ = lambda self: print(cls.summa())

class S(metaclass=F):
    ...

o = S()

def modify_list(lst=[]):
    lst.append(4)  # Изменяем переданный список
    print("Внутри функции:", lst)

my_list = [1, 2, 3]
modify_list(my_list)
modify_list(my_list)
print("После вызова функции:", my_list)





