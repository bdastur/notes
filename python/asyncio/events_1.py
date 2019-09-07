#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://pymotw.com/3/asyncio/synchronization.html
'''
import asyncio

async def worker(event):
    while True:
        print("Worker started")
        await event.wait()
        print("Event triggered, do action")
        event.clear()

async def event_setter(event):
    while True:
        print("Event setter")
        await asyncio.sleep(2)
        event.set()


def main():
    event = asyncio.Event()
    loop = asyncio.get_event_loop()
    try:
        task1 = asyncio.ensure_future(worker(event))
        task2 = asyncio.ensure_future(event_setter(event))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing loop")
        loop.close()




if __name__ == '__main__':
    main()

