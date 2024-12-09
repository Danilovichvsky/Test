import threading
import time

# Семафор позволяет только 2 потокам одновременно работать
semaphore = threading.Semaphore(2)

def worker(name):
    print(f"{name} пытается получить доступ к ресурсу")
    semaphore.acquire()
    print(f"{name} получил доступ к ресурсу")
    time.sleep(2)  # Симуляция работы с ресурсом
    print(f"{name} освобождает ресурс")
    semaphore.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(f"Поток-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
