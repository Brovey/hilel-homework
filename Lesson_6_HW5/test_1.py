import unittest
from exercise1 import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """simple unit test checking None return"""
    def testing(self):
        self.assertIsNotNone(fizz_buzz(1, 100), "should not be None")


