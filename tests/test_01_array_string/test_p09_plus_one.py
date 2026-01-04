"""Tests for plus_one problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def plus_one():
    func = get_function("plus_one")
    if func is None:
        pytest.skip("Function 'plus_one' not registered.")
    return func


class TestPlusOneBasic:
    def test_simple_increment(self, plus_one):
        assert plus_one([1, 2, 3]) == [1, 2, 4]

    def test_carry_over(self, plus_one):
        assert plus_one([1, 2, 9]) == [1, 3, 0]

    def test_single_digit(self, plus_one):
        assert plus_one([5]) == [6]


class TestPlusOneEdgeCases:
    def test_all_nines(self, plus_one):
        assert plus_one([9, 9, 9]) == [1, 0, 0, 0]

    def test_single_nine(self, plus_one):
        assert plus_one([9]) == [1, 0]

    def test_zero(self, plus_one):
        assert plus_one([0]) == [1]

    def test_multiple_carries(self, plus_one):
        assert plus_one([1, 9, 9, 9]) == [2, 0, 0, 0]

    def test_large_number(self, plus_one):
        assert plus_one([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
