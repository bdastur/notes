#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Using options and the click.echo() function.
http://click.pocoo.org/5/quickstart/#basic-concepts
"""
import click



@click.command()
@click.option('--name', default='Behzad', help='Name of user')
@click.option('--age', default=40, help="Age of user")
def hello(name, age):
    """Hello Click."""
    msg = "Hello %s, your age is %d" % (name, age)
    click.echo(msg)


def main():
    hello()


if __name__ == '__main__':
    main()
