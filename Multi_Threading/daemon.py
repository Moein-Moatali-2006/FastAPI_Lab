import time
from threading import Thread
import sys


start_time = time.perf_counter()

def show(name, delay):
    print(f"Starting {name}")
    time.sleep(delay)
    print(f"Finishing {name}")


t1 = Thread(target=show, args=("One", 5), daemon=True)
t2 = Thread(target=show, args=("Two", 3), daemon=False)

t1.start()
t2.start()

end_time = time.perf_counter()
print(f"Time: {round(end_time - start_time)}")
sys.exit()