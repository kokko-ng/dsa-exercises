"""Tests for next_interval problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def next_interval():
    func = get_function("next_interval")
    if func is None:
        pytest.skip("Function 'next_interval' not registered.")
    return func


class TestNextIntervalBasic:
    def test_example_1(self, next_interval):
        result = next_interval([[1, 2]])
        assert result == [-1]

    def test_example_2(self, next_interval):
        result = next_interval([[3, 4], [2, 3], [1, 2]])
        assert result == [-1, 0, 1]

    def test_example_3(self, next_interval):
        result = next_interval([[1, 4], [2, 3], [3, 4]])
        assert result == [-1, 2, -1]


class TestNextIntervalEdgeCases:
    def test_same_start_end(self, next_interval):
        result = next_interval([[1, 1], [2, 2], [3, 3]])
        assert result == [1, 2, -1]

    def test_overlapping(self, next_interval):
        result = next_interval([[1, 5], [2, 3], [4, 6]])
        assert result == [2, 2, -1]

    def test_consecutive(self, next_interval):
        result = next_interval([[1, 2], [2, 3], [3, 4]])
        assert result == [1, 2, -1]


@pytest.mark.performance
class TestNextIntervalPerformance:
    def test_large_input(self, next_interval):
        intervals = [[i, i + 1] for i in range(10000)]

        start = time.time()
        result = next_interval(intervals)
        elapsed = time.time() - start

        assert len(result) == 10000
        assert elapsed < 2.0
