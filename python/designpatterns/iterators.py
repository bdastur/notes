#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Objects that you can loop over are called iterables.
An iterator must support a __next__() method.

'''

import unittest


class Yrange(object):
    def __init__(self, n):
        self.iterval = 0
        self.range = n

    def __iter__(self):
        '''
        An iterable object must define this __iter__ method.
        '''
        return self

    def next(self):
        if self.iterval < self.range
            i = self.iterval
            self.iterval += 1
            return i
        else:
            raise StopIteration


class Itertest(unittest.TestCase):
    def test_yrange(self):
        print "test yrange"
        yrange = Yrange(4)
        for i in range(4):
            self.assertEqual(yrange.next(), i)

        # Iterator raises StopIteration, when runs out of range.
        with self.assertRaises(StopIteration):
            yrange.next()

        list(Yrange(4))



def main():
    unittest.main()

if __name__ == '__main__':
    main()

