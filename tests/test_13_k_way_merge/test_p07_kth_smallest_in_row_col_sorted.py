"""Tests for kth_smallest_in_row_col_sorted problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def kth_smallest_in_row_col_sorted():
    func = get_function("kth_smallest_in_row_col_sorted")
    if func is None:
        pytest.skip("Function 'kth_smallest_in_row_col_sorted' not registered.")
    return func


class TestKthSmallestInRowColSortedBasic:
    """Basic functionality tests."""

    def test_square_matrix(self, kth_smallest_in_row_col_sorted):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        assert kth_smallest_in_row_col_sorted(matrix, 8) == 13

    def test_2x2_matrix(self, kth_smallest_in_row_col_sorted):
        matrix = [[1, 2], [3, 4]]
        assert kth_smallest_in_row_col_sorted(matrix, 3) == 3

    def test_single_row(self, kth_smallest_in_row_col_sorted):
        matrix = [[1, 2, 3, 4, 5]]
        assert kth_smallest_in_row_col_sorted(matrix, 3) == 3

    def test_single_column(self, kth_smallest_in_row_col_sorted):
        matrix = [[1], [2], [3], [4]]
        assert kth_smallest_in_row_col_sorted(matrix, 2) == 2


class TestKthSmallestInRowColSortedEdgeCases:
    """Edge case tests."""

    def test_single_element(self, kth_smallest_in_row_col_sorted):
        assert kth_smallest_in_row_col_sorted([[5]], 1) == 5

    def test_k_equals_total(self, kth_smallest_in_row_col_sorted):
        matrix = [[1, 2], [3, 4]]
        assert kth_smallest_in_row_col_sorted(matrix, 4) == 4

    def test_rectangular_matrix(self, kth_smallest_in_row_col_sorted):
        matrix = [[1, 2, 3], [4, 5, 6]]
        assert kth_smallest_in_row_col_sorted(matrix, 4) == 4

    def test_negative_numbers(self, kth_smallest_in_row_col_sorted):
        matrix = [[-5, -4, -3], [-2, -1, 0]]
        assert kth_smallest_in_row_col_sorted(matrix, 3) == -3


@pytest.mark.performance
class TestKthSmallestInRowColSortedPerformance:
    """Performance tests."""

    def test_large_matrix(self, kth_smallest_in_row_col_sorted):
        m, n = 100, 100
        matrix = [[i + j for j in range(n)] for i in range(m)]
        k = m * n // 2

        start = time.time()
        result = kth_smallest_in_row_col_sorted(matrix, k)
        elapsed = time.time() - start

        assert result >= 0
        assert elapsed < 1.0
