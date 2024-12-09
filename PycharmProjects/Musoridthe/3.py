import random
from enum import Enum


class Players(Enum):
    danya = 1
    atret = 2
    __name = "Name"


obj = Players
print(Players.danya.value)
for names in Players:
    print(names)

import random

# Генерация списка случайных чисел
a = [random.randint(50, 1000) for _ in range(100)]


# Генератор
def print_a(a):
    for val in a:
        yield val


# Обычная функция
def print_a2(a):
    for val in a:
        return val  # Останавливается на первом элементе


# Сравнение работы генератора и обычной функции
print("Генератор:")
gen = print_a(a)
for el in gen:
    print(el, end=" , ")
print("")

print("Обычная функция:")
val2 = print_a2(a)  # Вернёт только первый элемент
print(val2)  # Просто печатаем результат, так как это не итерируемый объект

# Сравнение использования памяти
gen_memory = print_a(a).__sizeof__()
func_memory = a.__sizeof__()
print(f"Размер памяти (генератор): {gen_memory}")
print(f"Размер памяти (список): {func_memory}")
print(type(object))


class Something:
    __name = "dddd "


o = Something()
print(o._Something__name)

