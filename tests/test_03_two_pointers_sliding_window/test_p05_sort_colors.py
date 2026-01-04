"""Tests for sort_colors problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def sort_colors():
    func = get_function("sort_colors")
    if func is None:
        pytest.skip("Function 'sort_colors' not registered.")
    return func


class TestSortColorsBasic:
    def test_example_1(self, sort_colors):
        nums = [2, 0, 2, 1, 1, 0]
        sort_colors(nums)
        assert nums == [0, 0, 1, 1, 2, 2]

    def test_example_2(self, sort_colors):
        nums = [2, 0, 1]
        sort_colors(nums)
        assert nums == [0, 1, 2]


class TestSortColorsEdgeCases:
    def test_single_element(self, sort_colors):
        nums = [1]
        sort_colors(nums)
        assert nums == [1]

    def test_already_sorted(self, sort_colors):
        nums = [0, 0, 1, 1, 2, 2]
        sort_colors(nums)
        assert nums == [0, 0, 1, 1, 2, 2]

    def test_reverse_sorted(self, sort_colors):
        nums = [2, 2, 1, 1, 0, 0]
        sort_colors(nums)
        assert nums == [0, 0, 1, 1, 2, 2]

    def test_all_same(self, sort_colors):
        nums = [1, 1, 1]
        sort_colors(nums)
        assert nums == [1, 1, 1]

    def test_only_zeros_and_twos(self, sort_colors):
        nums = [2, 0, 2, 0]
        sort_colors(nums)
        assert nums == [0, 0, 2, 2]
