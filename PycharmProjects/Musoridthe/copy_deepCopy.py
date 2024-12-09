
import copy
di = {1:"vas",2:"dan",3:{1:"ivan",2:"zuba",3:{1:[1,2,3,4,5]}}}

di2 = copy.copy(di)
print(di2)
di2[3][1] = "changed"

print(di2)
print(di)
print(float(0.1+0.3))
print(di2.get(3))

print(di2[3][3][1])
di3 = di2
di3[1]="vas365"
print("di2=",di2)
print("di3",":",id(di3),"di2",":",id(di2))
print("-"*50)
for key,el in di2.items():
    if isinstance(el,dict):
        for key2,el2  in el.items():
            print(key2,"::",el2)
            if isinstance(el2, dict):
                for key3, el3 in el2.items():
                    print(key3, "::", el3)
                    el3[0] = 333


print("-"*50)
print(di)
print(di2)
print("-"*50)
def recursive_traverse(data):
    """Рекурсивно перебирает все элементы объекта."""
    if isinstance(data, dict):
        for key, value in data.items():
            print("  " f"{key} :: {value}")
            # Рекурсивно обрабатываем вложенные словари или списки
            recursive_traverse(value)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            print("  " f"[{index}] :: {item}")
            recursive_traverse(item)

# Используем функцию для перебора
print("-" * 50)
recursive_traverse(di2)
print("-" * 50)

values = ["apple","xiaomi","samsung","nokia"]
""" способ 1"""
dictionary_of_manuf = {}
id = 1
for el in values:
    manuf = 0
    dictionary_of_manuf[id] = values[manuf]
    id +=1
    manuf += 1

print(dictionary_of_manuf)
print("-" * 50)
""" способ 2"""
l = []
for ind,el in enumerate(values):
    l.append(ind+1)
print(dict(zip(l,values)))
print("-" * 50)

list_of_ranges = [(1,5),(2,4),(0,20)]

for start,stop in list_of_ranges:
    print(start,"and",stop)

import my_module

a,b = 10,4
my_module.func_sum(a,b)


