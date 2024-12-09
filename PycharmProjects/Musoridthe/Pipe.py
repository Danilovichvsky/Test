import multiprocessing
from multiprocessing import Pipe

def send_message(canal:Pipe,message:str)-> str:
    canal.send(str(message))

def get_message(canal:Pipe):
    print(canal.recv())
    return canal.recv()


if __name__ == "__main__":

    canal_send,canal_get = Pipe()
    a = multiprocessing.Process(target=send_message, args=(canal_send,"hello",))
    b = multiprocessing.Process(target=get_message, args=(canal_get,))
    a.start()
    b.start()
