#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Objects that you can loop over are called iterables.
An iterator must support a __next__() method.

'''

import unittest


class Yrange(object):
    '''
    A simple example of Iterator.
    __iter__() method returns self.
    '''
    def __init__(self, n):
        self.iterval = 0
        self.range = n

    def __iter__(self):
        '''
        An iterable object must define this __iter__ method.
        '''
        return self

    def next(self):
        if self.iterval < self.range:
            i = self.iterval
            self.iterval += 1
            return i
        else:
            raise StopIteration


class Yrange2(object):
    '''
    Another example of Iterator.
    Here the Yrange2 class invokes the Oddrange class's
    next method, and __iter__() returns the oddrange
    class object.

    The client initializes Yrange2, and depending on the
    type it will be able to instantiate the iterator
    for different purposes, like even iterator, odd iterator,
    prime, etc.
    '''
    def __init__(self, n, rangetype="odd"):
        self.iterval = 0
        self.range = n
        self.rangetype = rangetype
        if self.rangetype == "odd":
            self.rangeobj = Oddrange(n)

    def next(self):
        if self.rangetype == "odd":
            return self.rangeobj.next()

    def __iter__(self):
        return self.rangeobj


class Oddrange(object):
    def __init__(self, n):
        self.iterval = 1
        self.range = n

    def next(self):
        if self.iterval < self.range:
            i = self.iterval
            self.iterval += 2
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

    def test_yrange2(self):
        print "test yrange2"
        yrange2 = Yrange2(4, rangetype="odd")
        for i in range(1, 4, 2):
            self.assertEqual(yrange2.next(), (i))

        with self.assertRaises(StopIteration):
            yrange2.next()

        oddlist = list(Yrange2(4))
        self.assertEqual(oddlist, [1, 3])






def main():
    unittest.main()

if __name__ == '__main__':
    main()

