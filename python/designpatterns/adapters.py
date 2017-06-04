#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Adapter pattern: An interfacing layer which allows two incompatible
pieces of code to communicate to each other.
'''


class Synthesizer(object):
    '''
    The class implements a play method
    to play a tune.
    '''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Synthesizer %s" % self.name

    def play(self):
        return "A nice tune!"


class Computer(object):
    '''
    The class implements an execute method to execute
    something.
    '''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Computer %s" % self.name

    def execute(self):
        return "A piece of code executed!"


class Adapter(object):
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    computer = Computer('Dell')
    synth = Synthesizer('Casio')
    objects = []
    objects.append(computer)
    objects.append(Adapter(synth,
                           dict(execute=synth.play)))

    for obj in objects:
        print "obj: ", str(obj)
        print "    run: ", obj.execute()


if __name__ == '__main__':
    main()
