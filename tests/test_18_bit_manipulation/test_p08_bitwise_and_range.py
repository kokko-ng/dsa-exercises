"""Tests for bitwise_and_range problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def bitwise_and_range():
    """Get the user's bitwise_and_range implementation."""
    func = get_function("bitwise_and_range")
    if func is None:
        pytest.skip("Function 'bitwise_and_range' not registered. Run check(bitwise_and_range) in notebook.")
    return func


class TestBitwiseAndRangeBasic:
    """Basic functionality tests."""

    def test_example_5_to_7(self, bitwise_and_range):
        # 5 & 6 & 7 = 101 & 110 & 111 = 100 = 4
        result = bitwise_and_range(5, 7)
        assert result == 4

    def test_zero_to_zero(self, bitwise_and_range):
        result = bitwise_and_range(0, 0)
        assert result == 0

    def test_same_number(self, bitwise_and_range):
        result = bitwise_and_range(10, 10)
        assert result == 10

    def test_adjacent_numbers(self, bitwise_and_range):
        # 4 & 5 = 100 & 101 = 100 = 4
        result = bitwise_and_range(4, 5)
        assert result == 4


class TestBitwiseAndRangeEdgeCases:
    """Edge case tests."""

    def test_zero_to_one(self, bitwise_and_range):
        # 0 & 1 = 0
        result = bitwise_and_range(0, 1)
        assert result == 0

    def test_powers_of_two(self, bitwise_and_range):
        # 4 & 5 & 6 & 7 & 8 = 0 (crosses power of 2)
        result = bitwise_and_range(4, 8)
        assert result == 0

    def test_within_same_power(self, bitwise_and_range):
        # 12 to 15 = 1100 & 1101 & 1110 & 1111 = 1100 = 12
        result = bitwise_and_range(12, 15)
        assert result == 12

    def test_one_to_max(self, bitwise_and_range):
        result = bitwise_and_range(1, 2147483647)
        assert result == 0

    def test_large_range(self, bitwise_and_range):
        # Large range should return common prefix
        result = bitwise_and_range(1073741824, 1073741830)  # 2^30 to 2^30 + 6
        assert result == 1073741824


@pytest.mark.performance
class TestBitwiseAndRangePerformance:
    """Performance tests - require O(log n) solution."""

    def test_large_values(self, bitwise_and_range):
        left = 2147483640
        right = 2147483647

        start = time.time()
        result = bitwise_and_range(left, right)
        elapsed = time.time() - start

        assert result == 2147483640
        assert elapsed < 0.1, f"Solution too slow: {elapsed:.2f}s (should be < 0.1s)"
