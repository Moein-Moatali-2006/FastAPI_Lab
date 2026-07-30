from threading import Thread, RLock


lock = RLock()

def one():
    with lock:
        print("One..!")

def two():
    with lock:
        one()
        print("Two..!")

def both():
    one()
    two()

t1 = Thread(target=both)
t1.start()
t1.join()
