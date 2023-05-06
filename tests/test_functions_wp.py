from functions import *
from unittest.mock import patch


def test_suma():
    assert suma(5, 4) == 9
    assert suma(5, 2) == 7


def test_diff():
    assert diff(5, 4) in [2, 3, 4, 1]
    assert diff(2, 4) == -2


@patch("functions.rand", return_value=5)
def test_suma_with_rand(rand_mock):
    assert suma_with_rand(5, 4) == 14
    assert rand_mock.called
