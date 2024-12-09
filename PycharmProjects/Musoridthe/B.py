class ListAdder:
    def __init__(self, start=[]):
        self.data = start

    def add(self, other):
        self.data.extend(other)
        return self.data


if __name__ == '__main__':
    x = ListAdder()
    x.add([1, 2])
    print(x.data)
    y = ListAdder()
    print(y.data)
