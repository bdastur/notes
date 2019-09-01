#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import asyncio

"""
* A function that you introduce with assync def is a coroutine.
  It may use await, return or yield, but all of these are optional.
  Declaring async def noop():  pass is valid.

* Using await and/or return creates a coroutine function. To call a
  coroutine function you must await it to get it's results.

* The keyword await passes function control back to the event loop.
   (It suspends the execution of the surrounding coroutine.) If Python
   encounters an await f() expression in the scope of g():
   It suspends execution of g() until the result of f() is returned.

"""



async def count():
    print("One")
    ret = await asyncio.sleep(2)
    print("After await ", ret)


async def count_async():
    print("Count async start")
    await asyncio.gather(count(), count(), count())
    print("Count async Done!")

def main():
    s = time.perf_counter()
    asyncio.run(count_async())
    elapsed_time = time.perf_counter() - s
    print("File %s executed in %f seconds" % ( __file__, elapsed_time))

if __name__ == "__main__":
    main()
