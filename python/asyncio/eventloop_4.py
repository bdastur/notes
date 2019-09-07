#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import time

async def my_coroutine():
    print("Start work")
    time.sleep(1)
    print("Task Done")
    loop1 = asyncio.get_running_loop()
    print("In coroutine: ", loop1)


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
        obj = asyncio.ensure_future(my_coroutine())
        print(type(obj))
        loop.run_forever()
        print("here")
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing loop")
        loop.close()


if __name__ == '__main__':
    run_forever()
