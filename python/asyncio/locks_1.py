#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import time

async def work_one(lock):
    while True:
        print("Start One!")
        time.sleep(1)

        # A async sleep here passes the control back to the event loop.
        # without that, this coroutine will continue holding the context and
        # never let go.
        await asyncio.sleep(2)
        loop = asyncio.get_running_loop()
        print("One Done! Time: ", loop.time())
        await access_file(lock, "One")


async def work_two(lock):
    while True:
        print("Start Two!")
        time.sleep(1)
        await asyncio.sleep(1)
        loop = asyncio.get_running_loop()
        print("Two Done! Time: ", loop.time())
        await access_file(lock, "Two")

async def access_file(lock, n):
    print("Wait to acquire lock: ", n)
    await lock.acquire()
    try:
        print("Access file information..", n)

    finally:
        print("Lock released")
        lock.release()
    print("Done writing to file.. ", n)


# Run until complete.
def run_forever():

    # Instead of get_event_loop, using
    # new event loop to create new one and setting it as current
    # event loop
    lock = asyncio.Lock()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    print("Loop: ", loop)
    try:
        # this function returns the obj which could be a future, a task 
        # a task object wrapping obj, if the obj is a coroutine.
        obj1 = asyncio.ensure_future(work_one(lock))
        obj2 = asyncio.ensure_future(work_two(lock))
        print("Time: ", loop.time())
        loop.run_forever()
        print("here")
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing loop")
        loop.close()


if __name__ == '__main__':
    run_forever()
