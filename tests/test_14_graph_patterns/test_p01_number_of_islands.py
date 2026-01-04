"""Tests for number_of_islands problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def number_of_islands():
    func = get_function("number_of_islands")
    if func is None:
        pytest.skip("Function 'number_of_islands' not registered.")
    return func


class TestNumberOfIslandsBasic:
    def test_single_island(self, number_of_islands):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        assert number_of_islands([row[:] for row in grid]) == 1

    def test_three_islands(self, number_of_islands):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        assert number_of_islands([row[:] for row in grid]) == 3

    def test_no_islands(self, number_of_islands):
        grid = [
            ["0", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"]
        ]
        assert number_of_islands([row[:] for row in grid]) == 0


class TestNumberOfIslandsEdgeCases:
    def test_all_land(self, number_of_islands):
        grid = [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"]
        ]
        assert number_of_islands([row[:] for row in grid]) == 1

    def test_single_cell_land(self, number_of_islands):
        grid = [["1"]]
        assert number_of_islands([row[:] for row in grid]) == 1

    def test_single_cell_water(self, number_of_islands):
        grid = [["0"]]
        assert number_of_islands([row[:] for row in grid]) == 0

    def test_diagonal_not_connected(self, number_of_islands):
        grid = [
            ["1", "0"],
            ["0", "1"]
        ]
        assert number_of_islands([row[:] for row in grid]) == 2


@pytest.mark.performance
class TestNumberOfIslandsPerformance:
    def test_large_grid(self, number_of_islands):
        n = 300
        grid = [["1" if (i + j) % 2 == 0 else "0" for j in range(n)] for i in range(n)]

        start = time.time()
        result = number_of_islands(grid)
        elapsed = time.time() - start

        assert result >= 0
        assert elapsed < 2.0
