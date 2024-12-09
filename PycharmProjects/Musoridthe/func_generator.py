
def gen():
    spis = [1,2,3,4,5,6,7,8,9,10]
    for _ in range(len(spis)):
        yield spis
        spis.pop(0)

def gen2():
    spis = [1,2,3,4,5,6,7,8,9,10]
    for i in range(len(spis)):
        yield spis[i:]



values = gen()
values2 = gen2()

for el in values:
    print(el)

for el2 in values2:
    print(el2)

a = list(range(1,10))
print(a)

"""
Создать генератор геометрической прогрессии.

При задании начала прогрессии -2 и шага прогрессии -5,

генератор выдаёт такую последовательность:
-2
10
-50
250
-1250
6250
"""

def geom_gen(start,step):
    res = start
    for _ in range(6):
        yield res
        res*=step



geom = geom_gen(-2,5)
for el in geom:
    print(el)