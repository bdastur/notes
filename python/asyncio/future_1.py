#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://pymotw.com/3/asyncio/futures.html
'''

import asyncio
import time
import functools
#import gc
#gc.set_debug(gc.DEBUG_STATS)


def mark_done(future, result):
    print("Setting future result to ", result)
    future.set_result(result)


async def work_one(future):
    while True:
        print("Start One!")
        time.sleep(1)

        # A async sleep here passes the control back to the event loop.
        # without that, this coroutine will continue holding the context and
        # never let go.
        if future.done():
            print("We Have a future that is done")
        else:
            print("Future is not done yet")

        await asyncio.sleep(2)
        loop = asyncio.get_running_loop()
        print("One Done! Time: ", loop.time())
        loop.call_soon(mark_done, future, 'pass')
        print("After calling mark done")
        if future.done():
            print("We reached our state")

def callback(future, n):
    print("Future Done callback: ", future.result(), n)

def register_future_callback(future):
    print("Registering callbacks")
    future.add_done_callback(functools.partial(callback, n=44))
    future.add_done_callback(functools.partial(callback, n=102))

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
        all_done = asyncio.Future()
        register_future_callback(all_done)

        obj1 = asyncio.ensure_future(work_one(all_done))
        print("Time: ", loop.time())
        loop.run_forever()
        #result = loop.run_until_complete(all_done)
        #print("Result here ", result)
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing loop")
        loop.close()


if __name__ == '__main__':
    run_forever()
