#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Class Decorators.
Pretty useless example at the moment, just to illustrate the concept.
'''


def decorate(cls):
    # Instead of the inner function we use a wrapper class
    # to wrap the decoreated class over.
    class WrapperClass(object):
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print "Getting the %s of %s" % (name, self.wrapped)
            return getattr(self.wrapped, name)

    return WrapperClass



@decorate
class Decorate(object):
    def __init__(self, *args, **kwargs):
        print "args: %s, kwargs: %s" % (args, kwargs)
        self.args = args
        print "self args: ", args



def main():
    dec = Decorate(5, 4)
    print dec.args

if __name__ == '__main__':
    main()

