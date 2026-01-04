"""Tests for top_k_frequent problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def top_k_frequent():
    """Get the user's top_k_frequent implementation."""
    func = get_function("top_k_frequent")
    if func is None:
        pytest.skip("Function 'top_k_frequent' not registered. Run check(top_k_frequent) in notebook.")
    return func


class TestTopKFrequentBasic:
    """Basic functionality tests."""

    def test_standard_case(self, top_k_frequent):
        result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        assert sorted(result) == [1, 2]

    def test_single_element(self, top_k_frequent):
        result = top_k_frequent([1], 1)
        assert result == [1]

    def test_all_same_frequency(self, top_k_frequent):
        result = top_k_frequent([1, 2, 3], 2)
        assert len(result) == 2
        assert all(x in [1, 2, 3] for x in result)

    def test_k_equals_unique(self, top_k_frequent):
        result = top_k_frequent([1, 1, 2, 2, 3, 3], 3)
        assert sorted(result) == [1, 2, 3]


class TestTopKFrequentEdgeCases:
    """Edge case tests."""

    def test_negative_numbers(self, top_k_frequent):
        result = top_k_frequent([-1, -1, -2, -2, -2, 3], 1)
        assert result == [-2]

    def test_single_unique(self, top_k_frequent):
        result = top_k_frequent([5, 5, 5, 5], 1)
        assert result == [5]

    def test_many_unique(self, top_k_frequent):
        result = top_k_frequent([1, 1, 1, 2, 2, 3, 4, 5, 6], 3)
        assert 1 in result
        assert 2 in result


@pytest.mark.performance
class TestTopKFrequentPerformance:
    """Performance tests."""

    def test_large_input(self, top_k_frequent):
        nums = list(range(10000)) * 10 + [0] * 1000  # 0 is most frequent
        k = 10

        start = time.time()
        result = top_k_frequent(nums, k)
        elapsed = time.time() - start

        assert 0 in result
        assert len(result) == k
        assert elapsed < 1.0
