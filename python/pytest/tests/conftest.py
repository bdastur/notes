#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

@pytest.fixture
def inputString():
    value = "This is a test"
    return value
