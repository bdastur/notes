#!/usr/bin/env python3

import pytest


#@pytest.fixture
#def inputString():
#    return "This is a test string"


def test_reverseString(inputString):
    reverseString = inputString[::-1]
    print(reverseString)
    assert len(reverseString) == len(inputString)
