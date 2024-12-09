import copy
import random

# Генерация случайного списка
random_list_value = [random.randint(1, 1000) for _ in range(100)]

# Используем словарь для подсчёта частоты каждого элемента
duplicates = {}
for value in random_list_value:
    if value in duplicates:
        duplicates[value] += 1

    else:
        duplicates[value] = 1

print(duplicates)
# Отбираем только те элементы, которые встречаются более одного раза
d = [key for key, count in duplicates.items() if count > 1]

# Выводим список дубликатов
print("Дубликаты:", d)


