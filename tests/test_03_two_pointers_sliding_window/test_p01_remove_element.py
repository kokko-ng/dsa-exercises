"""Tests for remove_element problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def remove_element():
    func = get_function("remove_element")
    if func is None:
        pytest.skip("Function 'remove_element' not registered.")
    return func


class TestRemoveElementBasic:
    def test_example_1(self, remove_element):
        nums = [3, 2, 2, 3]
        k = remove_element(nums, 3)
        assert k == 2
        assert sorted(nums[:k]) == [2, 2]

    def test_example_2(self, remove_element):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        k = remove_element(nums, 2)
        assert k == 5
        assert sorted(nums[:k]) == [0, 0, 1, 3, 4]

    def test_no_match(self, remove_element):
        nums = [1, 2, 3, 4]
        k = remove_element(nums, 5)
        assert k == 4


class TestRemoveElementEdgeCases:
    def test_all_match(self, remove_element):
        nums = [3, 3, 3]
        k = remove_element(nums, 3)
        assert k == 0

    def test_empty_array(self, remove_element):
        nums = []
        k = remove_element(nums, 1)
        assert k == 0

    def test_single_match(self, remove_element):
        nums = [1]
        k = remove_element(nums, 1)
        assert k == 0

    def test_single_no_match(self, remove_element):
        nums = [1]
        k = remove_element(nums, 2)
        assert k == 1
