#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Generators Example
'''

import unittest


def generate_range(n):
    for i in range(n):
        yield i


def generate_update_range(n):
    i = 0
    while i < n:
        val = (yield i)
        #if value provided then change counter.
        if val is not None:
            i = val
        else:
            i += 1



class GeneratorUt(unittest.TestCase):
    def test_generate_range(self):
        gen = generate_range(3)
        for i in range(3):
            self.assertEqual(next(gen), i)

    def test_generate_update_range(self):
        gen = generate_update_range(9)
        self.assertEqual(next(gen), 0)
        self.assertEqual(next(gen), 1)
        gen.send(5)
        self.assertEqual(next(gen), 6)



def main():
    unittest.main()

if __name__ == '__main__':
    main()
