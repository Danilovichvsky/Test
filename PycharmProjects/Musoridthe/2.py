class Some:
    def __init__(self,n):
        self.n = 0
        self.varify_n(n)


    def __add__(self, other):
        if isinstance(other,Some):
            return Some(self.n + other.n)
        if isinstance(other, int):
            return self.n + other

    def __radd__(self, other):
        return Some(other + self.n)

    def __getattribute__(self, item):
        print("__getattribute__")
        return object.__getattribute__(self,item)

    def varify_n(self,n):
        if type(n) not in (int,float):
            print("Datatype error")
        else:
            self.n = n

    def get_n(self):
        return self.n

    def set_n(self,value):
        self.n = value

    thnach = property(get_n,set_n)


obj = Some("3")
print(obj.n)