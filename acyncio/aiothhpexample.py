import time
import urllib.request
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


def fetch_sycn(pid):
    print(f'Fetch sync process {pid} started')
    start = time.time()
    response = urllib.request.urlopen(URL)
    datetime = response.getheader('Date')

    print(f'Process {pid}: {datetime}, took: {time.time() - start:.2f} seconds')

    return datetime


async def fetch_async(pid):
    print('Fetch async process {} started'.format(pid))
    start = time.time()
    session = aiohttp.ClientSession()
    response = await session.get(URL)
    datetime = response.headers.get('Date')

    print(f'Process {pid}: {datetime}, took: {time.time() - start:.2f} seconds')

    session.close()
    return datetime


def synchronous():
    start = time.time()
    for i in range(1, MAX_CLIENTS + 1):
        fetch_sycn(i)
    print(f'Process took: {time.time() - start:.2f} seconds')


async def asynchronous():
    start = time.time()
    tasks = [asyncio.ensure_future(
        fetch_async(i)) for i in range(1, MAX_CLIENTS + 1)]
    await asyncio.wait(tasks)
    print(f"Process took: {time.time() - start:.2f} seconds")


print('Synchronous:')
synchronous()

print('Asynchronous:')
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
