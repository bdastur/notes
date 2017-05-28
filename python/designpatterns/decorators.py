#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Example of Decorator:

In this example we will override the default behavior of UnitTest to
ignore failures and execute all tests regardless of pass/fail. At the
end we will display a summary of test run with pass or fail status.
'''

import unittest


class UTReporter(object):
    '''
    The UT Report class keeps track of tests cases
    that have been executed.
    '''
    def __init__(self):
        self.testcases = []
        print "init called"

    def add_testcase(self, testcase):
        self.testcases.append(testcase)

    def display_report(self):
        for tc in self.testcases:
            msg = "=============================" + "\n" + \
                "Name: " + tc['name'] + "\n" + \
                "Description: " + str(tc['description']) + "\n" + \
                "Status: " + tc['status'] + "\n"
            print msg

reporter = UTReporter()


def assert_capture(*args, **kwargs):
    '''
    The Decorator defines the override behavior.
    unit test functions decorated with this decorator, will ignore
    the Unittest AssertionError. Instead they will log the test case
    to the UTReporter.
    '''
    def assert_decorator(func):
        def inner(*args, **kwargs):
            tc = {}
            tc['name'] = func.__name__
            tc['description'] = func.__doc__
            try:
                func(*args, **kwargs)
                tc['status'] = 'pass'
            except AssertionError:
                tc['status'] = 'fail'
            reporter.add_testcase(tc)
        return inner
    return assert_decorator



class DecorateUt(unittest.TestCase):

    @assert_capture()
    def test_basic(self):
        x = 5
        self.assertEqual(x, 4)

    @assert_capture()
    def test_basic_2(self):
        x = 4
        self.assertEqual(x, 4)


def main():
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(DecorateUt)
    unittest.TextTestRunner(verbosity=2).run(suite)

    reporter.display_report()



if __name__ == '__main__':
    main()
