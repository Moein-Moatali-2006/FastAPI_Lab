import asyncio
import aiohttp


async def cheek_url_health(url:str):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        print("*" * 64)
        print(f"Status Code for {url} is {response.status}")
        print("*" * 64)

async def main():
    t1 = asyncio.create_task(cheek_url_health("https://github.com"))
    await t1

asyncio.run(main())