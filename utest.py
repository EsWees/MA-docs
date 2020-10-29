#!/usr/bin/env python

import unittest


def not_true():
    return not True

class NotTrueTest(unittest.TestCase):
    """ Test not True and UnitTest """

    @classmethod
    def setUpClass(cls) -> None:
        print("======setUpClass======")

    @classmethod
    def tearDownClass(cls) -> None:
        print("======tearDown======")

    def setUp(self) -> None:
        """Hello world!"""
        pass
        #print("Start", self.shortDescription())

    def test_nonTrue(self):
        """Not True :D"""
        #not_true()
        self.assertFalse(not_true(), "True")

if __name__ == '__main__':
    unittest.main()