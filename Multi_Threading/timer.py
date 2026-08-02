import threading
import time


def greetings(name):
    print(f"Heelo {name}")


timer = threading.Timer(10, greetings, args=("Moein", ))
timer.start()
print("Timer started..!")
time.sleep(4)
timer.cancel()
print("Canceld")
