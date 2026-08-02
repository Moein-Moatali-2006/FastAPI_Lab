import threading
import time

num = 0
# lock = threading.Semaphore(value=2)
lock = threading.BoundedSemaphore(value=2)

def add():
    global num
    lock.acquire()
    print(threading.current_thread().name)
    time.sleep(2)
    num += 1
    lock.release()
    # lock.release()

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=add)
t3 = threading.Thread(target=add)
t4 = threading.Thread(target=add)
t5 = threading.Thread(target=add)
t6 = threading.Thread(target=add)
t7 = threading.Thread(target=add)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()

print(num)
print("Done")