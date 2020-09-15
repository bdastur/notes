#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import itertools as it
import os
import random
import time
#import uvloop

async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()


async def randsleep(a: int = 1, b: int = 5, caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print("%s sleeping for %d seconds" % (caller, i))
    await asyncio.sleep(i)


async def produce(name, q) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):
        await randsleep(caller="Producer %d" % name)
        print("producer-%d proceed to makeitem" % name)
        i = await makeitem()
        print("producer-%d after call to makeitem" % name)
        t = time.perf_counter()
        await q.put((i, t))
        print("Producer %d added %s to queue" % (name, str(i)))


async def consume(name: int, q: asyncio.Queue) -> None:
    while  True:
        await randsleep(caller="Consumer %d" % name)
        i, t = await q.get()
        now = time.perf_counter()
        print("Consumer %d got element %s in %f time" % (name, str(i), now-t))
        q.task_done()


async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    #loop = uvloop.new_event_loop()
    #loop = asyncio.new_event_loop()
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(**ns.__dict__))
    #asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print("Program completed in %0.5f seconds" % elapsed)




