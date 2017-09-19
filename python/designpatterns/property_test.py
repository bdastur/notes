#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Celcius(object):
    def __init__(self, value):
        self.reading = value

    @property
    def reading(self):
        print "Getter invoked!"
        return self.__reading

    @reading.setter
    def reading(self, value):
        print "Setter, set %f value" % value
        self.__reading = value

    @reading.deleter
    def reading(self):
        print "Deleter"
        del self.__reading

    def convert_to_celcius(self):
        return (self.reading - 32)/1.8



def main():
    tempval = 100
    celcius = Celcius(tempval)
    print "%f converted to celcius %.2f" % \
        (tempval, celcius.convert_to_celcius())

    # Modify the reading.
    celcius.reading = 32
    print "%f converted to celcius %.2f" % \
        (celcius.reading, celcius.convert_to_celcius())


if __name__ == '__main__':
    main()
