#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import time

async def my_coroutine():
    print("Start work")
    time.sleep(1)
    print("Task Done")


# Run until complete.
def run_until_complete():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(my_coroutine())
    finally:
        loop.close()

def run_forever():
    loop1 = asyncio.get_event_loop()
    #loop1 = asyncio.new_event_loop()
    try:
        loop1.run_forever()
    finally:
        loop1.close()


if __name__ == '__main__':
    # This does not work. Once the even loop is closed it cannot be used
    # again.
    #   File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/base_events.py", line 480, in _check_closed
    #    raise RuntimeError('Event loop is closed')
    # RuntimeError: Event loop is closed

    run_until_complete()
    run_forever()
