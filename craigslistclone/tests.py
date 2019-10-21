from django.test import TestCase

import unittest


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        a = 1
        self.assertEqual(1, a)
    def test_2(self):
        b = 4
        a = 1
        self.assertFalse(a == b)