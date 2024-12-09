
class descr_chel:
    """def __set_name__(self, owner, name):
       self.name = name"""
    def __init__(self,name):
        self.name = name

    def __get__(self, instance, owner):
        if self.name in instance.__dict__:
            print(self.name)
            return instance.__dict__[self.name]

        else:
            print("non")

    def __set__(self, instance, value):
        if isinstance(value, str):  # Проверяем, что значение — строка
            if any(char.isdigit() for char in value):  # Проверяем, есть ли цифры
                raise ValueError("Строка не должна содержать цифры")
            instance.__dict__[self.name] = value
class chelovek:
    chel = descr_chel("chel2")


obj_chel = chelovek()
obj_chel.chel = "sanya"
print(obj_chel.chel)

