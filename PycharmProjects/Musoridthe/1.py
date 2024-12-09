import asyncio
import time

str_ch = "1,2,3,4,5,6,7,8,9,10"
chet = []
nechet = []


for el in str_ch.split(","):
    if int(el) % 2 == 0:
        chet.append(el)
    else:
         nechet.append(el)
print("chet",chet)
print("nechet",nechet)

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
el = [el for key,el in my_dict.items()]
top_3 = sorted(el,reverse=True)
print(top_3[0:3])

async def f1():
    await asyncio.sleep(3)
    print("f1 is finished")

async def f2():
    await asyncio.sleep(2)
    print("f2 is finished")

async def m():
    await asyncio.gather(f1(), f2())
    print("all tasks are finished")
asyncio.run(m())


