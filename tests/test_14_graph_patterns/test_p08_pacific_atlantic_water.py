"""Tests for pacific_atlantic_water problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def pacific_atlantic_water():
    func = get_function("pacific_atlantic_water")
    if func is None:
        pytest.skip("Function 'pacific_atlantic_water' not registered.")
    return func


class TestPacificAtlanticWaterBasic:
    def test_example_1(self, pacific_atlantic_water):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        result = pacific_atlantic_water(heights)
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        assert sorted(result) == sorted(expected)

    def test_single_cell(self, pacific_atlantic_water):
        heights = [[1]]
        result = pacific_atlantic_water(heights)
        assert result == [[0, 0]]


class TestPacificAtlanticWaterEdgeCases:
    def test_all_same_height(self, pacific_atlantic_water):
        heights = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = pacific_atlantic_water(heights)
        # All cells should be reachable from both oceans
        assert len(result) == 9

    def test_single_row(self, pacific_atlantic_water):
        heights = [[1, 2, 3]]
        result = pacific_atlantic_water(heights)
        expected = [[0, 0], [0, 1], [0, 2]]
        assert sorted(result) == sorted(expected)

    def test_single_column(self, pacific_atlantic_water):
        heights = [[1], [2], [3]]
        result = pacific_atlantic_water(heights)
        expected = [[0, 0], [1, 0], [2, 0]]
        assert sorted(result) == sorted(expected)


@pytest.mark.performance
class TestPacificAtlanticWaterPerformance:
    def test_large_grid(self, pacific_atlantic_water):
        n = 200
        heights = [[i + j for j in range(n)] for i in range(n)]

        start = time.time()
        result = pacific_atlantic_water(heights)
        elapsed = time.time() - start

        assert len(result) >= 0
        assert elapsed < 2.0
