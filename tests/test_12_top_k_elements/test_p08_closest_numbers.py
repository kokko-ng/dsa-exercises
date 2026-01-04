"""Tests for closest_numbers problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def closest_numbers():
    func = get_function("closest_numbers")
    if func is None:
        pytest.skip("Function 'closest_numbers' not registered.")
    return func


class TestClosestNumbersBasic:
    """Basic functionality tests."""

    def test_standard_case(self, closest_numbers):
        result = closest_numbers([1, 2, 3, 4, 5], 4, 3)
        assert result == [1, 2, 3, 4]

    def test_target_smaller_than_all(self, closest_numbers):
        result = closest_numbers([1, 2, 3, 4, 5], 4, -1)
        assert result == [1, 2, 3, 4]

    def test_target_larger_than_all(self, closest_numbers):
        result = closest_numbers([1, 2, 3, 4, 5], 4, 10)
        assert result == [2, 3, 4, 5]

    def test_target_in_array(self, closest_numbers):
        result = closest_numbers([1, 2, 3, 4, 5], 3, 3)
        assert result == [2, 3, 4]


class TestClosestNumbersEdgeCases:
    """Edge case tests."""

    def test_k_equals_length(self, closest_numbers):
        result = closest_numbers([1, 2, 3], 3, 2)
        assert result == [1, 2, 3]

    def test_k_equals_1(self, closest_numbers):
        result = closest_numbers([1, 2, 3, 4, 5], 1, 3)
        assert result == [3]

    def test_tie_breaking(self, closest_numbers):
        # When tied, prefer smaller element
        result = closest_numbers([1, 2, 3, 4, 5], 2, 3)
        # 2 and 4 are equidistant from 3, but prefer 2 (smaller)
        assert result == [2, 3]

    def test_negative_numbers(self, closest_numbers):
        result = closest_numbers([-5, -3, -1, 0, 2], 3, -2)
        assert result == [-3, -1, 0]


@pytest.mark.performance
class TestClosestNumbersPerformance:
    """Performance tests."""

    def test_large_input(self, closest_numbers):
        arr = list(range(100000))
        k = 100
        x = 50000

        start = time.time()
        result = closest_numbers(arr, k, x)
        elapsed = time.time() - start

        assert len(result) == k
        assert result == sorted(result)
        assert elapsed < 1.0
