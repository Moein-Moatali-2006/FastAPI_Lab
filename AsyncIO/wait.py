import asyncio 
import aiohttp


async def show_satus(session, url):
    async with session.get(url) as result:
        return f"status for {url} is {result.status}"

async def main():
    async with aiohttp.ClientSession() as session:
        requests = [asyncio.create_task(show_satus(session, "https://mongard.ir")),
                    asyncio.create_task(show_satus(session, "https://mongard.ir/courses"))]

        done, pending = await asyncio.wait(requests, return_when=asyncio.FIRST_EXCEPTION)
        print(f"Done--> {done}")
        print(f"Pending--> {pending}")

        for d in done:
            # print(d.result())
            # print(await d)

            if d.exception() is None:
                print(d.result())
            else:
                print("Error")

        for p in pending:
            p.cancel()


asyncio.run(main())