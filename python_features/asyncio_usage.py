#!/bin/python3

import asyncio
import time


# There are three main types of awaitable objects:
# coroutines, Tasks, and Futures.

# The Future object was designed to mimic concurrent.futures.Future

async def coroutine(delay, what):
    await asyncio.sleep(delay)
    return what


# coroutine
async def main1():
    print(f"started at {time.strftime('%X')}")

    # serial, takes 3 sec
    print(await coroutine(1, 'result one'))
    print(await coroutine(2, 'result two'))

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main1())


# task (can be done with TaskGroup() as well)
async def main2():
    task1 = asyncio.create_task(coroutine(1, 'result one'))

    task2 = asyncio.create_task(coroutine(2, 'result two'))

    print(f"started at {time.strftime('%X')}")

    # parallel, takes 2 sec
    print(await task1)
    print(await task2)

    # immediate, since abowe we already awaited; if above skipped, takes 2 sec
    print(await asyncio.gather(task1, task2))

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main2())


# future
async def set_future(future, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)

    # Set *value* as a result of *future* Future.
    future.set_result(value)


async def main3():
    future = asyncio.Future()

    asyncio.create_task(set_future(future, 1, 'result future'))

    print(f"started at {time.strftime('%X')}")

    print('meanwhile ...')
    print(await future)

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main3())
