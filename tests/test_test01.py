#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_test01
----------------------------------

Tests for `test01` module.
"""

import unittest

import test01
import cli

class TestTest01(unittest.TestCase):

    def setUp(self):
        self.hello_message = "hello, Mehdi!"
        #pass

    def test_prints_hello_mehdi(self):
        output = cli.hello()
        assert(output == self.hello_message)

    def test_something(self):
        assert(test01.hello_world())
        pass

    def tearDown(self):
        pass
