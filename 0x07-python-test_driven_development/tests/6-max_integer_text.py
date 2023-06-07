#!/usr/bin/python3
"""Test max_integer module"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class"""

    def test_module_docstring(self):
        """Tests one"""
        m = ('6-max_integer').__doc__
        self.assertTrue(len(m) >= 1)

    def test_function_docstring(self):
        """Test two"""
        m = max_integer.__doc__
        self.assertTrue(len(m) >= 1)

    def test_max_integer(self):
        """correct test
        """
        result = max_integer([10, 18, 13, 12])
        self.assertEqual(18, result)

    def test_two_max_integers(self):
        """correct test
        """
        result = max_integer([1, 4, 15, 3, 2, 15])
        self.assertEqual(15, result)

    def test_list_is_empty(self):
        """List is empty
        """
        result = max_integer([])
        self.assertEqual(None, result)

    def test_list_param_contains_only_one_arg(self):
        """List has more"""
        self.assertRaises(TypeError,
                          max_integer, 1, "2ksdjkf")


    def test_not_supported(self):
        """List param not supported type
        """
        self.assertRaisesRegex(TypeError, "object of type *", max_integer, 1)


if __name__ == '__main__':
    unittest.main()
