"""Tests for combination_sum_ii problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def combination_sum_ii():
    func = get_function("combination_sum_ii")
    if func is None:
        pytest.skip("Function 'combination_sum_ii' not registered.")
    return func


class TestCombinationSumIIBasic:
    def test_example_1(self, combination_sum_ii):
        result = combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8)
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        assert sorted([sorted(r) for r in result]) == sorted([sorted(e) for e in expected])

    def test_example_2(self, combination_sum_ii):
        result = combination_sum_ii([2, 5, 2, 1, 2], 5)
        expected = [[1, 2, 2], [5]]
        assert sorted([sorted(r) for r in result]) == sorted([sorted(e) for e in expected])


class TestCombinationSumIIEdgeCases:
    def test_no_duplicates_in_result(self, combination_sum_ii):
        result = combination_sum_ii([1, 1, 1], 2)
        assert result == [[1, 1]]

    def test_single_element(self, combination_sum_ii):
        result = combination_sum_ii([5], 5)
        assert result == [[5]]

    def test_no_solution(self, combination_sum_ii):
        result = combination_sum_ii([2, 4, 6], 5)
        assert result == []
