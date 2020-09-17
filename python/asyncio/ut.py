#!/usr/bin/env python
# -*- coding: utf-8 -*-


import asyncio
import unittest
import blocking_2

class AsyncUt(unittest.TestCase):
    def test_async_coroutine(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(blocking_2.non_blocking_one_two())
