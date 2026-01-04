"""Tests for remove_duplicates problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def remove_duplicates():
    func = get_function("remove_duplicates")
    if func is None:
        pytest.skip("Function 'remove_duplicates' not registered.")
    return func


class TestRemoveDuplicatesBasic:
    def test_simple_duplicates(self, remove_duplicates):
        nums = [1, 1, 2]
        k = remove_duplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 2]

    def test_multiple_duplicates(self, remove_duplicates):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = remove_duplicates(nums)
        assert k == 5
        assert nums[:k] == [0, 1, 2, 3, 4]

    def test_no_duplicates(self, remove_duplicates):
        nums = [1, 2, 3, 4, 5]
        k = remove_duplicates(nums)
        assert k == 5
        assert nums[:k] == [1, 2, 3, 4, 5]


class TestRemoveDuplicatesEdgeCases:
    def test_single_element(self, remove_duplicates):
        nums = [1]
        k = remove_duplicates(nums)
        assert k == 1
        assert nums[:k] == [1]

    def test_all_same(self, remove_duplicates):
        nums = [5, 5, 5, 5, 5]
        k = remove_duplicates(nums)
        assert k == 1
        assert nums[:k] == [5]

    def test_negative_numbers(self, remove_duplicates):
        nums = [-3, -3, -1, 0, 0, 2]
        k = remove_duplicates(nums)
        assert k == 4
        assert nums[:k] == [-3, -1, 0, 2]
