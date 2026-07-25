import time
from threading import Thread


start_time = time.perf_counter()

def show(name, delay):
    print(f"Starting {name}")
    time.sleep(delay)
    print(f"Finishing {name}")

class ShowThread(Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)

t1 = ShowThread("One", 5)
t2 = ShowThread("Two", 3)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.perf_counter()
print(f"Time: {round(end_time - start_time)}")