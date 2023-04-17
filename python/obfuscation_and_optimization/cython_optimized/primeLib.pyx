#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Just contains a function that returns the nth prime number.
"""


cpdef getPrimeNumber(num):
    cdef int [100000] primes
    cdef int primeFound = 0
    cdef int number = 2
    cdef bint composite


    while primeFound < num:
        composite = False
        for i in range(primeFound+1):
            if primes[i] != 0 and number % primes[i] == 0:
                # Not a prime.
                composite = True
                break

        if not composite:
            primes[primeFound] = number 
            primeFound  = primeFound + 1

        number = number + 1

    print("Primefound: ", primeFound)
    return primes[primeFound-1]


