"""Tests for maximal_square problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def maximal_square():
    func = get_function("maximal_square")
    if func is None:
        pytest.skip("Function 'maximal_square' not registered.")
    return func


class TestMaximalSquareBasic:
    def test_example_1(self, maximal_square):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
        assert maximal_square(matrix) == 4

    def test_example_2(self, maximal_square):
        matrix = [["0", "1"], ["1", "0"]]
        assert maximal_square(matrix) == 1

    def test_example_3(self, maximal_square):
        matrix = [["0"]]
        assert maximal_square(matrix) == 0


class TestMaximalSquareEdgeCases:
    def test_all_ones(self, maximal_square):
        matrix = [["1", "1"], ["1", "1"]]
        assert maximal_square(matrix) == 4

    def test_all_zeros(self, maximal_square):
        matrix = [["0", "0"], ["0", "0"]]
        assert maximal_square(matrix) == 0

    def test_single_one(self, maximal_square):
        matrix = [["1"]]
        assert maximal_square(matrix) == 1


@pytest.mark.performance
class TestMaximalSquarePerformance:
    def test_large_input(self, maximal_square):
        matrix = [["1"] * 300 for _ in range(300)]

        start = time.time()
        result = maximal_square(matrix)
        elapsed = time.time() - start

        assert result == 300 * 300
        assert elapsed < 2.0
