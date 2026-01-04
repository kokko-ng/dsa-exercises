"""Tests for longest_increasing_subsequence problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def longest_increasing_subsequence():
    func = get_function("longest_increasing_subsequence")
    if func is None:
        pytest.skip("Function 'longest_increasing_subsequence' not registered.")
    return func


class TestLISBasic:
    def test_example_1(self, longest_increasing_subsequence):
        assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_example_2(self, longest_increasing_subsequence):
        assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4

    def test_example_3(self, longest_increasing_subsequence):
        assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1


class TestLISEdgeCases:
    def test_single_element(self, longest_increasing_subsequence):
        assert longest_increasing_subsequence([5]) == 1

    def test_increasing(self, longest_increasing_subsequence):
        assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

    def test_decreasing(self, longest_increasing_subsequence):
        assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1


@pytest.mark.performance
class TestLISPerformance:
    def test_large_input(self, longest_increasing_subsequence):
        nums = [i % 100 for i in range(2500)]

        start = time.time()
        result = longest_increasing_subsequence(nums)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 2.0
