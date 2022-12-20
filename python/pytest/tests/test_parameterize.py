#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest

@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 35), (4, 44)])
def test_multiplication_11(num, output):
    assert 11*num == output

@pytest.mark.xfail
def test_failbutAllow_1():
    assert 1 == 3

@pytest.mark.xfail
def test_failbutAllow_2():
    assert len("test") == 2

@pytest.mark.skip
def test_skiptest():
    assert len("test") == 4
