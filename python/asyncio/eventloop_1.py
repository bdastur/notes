#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

async def my_coroutine():
    print("My coroutine")


# Run until complete.
def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(my_coroutine())
    finally:
        loop.close()


if __name__ == '__main__':
    main()
