#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Most basic example of click module usage.
"""
import click



@click.command()
def hello():
    """Hello Click."""
    print "Hello Click"



def main():
    print "Start main"
    hello()
    print "After hello"


if __name__ == '__main__':
    main()
