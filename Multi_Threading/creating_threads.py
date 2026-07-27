import time
from threading import Thread
import sys


start_time = time.perf_counter()

def show(name):
    print(f"Starting {name}")
    time.sleep(3)
    print(f"Finishing {name}")


t1 = Thread(target=show, args=("One", ))
t2 = Thread(target=show, args=("Two", ))

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.perf_counter()
print(f"Time: {round(end_time - start_time)}")
sys.exit()