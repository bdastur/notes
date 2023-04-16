#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Just contains a function that returns the nth prime number.
"""


def getPrimeNumber(num):
    primes = []
    primeFound = 0
    number = 2

    while primeFound < num:
        composite = False
        for x in primes:
            if number % x == 0:
                # Not a prime.
                composite = True
                break

        if not composite:
            primes.append(number)
            primeFound += 1

        number += 1
    
    return primes[-1]


