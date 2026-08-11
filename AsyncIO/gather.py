import asyncio
import aiohttp

async def show_status(session, url):
    async with session.get(url) as result:
        return result.status

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://www.wikipediagrrq3gq35tg.org/', "https://fa.wikipedia.org/wiki/iran"]

        rqs = [show_status(session, url) for url in urls]

        status_codes = await asyncio.gather(*rqs, return_exceptions=True)
        print(status_codes)

asyncio.run(main())