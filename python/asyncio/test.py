#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import unittest
import conditions



class TestAsync(unittest.TestCase):
    def test_basic(self):
        print("Test Basic")
        loop = asyncio.get_event_loop()
        try:
            result = loop.run_until_complete(conditions.main(loop))
        finally:
            loop.close()
