import threading

shared_resource = []
condition = threading.Condition()

def consumer():
    with condition:
        while not shared_resource:
            print("Consumer is wating..!")
            condition.wait()
        item = shared_resource.pop(0)
        print(f"Consumer consumed item {item}")

def producer():
    with condition:
        item = "New item"
        shared_resource.append(item)
        print(f"Producer produced {item}")
        condition.notify()

con = threading.Thread(target=consumer).start()
pro = threading.Thread(target=producer).start()