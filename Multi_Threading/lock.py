"""
    Race condition - Thread safe - Dead lock 
"""
from threading import Thread, Lock

x = 1 # shared resource 
lock = Lock()

def fibonaci(n):
    if n <= 2: return 1
    return fibonaci(n-1) + fibonaci(n-2)

def first_fibonaci():
    global x
    lock.acquire()
    print(f"first_fibonaci resource is {x} \n")
    while x <= 10:
        print(fibonaci(x))
        x += 1
    lock.release()

def secondt_fibonaci():
    global x
    with lock:
        print(f"second_fibonaci resource is {x} \n")
        while x <= 10:
            print(fibonaci(x))
            x += 1

t1 = Thread(target=fibonaci)
t2 = Thread(target=secondt_fibonaci)

t1.start()
t2.start()

t1.join()
t2.join()