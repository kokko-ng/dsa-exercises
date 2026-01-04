"""Tests for subsets problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def subsets():
    """Get the user's subsets implementation."""
    func = get_function("subsets")
    if func is None:
        pytest.skip("Function 'subsets' not registered. Run check(subsets) in notebook.")
    return func


class TestSubsetsBasic:
    """Basic functionality tests."""

    def test_example_1(self, subsets):
        result = subsets([1, 2, 3])
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        assert len(result) == len(expected)
        for subset in expected:
            assert sorted(subset) in [sorted(r) for r in result]

    def test_example_2(self, subsets):
        result = subsets([0])
        assert len(result) == 2
        assert [] in result
        assert [0] in result

    def test_two_elements(self, subsets):
        result = subsets([1, 2])
        expected = [[], [1], [2], [1, 2]]
        assert len(result) == 4

    def test_single_element(self, subsets):
        result = subsets([5])
        assert len(result) == 2


class TestSubsetsEdgeCases:
    """Edge case tests."""

    def test_negative_numbers(self, subsets):
        result = subsets([-1, 0, 1])
        assert len(result) == 8

    def test_power_of_two_count(self, subsets):
        # For n elements, there should be 2^n subsets
        result = subsets([1, 2, 3, 4])
        assert len(result) == 16


@pytest.mark.performance
class TestSubsetsPerformance:
    """Performance tests."""

    def test_max_size(self, subsets):
        nums = list(range(10))

        start = time.time()
        result = subsets(nums)
        elapsed = time.time() - start

        assert len(result) == 1024  # 2^10
        assert elapsed < 1.0
