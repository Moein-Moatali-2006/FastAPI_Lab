import asyncio
import aiohttp
import logging


urls = [line.rstrip() for line in open("urls.txt")]

timeout = aiohttp.ClientTimeout(total=10)

logging.basicConfig(filename="logs.log", level=logging.INFO) 


async def check_url_health(url:str, semaphore, session):
        async with semaphore:
            try:
                response = await session.get(url)
                if not 200 <= response.status < 300:
                    logging.info(f"Status code for {url} was {response.status}..!")

                print(f"Status Code for {url} is {response.status}")
                print("*" * 64)

            except aiohttp.ClientError as client_e:
                logging.error(f"{url} --> {client_e}")
                print(f"{url} --> {client_e}")
            except asyncio.TimeoutError as timeout_e:
                logging.error(f"{url} --> {timeout_e}")
                print(f"{url} --> {timeout_e}")
            except Exception as e:
                logging.error(f"{url} --> {e}")
                print(f"{url} --> {e}")

async def main():
    print("Async URL Health Monitor")
    print("Service Started ⚡")
    print("_"*64)

    semaphore = asyncio.BoundedSemaphore(value=5)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        results = [check_url_health(url, semaphore, session) for url in urls]
        await asyncio.gather(*results)

    print("_"*64)
    print("Finished - check logs.log if you need.")

asyncio.run(main())