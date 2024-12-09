class Players:
    __name = "Bulya"

    def get_name(self):
        print(self.__name)


class second(Players):
    __slots__ = ('x','y')

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.z=50

    def get_name(self):
        print(self.__name)


obj = Players()
obj.get_name()

print("-"*50,end=" ")
print("BULYA",end=" ")
print("-"*50)
obj2 = second(3,4)
print(obj2.x)
print(obj2.__slots__)
