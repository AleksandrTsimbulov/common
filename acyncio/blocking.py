import asyncio
import time


start = time.time()


def tic():
    return f'at {time.time() - start:1.1f} seconds'


async def gr1():
    # Busy waits for a second, but we don't want to strick around...
    print(f'gr1 started work: {tic()}')
    await asyncio.sleep(2)
    print(f'gr1 ended work: {tic()}')


async def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print(f'gr2 started work: {tic()}')
    await asyncio.sleep(2)
    print(f'gr2 Ended work: {tic()}')


async def gr3():
    print(f"Let's do some stuff while the coroutines are blocked, {tic()}")
    await asyncio.sleep(1)
    print(f"Done!")


ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(gr1()),
    ioloop.create_task(gr2()),
    ioloop.create_task(gr3())
]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()
