import time
from multiprocessing import Pool

def add(a, b):
    return a + b

if __name__ == '__main__':
    t = time.time()
    with Pool(2) as pool:
        result = pool.apply(add, args=(5, 3))  # Передаем два аргумента
        print(result)  # Вывод: 8
    print("time:",time.time()-t)