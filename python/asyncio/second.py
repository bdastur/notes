#!/usr/bin/env python
# -*- coding: utf-8 -*-


import asyncio

async def nested():
    return 42

async def operation(factorial, number):
    factorial *= number
    await asyncio.sleep(1)
    return factorial

async def calculate_factorial(name, number):
    factorial = 1
    for i in range(2, number):
        print("Task %s: Compute factorial %i" % (name, i))
        #await asyncio.sleep(1)
        factorial = await(operation(factorial, i))
    print("Task: %s, Factorial: %i" % (name, factorial))
    return factorial

async def main():
    res= await asyncio.gather(
        calculate_factorial("A", 10),
        calculate_factorial("B", 3),
        calculate_factorial("C", 4)
    )
    print("Result: ", res)

asyncio.run(main())


# async def main():
#     # Schedule nested() to run soon concurrently
#     # with "main()".
#     task = asyncio.create_task(nested())

#     # "task" can now be used to cancel "nested()", or
#     # can simply be awaited to wait until it is complete:
#     print(await task)

# asyncio.run(main())



# async def main():
#     # Nothing happens if we just call "nested()".
#     # A coroutine object is created but not awaited,
#     # so it *won't run at all*.
#     # Also get a runtime warning. A coroutine was never awaited
#     nested()

#     # Let's do it differently now and await it:
#     print(await nested())  # will print "42".

# asyncio.run(main())