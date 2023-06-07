#!/usr/bin/python3
"""Test max_integer module"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class"""

    def test_one(self):
        """Tests one"""
        m = ('6-max_integer').__doc__
        self.assertTrue(len(m) >= 1)

    def test_two(self):
        """Test two"""
        m = max_integer.__doc__
        self.assertTrue(len(m) >= 1)

    def test_three(self):
        """a test
        """
        result = max_integer([10, 18, 13, 12])
        self.assertEqual(18, result)

    def test_four(self):
        """a test
        """
        result = max_integer([1, 4, 15, 3, 2, 15])
        self.assertEqual(15, result)

    def test_five(self):
        """a test
        """
        result = max_integer([])
        self.assertEqual(None, result)

    def test_six(self):
        """a test"""
        self.assertRaises(TypeError,
                          max_integer, 1, "2")

    def test_seven(self):
        """a test
        """
        self.assertRaises(TypeError,
                          max_integer, [1, 32], [23, 84])

    def test_eight(self):
        """a test
        """
        self.assertRaisesRegex(TypeError, "object of type *", max_integer, 81)


if __name__ == '__main__':
    unittest.main()
