import time
import threading


def worker_func(ev):
    print("Worker is wating for the main thread..!")
    ev.wait(timeout=7) # flag -> false
    print("Worker recived signal..!")

def main_func(ev):
    time.sleep(2)
    print(" main thread..!")
    ev.set()

e = threading.Event()

worker = threading.Thread(target=worker_func, args=(e, ))
main = threading.Thread(target=main_func, args=(e, ))
worker.start()
main.start()