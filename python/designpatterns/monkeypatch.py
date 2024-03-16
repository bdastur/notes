#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


class A(object):
    def simple_print(self, value="A"):
        print("Function simple_print! %s" % value)

class MockA(object):
    def mocked_print(self, value="MockedA"):
        print("Printing Mocked %s " % value)

class B(object):
    def __init__(self, aobj):
        self.a = aobj
    
    def print_b(self):
        current_frame = sys._getframe(0)
        self.a.simple_print(value="B")


def withoutMock():
    objA = A()
    objA.simple_print()

    objB = B(objA)
    objB.print_b()

def mockPrint():
    objA = A()
    mockA = MockA()
    objA.simple_print = mockA.mocked_print

    objB = B(objA)
    objB.print_b()


def main():
    withoutMock()
    print("---- mocked ---")
    mockPrint()





if __name__ == "__main__":
    main() 
