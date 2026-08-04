import asyncio
from asyncio import CancelledError, TimeoutError

async def one():
    await asyncio.sleep(7)
    print("Hello")


async def main():
    a = asyncio.create_task(one())

    # secs = 0
    # while not a.done():
    #     print("Task is not finished...")
    #     await asyncio.sleep(1)
    #     secs += 1
    #     if secs == 5:
    #         a.cancel()

    # try:
    #     await a
    # except CancelledError:
    #     print("Task canceled")

    try:
        await asyncio.wait_for(asyncio.shield(a), timeout=5)
    except TimeoutError:
        print("Task is longer than usual, but we are working on it")
        await a
        # print("Deadline reached")

    # print(f"was task cancelled? {a.cancelled()}")

asyncio.run(main())