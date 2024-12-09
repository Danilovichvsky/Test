import pprint
def func_sum(a,b):
    print(a+b)
    return a+b

def func_sub(a,b):
    print(a-b)
    return a-b



# Пример вложенного словаря
data = {
    'name': 'John',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'New York',
        'zipcode': '10001'
    },
    'phones': ['123-456-7890', '987-654-3210']
}

# Использование pprint для красивого вывода вложенных данных
pprint.pprint(data,depth=3)
print(list(data["address"]))
values_of_address = [values for key,values in data["address"].items()]
print(','.join(values_of_address))
