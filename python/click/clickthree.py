#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nesting commands, passing context.
http://click.pocoo.org/5/quickstart/#basic-concepts
"""
import click


@click.group()
@click.option('--number1', default=0, help="An integer number")
@click.option('--number2', default=0, help="An integer number")
@click.pass_context
def cli(ctx, number1, number2):
    """Math operations."""
    ctx.obj['NUMBER1'] = number1
    ctx.obj['NUMBER2'] = number2


@click.command()
@click.pass_context
def add(ctx):
    """Addition operation."""
    sum = int(ctx.obj['NUMBER1']) + int(ctx.obj['NUMBER2'])
    print "Add operation %s + %s = %d" % \
        (ctx.obj['NUMBER1'], ctx.obj['NUMBER2'], sum)


@click.command()
@click.pass_context
def sub(ctx):
    """Subtraction operation."""
    print "Subtract %s" % ctx.obj['NUMBER']


def main():
    cli.add_command(add)
    cli.add_command(sub)
    cli(obj={})



if __name__ == '__main__':
    main()
