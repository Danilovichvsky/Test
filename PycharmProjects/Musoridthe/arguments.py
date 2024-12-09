"""
def some(l = []):
    l.append([1,2,3])
    print(l)

some()
some()

def some(l = 1):
    l = l+1
    print(l)

some()
some()
"""
import time

names = """Иванов Дмитро Иваніч, Славко Иван Санич ,'
         Зубенко василь сергеич, каманов илья викторич, мамасян сергей"""

def find_average_fio(names:str):
    ind_l = []
    k = 1
    for el in names.replace("\n"," ").split(","):
        k+=1
        ind_l.append(el)
    print(ind_l)
    print(len(ind_l)//2)
    avarage_name_ind = len(ind_l)//2
    print(ind_l[round(avarage_name_ind)])

    print("кількість ПІБ: ",k)



find_average_fio(names)

def sortirouka(l: list) -> list:
    n = len(l)
    for i in range(n):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:  # Сравниваем соседние элементы
                l[j], l[j + 1] = l[j + 1], l[j]  # Меняем их местами
    return l

# Данные для сортировки
data = list(range(-5, 1000))

# Замер времени для sortirouka
t_time = time.time()
res = sortirouka(data.copy())  # Используем .copy(), чтобы избежать изменений исходного списка
print("sortirouka result:", res)
print("sortirouka total time:", time.time() - t_time)

# Замер времени для встроенной функции sorted
t_time = time.time()
res = sorted(data)
print("sorted result:", res)
print("sorted total time:", time.time() - t_time)





