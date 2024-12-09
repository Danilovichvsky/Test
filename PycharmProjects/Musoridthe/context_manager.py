fp = None

try:
    with open("l.txt",encoding="utf-8") as f:
        for t in f:
            print(t)
except Exception as e:
    print(e)

print("-"*50)

import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")


# Пример использования контекстного менеджера
with Timer() as timer:
    # Ваш блок кода
    time.sleep(2)



x=1
y=0
res = None
try:
    x = x/y

except:
    print("zero by division")

print(x)

a = [1,2,3]
b = [1,2]
try:
    for ind, el in enumerate(a):
        a[ind] +=b[ind]

except:
    print("error")

print(a)
