"""Tests for combination_sum_iii problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def combination_sum_iii():
    func = get_function("combination_sum_iii")
    if func is None:
        pytest.skip("Function 'combination_sum_iii' not registered.")
    return func


class TestCombinationSumIIIBasic:
    def test_example_1(self, combination_sum_iii):
        result = combination_sum_iii(3, 7)
        assert result == [[1, 2, 4]]

    def test_example_2(self, combination_sum_iii):
        result = combination_sum_iii(3, 9)
        expected = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        assert sorted(result) == sorted(expected)

    def test_example_3(self, combination_sum_iii):
        result = combination_sum_iii(4, 1)
        assert result == []


class TestCombinationSumIIIEdgeCases:
    def test_k_equals_1(self, combination_sum_iii):
        result = combination_sum_iii(1, 5)
        assert result == [[5]]

    def test_no_solution(self, combination_sum_iii):
        result = combination_sum_iii(2, 18)
        assert result == []  # Max is 8+9=17

    def test_max_sum(self, combination_sum_iii):
        # k=2, n=17 gives [8,9]
        result = combination_sum_iii(2, 17)
        assert result == [[8, 9]]
