#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import boto3
import botocore


class SQS(unittest.TestCase):
    def test_basic(self):
        print "basic"
        
