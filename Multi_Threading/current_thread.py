import time
from threading import Thread, active_count, current_thread, enumerate, main_thread
import sys


start_time = time.perf_counter()

def show(name):
    print(enumerate())
    print(active_count())
    print(main_thread())
    print(current_thread().name)
    print(f"Starting {name}")
    time.sleep(3)
    print(f"Finishing {name}")


t1 = Thread(target=show, args=("One", ), name="First")
t2 = Thread(target=show, args=("Two", ), name="Second")

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.perf_counter()
print(f"Time: {round(end_time - start_time)}")
sys.exit()