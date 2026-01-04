"""Tests for combination_sum problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def combination_sum():
    func = get_function("combination_sum")
    if func is None:
        pytest.skip("Function 'combination_sum' not registered.")
    return func


class TestCombinationSumBasic:
    def test_example_1(self, combination_sum):
        result = combination_sum([2, 3, 6, 7], 7)
        expected = [[2, 2, 3], [7]]
        assert sorted([sorted(r) for r in result]) == sorted([sorted(e) for e in expected])

    def test_example_2(self, combination_sum):
        result = combination_sum([2, 3, 5], 8)
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        assert sorted([sorted(r) for r in result]) == sorted([sorted(e) for e in expected])

    def test_example_3(self, combination_sum):
        result = combination_sum([2], 1)
        assert result == []


class TestCombinationSumEdgeCases:
    def test_single_element_exact(self, combination_sum):
        result = combination_sum([5], 5)
        assert result == [[5]]

    def test_reuse_element(self, combination_sum):
        result = combination_sum([2], 4)
        assert result == [[2, 2]]

    def test_no_solution(self, combination_sum):
        result = combination_sum([3, 5], 7)
        assert result == []
