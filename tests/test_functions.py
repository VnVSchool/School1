import unittest
from unittest.mock import patch
from functions import *


class TestFunctions(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5, 4), 9)
        self.assertEqual(suma(4, 3), 7)

    def test_diff(self):
        self.assertEqual(diff(6, 4), 2)
        self.assertEqual(diff(6, 2), 4)
        self.assertEqual(diff(6, 9), -3)

    def test_div(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)
        self.assertEqual(div(6, 2), 3)

    def test_mn(self):
        self.assertEqual(mn(5, 4), 20)
        self.assertEqual(mn(4, 4), 16)

    def test_suma_with_rand(self):
        with patch("functions.rand", return_value=5) as rand_mock:
            self.assertEqual(suma_with_rand(5, 4), 14)
            self.assertEqual(rand_mock.called, True)
