"""Tests for maximum_distinct_elements problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def maximum_distinct_elements():
    func = get_function("maximum_distinct_elements")
    if func is None:
        pytest.skip("Function 'maximum_distinct_elements' not registered.")
    return func


class TestMaximumDistinctElementsBasic:
    """Basic functionality tests."""

    def test_remove_duplicate(self, maximum_distinct_elements):
        assert maximum_distinct_elements([5, 5, 4], 1) == 2

    def test_multiple_removals(self, maximum_distinct_elements):
        assert maximum_distinct_elements([4, 3, 1, 1, 3, 3, 2], 3) == 3

    def test_k_zero(self, maximum_distinct_elements):
        assert maximum_distinct_elements([1, 2, 3, 4], 0) == 4


class TestMaximumDistinctElementsEdgeCases:
    """Edge case tests."""

    def test_all_same(self, maximum_distinct_elements):
        assert maximum_distinct_elements([5, 5, 5, 5], 2) == 1
        assert maximum_distinct_elements([5, 5, 5, 5], 4) == 0

    def test_all_unique(self, maximum_distinct_elements):
        assert maximum_distinct_elements([1, 2, 3, 4], 2) == 2

    def test_remove_all(self, maximum_distinct_elements):
        assert maximum_distinct_elements([1, 2, 3], 3) == 0

    def test_single_element(self, maximum_distinct_elements):
        assert maximum_distinct_elements([5], 0) == 1
        assert maximum_distinct_elements([5], 1) == 0


@pytest.mark.performance
class TestMaximumDistinctElementsPerformance:
    """Performance tests."""

    def test_large_input(self, maximum_distinct_elements):
        nums = list(range(10000)) + list(range(5000))  # 5000 duplicates
        k = 5000

        start = time.time()
        result = maximum_distinct_elements(nums, k)
        elapsed = time.time() - start

        assert result >= 0
        assert elapsed < 1.0
