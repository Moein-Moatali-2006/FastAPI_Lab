import asyncio


counter = 0 

async def increment(lock):
    global counter
    # await lock.acquire()
    async with lock:
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(0.01)
        counter = temp_counter
    # lock.release()

async def main():
    lock = asyncio.Lock()
    global counter
    tasks = [asyncio.create_task(increment(lock)) for _ in range(100)]
    await asyncio.gather(*tasks)
    print(f'Counter is {counter} ')

asyncio.run(main())