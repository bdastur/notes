#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import random
import time

async def worker(name, queue):
    print("Worker %s started" % name)
    while True:
        # Get a work item
        sleep_for = await queue.get()
        #await asyncio.sleep(sleep_for[1])


        queue.task_done()
        print("Worker %s, task done" % name)


async def main():
    task_queue = asyncio.PriorityQueue(20)

    total_sleep_time = 0
#    for _ in range(20):
#        sleep_for = random.uniform(1, 3)
#        total_sleep_time += sleep_for
#        task_queue.put_nowait((1, sleep_for))

    tasks = []
    for i in range(3):
        worker_name = "Worker-%i" % i
        task = asyncio.create_task(worker(worker_name, task_queue))
        tasks.append(task)


    for _ in range(20):                                                        
        sleep_for = random.uniform(2, 5)                                       
        total_sleep_time += sleep_for                                          
        task_queue.put_nowait((1, sleep_for))     
        await asyncio.sleep(1)

    # Wait until queue is fully processed
#    started_at = time.monotonic()
#    await task_queue.join()
#    total_slept_for = time.monotonic() - started_at
#    print("Total sleep time: %i, Total slept for: %i" % \
#        (total_sleep_time, total_slept_for))


    # Cancel our worker tasks.
#    for task in tasks:
#        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')

asyncio.run(main())

