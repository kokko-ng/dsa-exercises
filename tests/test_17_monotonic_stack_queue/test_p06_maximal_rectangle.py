"""Tests for maximal_rectangle problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def maximal_rectangle():
    """Get the user's maximal_rectangle implementation."""
    func = get_function("maximal_rectangle")
    if func is None:
        pytest.skip("Function 'maximal_rectangle' not registered. Run check(maximal_rectangle) in notebook.")
    return func


class TestMaximalRectangleBasic:
    """Basic functionality tests."""

    def test_example_case(self, maximal_rectangle):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
        result = maximal_rectangle(matrix)
        assert result == 6

    def test_single_zero(self, maximal_rectangle):
        result = maximal_rectangle([["0"]])
        assert result == 0

    def test_single_one(self, maximal_rectangle):
        result = maximal_rectangle([["1"]])
        assert result == 1

    def test_all_ones(self, maximal_rectangle):
        matrix = [
            ["1", "1"],
            ["1", "1"]
        ]
        result = maximal_rectangle(matrix)
        assert result == 4

    def test_all_zeros(self, maximal_rectangle):
        matrix = [
            ["0", "0"],
            ["0", "0"]
        ]
        result = maximal_rectangle(matrix)
        assert result == 0


class TestMaximalRectangleEdgeCases:
    """Edge case tests."""

    def test_single_row(self, maximal_rectangle):
        result = maximal_rectangle([["1", "1", "1"]])
        assert result == 3

    def test_single_column(self, maximal_rectangle):
        matrix = [["1"], ["1"], ["1"]]
        result = maximal_rectangle(matrix)
        assert result == 3

    def test_broken_rectangle(self, maximal_rectangle):
        matrix = [
            ["1", "1", "1"],
            ["1", "0", "1"],
            ["1", "1", "1"]
        ]
        result = maximal_rectangle(matrix)
        assert result == 3

    def test_l_shape(self, maximal_rectangle):
        matrix = [
            ["1", "0"],
            ["1", "0"],
            ["1", "1"]
        ]
        result = maximal_rectangle(matrix)
        assert result == 3

    def test_diagonal(self, maximal_rectangle):
        matrix = [
            ["1", "0", "0"],
            ["0", "1", "0"],
            ["0", "0", "1"]
        ]
        result = maximal_rectangle(matrix)
        assert result == 1


@pytest.mark.performance
class TestMaximalRectanglePerformance:
    """Performance tests."""

    def test_large_input(self, maximal_rectangle):
        n = 200
        matrix = [["1"] * n for _ in range(n)]

        start = time.time()
        result = maximal_rectangle(matrix)
        elapsed = time.time() - start

        assert result == n * n
        assert elapsed < 2.0, f"Solution too slow: {elapsed:.2f}s (should be < 2s)"
