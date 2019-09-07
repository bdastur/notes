#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import time
#import gc
#gc.set_debug(gc.DEBUG_STATS)

def fastcall(*args):
    print("Callback invoked with args: ", *args)


def slowcall(*args):
    print("Slow callback invoked with argss: ", *args)


async def work_one():
    while True:
        print("Start One!")
        time.sleep(1)

        # A async sleep here passes the control back to the event loop.
        # without that, this coroutine will continue holding the context and
        # never let go.
        await asyncio.sleep(2)
        loop = asyncio.get_running_loop()
        print("One Done! Time: ", loop.time())
        loop.call_soon(fastcall, 1, 434, "test")
        print("One after callback")

async def work_two():
    while True:
        print("Start Two!")
        time.sleep(1)
        await asyncio.sleep(1)
        loop = asyncio.get_running_loop()
        print("Two Done! Time: ", loop.time())
        loop.call_later(10, slowcall, 4, "slow call", 434)
        print("Two after callback")

        # Using call_at.
        call_time = loop.time() + 5
        loop.call_at(call_time, slowcall, "Call at", 4442)
        print("Two after call_at()")


# Run until complete.
def run_forever():

    # Instead of get_event_loop, using
    # new event loop to create new one and setting it as current
    # event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    print("Loop: ", loop)
    try:
        # this function returns the obj which could be a future, a task 
        # a task object wrapping obj, if the obj is a coroutine.
        obj1 = asyncio.ensure_future(work_one())
        obj2 = asyncio.ensure_future(work_two())
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
