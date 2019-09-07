#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://pymotw.com/3/asyncio/synchronization.html
'''

import asyncio

async def worker(condition, n):
    print("Worker ", n)
    async with condition:
        print("worker is waiting ", n)
        await condition.wait()

    print("Worker %d ending" % n)


async def manipulate_condition(condition):
    print("Manipulate condition")
    await asyncio.sleep(1)
    for i in range(1, 3):
        async with condition:
            condition.notify(n=i)
        await asyncio.sleep(1)

    async with condition:
        condition.notify_all()

    print("Ending manipulate condition")


async def main(loop):
    condition = asyncio.Condition()
    workers = [ worker(condition, i) for i in range(5)]
 
    loop.create_task(manipulate_condition(condition)) 
    await asyncio.wait(workers)
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(main(loop))
    finally:
        loop.close()
