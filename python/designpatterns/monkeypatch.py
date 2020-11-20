#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


class A(object):
    def simple_print(self):
        print("Function simple_print!")

class AMock(object):
    def mocked_print(self):
        print("Printing Mocked")

class B(object):
    def __init__(self, aobj):
        self.a = aobj
    
    def print_b(self):
        current_frame = sys._getframe(0)
        import pdb; pdb.set_trace()
        self.a.simple_print()



def main():
    aobj = A()
    aobj.simple_print()

    bobj = B(aobj)
    bobj.print_b()

    mock_obj = AMock()
    aobj.simple_print = mock_obj.mocked_print

    print("Simple print:", aobj.simple_print)

    newobj = B(aobj)
    newobj.print_b()




if __name__ == "__main__":
    main() 
