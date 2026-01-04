"""Tests for minimum_path_sum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def minimum_path_sum():
    func = get_function("minimum_path_sum")
    if func is None:
        pytest.skip("Function 'minimum_path_sum' not registered.")
    return func


class TestMinimumPathSumBasic:
    def test_example_1(self, minimum_path_sum):
        assert minimum_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7

    def test_example_2(self, minimum_path_sum):
        assert minimum_path_sum([[1, 2, 3], [4, 5, 6]]) == 12


class TestMinimumPathSumEdgeCases:
    def test_single_cell(self, minimum_path_sum):
        assert minimum_path_sum([[5]]) == 5

    def test_single_row(self, minimum_path_sum):
        assert minimum_path_sum([[1, 2, 3]]) == 6

    def test_single_column(self, minimum_path_sum):
        assert minimum_path_sum([[1], [2], [3]]) == 6


@pytest.mark.performance
class TestMinimumPathSumPerformance:
    def test_large_input(self, minimum_path_sum):
        grid = [[1] * 200 for _ in range(200)]

        start = time.time()
        result = minimum_path_sum(grid)
        elapsed = time.time() - start

        assert result == 399
        assert elapsed < 1.0
