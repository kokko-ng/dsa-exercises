"""Tests for product_except_self problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def product_except_self():
    func = get_function("product_except_self")
    if func is None:
        pytest.skip("Function 'product_except_self' not registered.")
    return func


class TestProductExceptSelfBasic:
    def test_simple_case(self, product_except_self):
        assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_with_zero(self, product_except_self):
        assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    def test_two_elements(self, product_except_self):
        assert product_except_self([2, 3]) == [3, 2]


class TestProductExceptSelfEdgeCases:
    def test_with_ones(self, product_except_self):
        assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]

    def test_two_zeros(self, product_except_self):
        assert product_except_self([0, 0, 1]) == [0, 0, 0]

    def test_negative_numbers(self, product_except_self):
        assert product_except_self([-1, -2, -3]) == [6, 3, 2]

    def test_mixed_signs(self, product_except_self):
        assert product_except_self([-1, 2, -3, 4]) == [-24, 12, -8, 6]


@pytest.mark.performance
class TestProductExceptSelfPerformance:
    def test_large_input(self, product_except_self):
        n = 100000
        nums = [2] * n

        start = time.time()
        result = product_except_self(nums)
        elapsed = time.time() - start

        assert len(result) == n
        assert elapsed < 1.0
