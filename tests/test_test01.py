#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_test01
----------------------------------

Tests for `test01` module.
"""

import unittest

import test01


class TestTest01(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(test01.hello_world())
        pass

    def tearDown(self):
        pass
