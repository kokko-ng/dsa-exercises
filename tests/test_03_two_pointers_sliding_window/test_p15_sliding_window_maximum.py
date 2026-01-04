"""Tests for sliding_window_maximum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def sliding_window_maximum():
    func = get_function("sliding_window_maximum")
    if func is None:
        pytest.skip("Function 'sliding_window_maximum' not registered.")
    return func


class TestSlidingWindowMaxBasic:
    def test_example_1(self, sliding_window_maximum):
        assert sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    def test_example_2(self, sliding_window_maximum):
        assert sliding_window_maximum([1], 1) == [1]


class TestSlidingWindowMaxEdgeCases:
    def test_k_equals_n(self, sliding_window_maximum):
        assert sliding_window_maximum([1, 3, 2], 3) == [3]

    def test_all_same(self, sliding_window_maximum):
        assert sliding_window_maximum([5, 5, 5, 5], 2) == [5, 5, 5]

    def test_increasing(self, sliding_window_maximum):
        assert sliding_window_maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]

    def test_decreasing(self, sliding_window_maximum):
        assert sliding_window_maximum([5, 4, 3, 2, 1], 3) == [5, 4, 3]

    def test_negatives(self, sliding_window_maximum):
        assert sliding_window_maximum([-1, -2, -3, -4], 2) == [-1, -2, -3]


@pytest.mark.performance
class TestSlidingWindowMaxPerformance:
    def test_large_input(self, sliding_window_maximum):
        nums = list(range(100000))
        k = 1000

        start = time.time()
        result = sliding_window_maximum(nums, k)
        elapsed = time.time() - start

        assert len(result) == 99001
        assert elapsed < 1.0
