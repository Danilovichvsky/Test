import time
import asyncio

a = []


async def v():
    for el in range(1000):
        a.append(el)

    start = time.time()
    await asyncio.sleep(5)
    end = time.time()
    print("time spent:", end - start)

    print(a[-1:])


async def v2():
    for el in range(1000):
        a.append(el)
    start = time.time()
    await asyncio.sleep(2)
    end = time.time()
    print("time spent:", end - start)

    print(a[-1:])

async def v3():
    for el in range(1000):
        a.append(el)
    start = time.time()
    await asyncio.sleep(3)
    end = time.time()
    print("time spent:", end - start)

    print(a[-1:])


async def main():
    task1 = asyncio.create_task(v())
    task2 = asyncio.create_task(v2())
    task3 = asyncio.create_task(v3())

    await task2
    await task1
    await task3




start_time = time.time()
asyncio.run(main())
print(f"total time:{start_time - time.time()} ")
