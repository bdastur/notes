#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import pytest


@pytest.mark.valid
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.valid
def testsquare():
    num = 7
    assert 7 * 7 == 49

@pytest.mark.invalid
def equality_test():
    # This will not get executed.
    assert 10 == 11

@pytest.mark.invalid
def test_greater():
    assert 11 > 10
