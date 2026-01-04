"""Tests for sliding_window_median problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def sliding_window_median():
    func = get_function("sliding_window_median")
    if func is None:
        pytest.skip("Function 'sliding_window_median' not registered.")
    return func


class TestSlidingWindowMedianBasic:
    def test_example_1(self, sliding_window_median):
        result = sliding_window_median([1, 3, -1, -3, 5, 3, 6, 7], 3)
        expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
        assert len(result) == len(expected)
        for r, e in zip(result, expected):
            assert abs(r - e) < 0.001

    def test_example_2(self, sliding_window_median):
        result = sliding_window_median([1, 2, 3, 4, 2, 3, 1, 4, 2], 3)
        expected = [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
        assert len(result) == len(expected)
        for r, e in zip(result, expected):
            assert abs(r - e) < 0.001

    def test_single_element_window(self, sliding_window_median):
        result = sliding_window_median([1, 2, 3], 1)
        expected = [1.0, 2.0, 3.0]
        assert len(result) == len(expected)

    def test_full_window(self, sliding_window_median):
        result = sliding_window_median([1, 2, 3], 3)
        assert len(result) == 1
        assert abs(result[0] - 2.0) < 0.001


class TestSlidingWindowMedianEdgeCases:
    def test_even_window(self, sliding_window_median):
        result = sliding_window_median([1, 2, 3, 4], 2)
        expected = [1.5, 2.5, 3.5]
        for r, e in zip(result, expected):
            assert abs(r - e) < 0.001

    def test_duplicates(self, sliding_window_median):
        result = sliding_window_median([1, 1, 1, 1], 2)
        for r in result:
            assert abs(r - 1.0) < 0.001


@pytest.mark.performance
class TestSlidingWindowMedianPerformance:
    def test_large_input(self, sliding_window_median):
        nums = list(range(1000))

        start = time.time()
        result = sliding_window_median(nums, 100)
        elapsed = time.time() - start

        assert len(result) == 901
        assert elapsed < 2.0
