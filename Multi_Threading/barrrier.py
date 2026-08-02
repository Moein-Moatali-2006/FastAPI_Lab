import threading
import time

def show(b):
    print(f"{threading.current_thread().name} is waiting..!")
    n = b.wait(timeout=5)
    print(f"{n} remaining..!")
    print("Hello user..!")

barrier = threading.Barrier(parties=3)

t1 = threading.Thread(target=show, args=(barrier, ))
t2 = threading.Thread(target=show, args=(barrier, ))
t3 = threading.Thread(target=show, args=(barrier, ))

t1.start()
t2.start()
t3.start()