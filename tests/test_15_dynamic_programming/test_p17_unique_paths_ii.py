"""Tests for unique_paths_ii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def unique_paths_ii():
    func = get_function("unique_paths_ii")
    if func is None:
        pytest.skip("Function 'unique_paths_ii' not registered.")
    return func


class TestUniquePathsIIBasic:
    def test_example_1(self, unique_paths_ii):
        assert unique_paths_ii([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2

    def test_example_2(self, unique_paths_ii):
        assert unique_paths_ii([[0, 1], [0, 0]]) == 1


class TestUniquePathsIIEdgeCases:
    def test_start_blocked(self, unique_paths_ii):
        assert unique_paths_ii([[1, 0], [0, 0]]) == 0

    def test_end_blocked(self, unique_paths_ii):
        assert unique_paths_ii([[0, 0], [0, 1]]) == 0

    def test_no_obstacles(self, unique_paths_ii):
        assert unique_paths_ii([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 6

    def test_single_cell(self, unique_paths_ii):
        assert unique_paths_ii([[0]]) == 1


@pytest.mark.performance
class TestUniquePathsIIPerformance:
    def test_large_input(self, unique_paths_ii):
        grid = [[0] * 100 for _ in range(100)]

        start = time.time()
        result = unique_paths_ii(grid)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0
