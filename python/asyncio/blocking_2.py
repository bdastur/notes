#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import time
import random
import concurrent.futures

def blocking_operation_one(id, queue):
    print("Blocking operation one ", id)
    time.sleep(5)
    rand_val = random.randint(1, 233)
    result = {
        "id": id,
        "randval": rand_val
    }
    print("put result %s to queue " % result)
    queue.put_nowait(result)
    print("Blocking operation one done", id)

def blocking_operation_two(id, queue):
    print("Blocking operation two ", id)
    time.sleep(5)
    rand_val = random.randint(1, 233)
    result = {
        "id": id,
        "randval": rand_val
    }
    print("put result %s to queue " % result)
    queue.put_nowait(result)
    print("Blocking operation two done", id)


async def non_blocking_one_two():
    print("Non Blocking one two")

    loop = asyncio.get_running_loop()
    executor =  None
    one_queue = asyncio.Queue(maxsize=1)
    two_queue = asyncio.Queue(maxsize=1)
    loop.run_in_executor(None, blocking_operation_one, 1, one_queue)
    loop.run_in_executor(None, blocking_operation_two, 2, two_queue)

    print("Non Blocking one two - waiting for data")
    one_data = await one_queue.get()
    two_data = await two_queue.get()

    print("One data: ", one_data)
    print("Two data: ", two_data)

    print("Non Blocking one two done")






if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(non_blocking_one_two())
