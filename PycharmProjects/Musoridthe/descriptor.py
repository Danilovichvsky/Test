class Descriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"instance: {instance}")
        print(f"owner: {owner}")
        print(self.name)
        return instance.__dict__[self.name]  # Возвращаем None, если ключ отсутствует

    def __set__(self, instance, value):
        if self.name == "c_desc":
            if value < 0:
                instance.__dict__["c_desc"] = value
            else:
                print("позитивні значення не допускаються")
                instance.__dict__["c_desc"] = None  # Устанавливаем значение по умолчанию
        else:
            if value > -1:
                instance.__dict__[self.name] = value
            else:
                print("значення не повинно бути з '-' ")
                instance.__dict__[self.name] = None  # Устанавливаем значение по умолчанию

class Some:
    n_desc = Descriptor()
    b_desc = Descriptor()
    c_desc = Descriptor()

    def __init__(self, n, b, c,v=None):
        self.n_desc = n
        self.b_desc = b
        self.c_desc = c


    def create_variable(self,v):
        self.v = v
        return v

# Создаем объект obg
obg = Some(4, -2, -4)
print(obg.b_desc)  # Должно вывести 2
print(obg.n_desc)  # Должно вывести 4

# Создаем объект obg2 с некорректным значением для c
obg2 = Some(4, 2, 5)
print(obg2.c_desc)  # Должно вывести None

obg2.create_variable(3)
print(obg2.v)
