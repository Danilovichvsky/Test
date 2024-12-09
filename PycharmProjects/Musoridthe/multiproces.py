import multiprocessing
import time
from multiprocessing import *
def worker(iterations,kp):
    #print(f"starting with {kp}")
    for i in range(iterations):
        print(i)
    #print(f"ending with {kp}")


if __name__ == '__main__':
    l = []
    locker = Lock()
    s_time = time.time()
    for _ in range(2):
        #time.sleep(2)

        proc = multiprocessing.Process(target=worker,args=(2,_,))
        proc.start()
        l.append(proc)
        #proc.join()


    for p in l:
        p.join()
    print("time: 2f",time.time()-s_time)
    print(multiprocessing.cpu_count())

    print("FINISH!!!")

