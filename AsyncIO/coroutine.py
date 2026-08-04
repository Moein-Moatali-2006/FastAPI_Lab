import asyncio
import datetime


async def one(name):
    await asyncio.sleep(2)
    print(f"Hello {name}")

async def main():
    a = asyncio.create_task(one("Moein"))
    b = asyncio.create_task(one("Kevin"))

    await a
    await b



# print(type(one("Amir")))

print(datetime.datetime.now())
# asyncio.run(one("Moein"))
# asyncio.run(one("Kevin"))

asyncio.run(main())

print(datetime.datetime.now())
