import time
import random
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


async def fetch_async(pid):
    start = time.time()
    sleepy_time = random.randint(2, 5)
    print(f'Fetch async process started {pid}, sleeping for {sleepy_time} seconds')
    await asyncio.sleep(sleepy_time)

    session = aiohttp.ClientSession()
    response = await session.get(URL)
    datetime = response.headers.get('Date')

    session.close()
    return f'Process {pid}: {datetime}, took: {time.time() - start:.2f} seconds'


async def asynchronous():
    start = time.time()
    futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
    for i, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        print(f'{">>" * (i + 1)} {result}')

    print(f"Process took: {time.time() - start:.2f} seconds")


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
