import time
from concurrent.futures import ThreadPoolExecutor


start_time = time.perf_counter()

def show(name, delay):
    print(f"Starting {name}")
    time.sleep(delay)
    return f"Finishing {name}"


with ThreadPoolExecutor(max_workers=2) as executor:
    # results = executor.map(show, ["A", "B", "C"], [2, 3, 1])
    # for res in results:
    #     print(res)

    t1 = executor.submit(show, "A", 2)
    t2 = executor.submit(show, "B", 3)
    t3 = executor.submit(show, "C", 1)

    print(t1.result())
    print(t2.result())
    print(t3.result())

end_time = time.perf_counter()
print(f"Time: {round(end_time - start_time)}")
