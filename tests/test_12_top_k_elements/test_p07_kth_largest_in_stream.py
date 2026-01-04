"""Tests for kth_largest_in_stream problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def kth_largest_in_stream():
    func = get_function("kth_largest_in_stream")
    if func is None:
        pytest.skip("Function 'kth_largest_in_stream' not registered.")
    return func


class TestKthLargestInStreamBasic:
    """Basic functionality tests."""

    def test_standard_case(self, kth_largest_in_stream):
        result = kth_largest_in_stream(3, [4, 5, 8, 2], [3, 5, 10, 9, 4])
        assert result == [4, 5, 5, 8, 8]

    def test_k_equals_1(self, kth_largest_in_stream):
        result = kth_largest_in_stream(1, [1, 2, 3], [4, 5])
        assert result == [4, 5]

    def test_increasing_stream(self, kth_largest_in_stream):
        result = kth_largest_in_stream(2, [1, 2], [3, 4, 5])
        assert result == [2, 3, 4]


class TestKthLargestInStreamEdgeCases:
    """Edge case tests."""

    def test_empty_initial(self, kth_largest_in_stream):
        result = kth_largest_in_stream(1, [], [1, 2, 3])
        assert result == [1, 2, 3]

    def test_same_values(self, kth_largest_in_stream):
        result = kth_largest_in_stream(2, [5, 5], [5, 5])
        assert result == [5, 5]

    def test_negative_numbers(self, kth_largest_in_stream):
        result = kth_largest_in_stream(2, [-5, -10], [-3, -1])
        assert result == [-5, -3]


@pytest.mark.performance
class TestKthLargestInStreamPerformance:
    """Performance tests."""

    def test_large_stream(self, kth_largest_in_stream):
        k = 100
        initial = list(range(1000))
        operations = list(range(1000, 10000))

        start = time.time()
        result = kth_largest_in_stream(k, initial, operations)
        elapsed = time.time() - start

        assert len(result) == len(operations)
        assert elapsed < 1.0
