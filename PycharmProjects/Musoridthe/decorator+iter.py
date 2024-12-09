import random
import time


def decorarot(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"total time is {end - start}")

    return wrapper


def some():
    # time.sleep(2)
    print("task is done")


some_func = decorarot(some)
some_func()

li = [1, 2, 3, 4, 5]

ter_li = iter(li)

print(ter_li.__next__())

print("-" * 50)

n = 4  # Количество строк
m = 5  # Количество столбцов

A = []  # Инициализация матрицы

# Заполнение матрицы случайными числами
for i in range(n):
    row = []  # Создаем новую строку
    for j in range(m):
        row.append(random.randint(1, 100))  # Генерируем случайное число от 1 до 100
    A.append(row)  # Добавляем строку в матрицу

# Печать матрицы
for row in A:
    print(row)

a = [1, 2, 3]
b = [4, 5, 6]

for x, y in zip(*[a, b]):
    print(x, y)

class myclass:
    def __init__(self, start, step, end):
        self.start = start
        self.step = step
        self.end = end
        self.val = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.val > self.end:  # Проверка перед увеличением
            raise StopIteration("end")
        current = self.val  # Сохраняем текущее значение
        self.val += self.step  # Увеличиваем значение
        return current  # Возвращаем сохраненное значение


obj = myclass(10, 2, 20)

a = iter(obj)
print(next(a))  # 10
print(next(a))  # 12
print(next(a))  # 14
print(next(a))  # 16
print(next(a))  # 18
print(next(a))  # 20





