"""Tests for sum_of_two_integers problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def sum_of_two_integers():
    """Get the user's sum_of_two_integers implementation."""
    func = get_function("sum_of_two_integers")
    if func is None:
        pytest.skip("Function 'sum_of_two_integers' not registered. Run check(sum_of_two_integers) in notebook.")
    return func


class TestSumOfTwoIntegersBasic:
    """Basic functionality tests."""

    def test_positive_numbers(self, sum_of_two_integers):
        result = sum_of_two_integers(1, 2)
        assert result == 3

    def test_another_positive(self, sum_of_two_integers):
        result = sum_of_two_integers(2, 3)
        assert result == 5

    def test_zero_sum(self, sum_of_two_integers):
        result = sum_of_two_integers(-1, 1)
        assert result == 0

    def test_with_zero(self, sum_of_two_integers):
        result = sum_of_two_integers(0, 5)
        assert result == 5

    def test_both_zero(self, sum_of_two_integers):
        result = sum_of_two_integers(0, 0)
        assert result == 0


class TestSumOfTwoIntegersEdgeCases:
    """Edge case tests."""

    def test_negative_result(self, sum_of_two_integers):
        result = sum_of_two_integers(-5, 2)
        assert result == -3

    def test_both_negative(self, sum_of_two_integers):
        result = sum_of_two_integers(-3, -5)
        assert result == -8

    def test_larger_positive(self, sum_of_two_integers):
        result = sum_of_two_integers(100, 200)
        assert result == 300

    def test_larger_negative(self, sum_of_two_integers):
        result = sum_of_two_integers(-100, -200)
        assert result == -300

    def test_boundary_positive(self, sum_of_two_integers):
        result = sum_of_two_integers(1000, 0)
        assert result == 1000

    def test_boundary_negative(self, sum_of_two_integers):
        result = sum_of_two_integers(-1000, 0)
        assert result == -1000

    def test_mixed_large(self, sum_of_two_integers):
        result = sum_of_two_integers(500, -300)
        assert result == 200

    def test_near_boundary(self, sum_of_two_integers):
        result = sum_of_two_integers(999, 1)
        assert result == 1000
