import asyncio
import aiohttp

async def show_status(session, url, delay):
    asyncio.sleep(delay)
    async with session.get(url) as result:
        print(f"status for {url} is {result.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        requests = [show_status(session, 'https://www.mongard.ir/', 3),
                    show_status(session, 'https://www.mongard.ir/courses', 4),
                    show_status(session, 'https://www.mongard.ir/articles', 11),
                    show_status(session, 'https://www.mongard.ir/courses/linux', 9),
                    show_status(session, 'https://www.mongard.ir/', 1),]


        for rqs in asyncio.as_completed(requests):
            await rqs

asyncio.run(main())