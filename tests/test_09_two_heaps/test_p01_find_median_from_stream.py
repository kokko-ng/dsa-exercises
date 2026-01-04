"""Tests for find_median_from_stream problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def find_median_from_stream():
    """Get the user's MedianFinder class."""
    func = get_function("find_median_from_stream")
    if func is None:
        pytest.skip("Function 'find_median_from_stream' not registered.")
    return func


class TestFindMedianFromStreamBasic:
    """Basic functionality tests."""

    def test_example_1(self, find_median_from_stream):
        MedianFinder = find_median_from_stream()
        mf = MedianFinder()
        mf.add_num(1)
        mf.add_num(2)
        assert abs(mf.find_median() - 1.5) < 0.001
        mf.add_num(3)
        assert abs(mf.find_median() - 2.0) < 0.001

    def test_single_element(self, find_median_from_stream):
        MedianFinder = find_median_from_stream()
        mf = MedianFinder()
        mf.add_num(5)
        assert abs(mf.find_median() - 5.0) < 0.001

    def test_two_elements(self, find_median_from_stream):
        MedianFinder = find_median_from_stream()
        mf = MedianFinder()
        mf.add_num(1)
        mf.add_num(2)
        assert abs(mf.find_median() - 1.5) < 0.001

    def test_odd_count(self, find_median_from_stream):
        MedianFinder = find_median_from_stream()
        mf = MedianFinder()
        for num in [1, 2, 3, 4, 5]:
            mf.add_num(num)
        assert abs(mf.find_median() - 3.0) < 0.001


class TestFindMedianFromStreamEdgeCases:
    """Edge case tests."""

    def test_negative_numbers(self, find_median_from_stream):
        MedianFinder = find_median_from_stream()
        mf = MedianFinder()
        for num in [-5, -10, -3]:
            mf.add_num(num)
        assert abs(mf.find_median() - (-5.0)) < 0.001

    def test_duplicates(self, find_median_from_stream):
        MedianFinder = find_median_from_stream()
        mf = MedianFinder()
        for num in [1, 1, 1, 1]:
            mf.add_num(num)
        assert abs(mf.find_median() - 1.0) < 0.001

    def test_unsorted_input(self, find_median_from_stream):
        MedianFinder = find_median_from_stream()
        mf = MedianFinder()
        for num in [5, 2, 8, 1, 9]:
            mf.add_num(num)
        assert abs(mf.find_median() - 5.0) < 0.001


@pytest.mark.performance
class TestFindMedianFromStreamPerformance:
    """Performance tests."""

    def test_large_input(self, find_median_from_stream):
        MedianFinder = find_median_from_stream()
        mf = MedianFinder()

        start = time.time()
        for i in range(10000):
            mf.add_num(i)
            mf.find_median()
        elapsed = time.time() - start

        assert abs(mf.find_median() - 4999.5) < 0.001
        assert elapsed < 2.0
