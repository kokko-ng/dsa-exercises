"""Tests for rotation_count problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def rotation_count():
    func = get_function("rotation_count")
    if func is None:
        pytest.skip("Function 'rotation_count' not registered.")
    return func


class TestRotationCountBasic:
    """Basic functionality tests."""

    def test_rotated_twice(self, rotation_count):
        assert rotation_count([10, 15, 1, 3, 8]) == 2

    def test_rotated_five_times(self, rotation_count):
        assert rotation_count([4, 5, 7, 9, 10, -1, 2]) == 5

    def test_not_rotated(self, rotation_count):
        assert rotation_count([1, 3, 8, 10]) == 0

    def test_rotated_once(self, rotation_count):
        assert rotation_count([5, 1, 2, 3, 4]) == 1


class TestRotationCountEdgeCases:
    """Edge case tests."""

    def test_single_element(self, rotation_count):
        assert rotation_count([1]) == 0

    def test_two_elements_not_rotated(self, rotation_count):
        assert rotation_count([1, 2]) == 0

    def test_two_elements_rotated(self, rotation_count):
        assert rotation_count([2, 1]) == 1

    def test_fully_rotated(self, rotation_count):
        # Rotated n times = same as 0 rotations
        # But minimum is still at index 0
        assert rotation_count([1, 2, 3, 4, 5]) == 0

    def test_rotated_n_minus_1(self, rotation_count):
        assert rotation_count([2, 3, 4, 5, 1]) == 4

    def test_negative_numbers(self, rotation_count):
        assert rotation_count([0, 1, 2, -5, -4, -3, -2, -1]) == 3


@pytest.mark.performance
class TestRotationCountPerformance:
    """Performance tests - require O(log n) solution."""

    def test_large_input(self, rotation_count):
        n = 1000000
        pivot = n // 3
        nums = list(range(pivot, n)) + list(range(pivot))

        start = time.time()
        result = rotation_count(nums)
        elapsed = time.time() - start

        assert result == n - pivot
        assert elapsed < 0.1, f"Solution too slow: {elapsed:.3f}s"
