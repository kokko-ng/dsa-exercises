"""Tests for rotate_array problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def rotate_array():
    func = get_function("rotate_array")
    if func is None:
        pytest.skip("Function 'rotate_array' not registered.")
    return func


class TestRotateArrayBasic:
    def test_rotate_by_3(self, rotate_array):
        nums = [1, 2, 3, 4, 5, 6, 7]
        rotate_array(nums, 3)
        assert nums == [5, 6, 7, 1, 2, 3, 4]

    def test_rotate_by_2(self, rotate_array):
        nums = [-1, -100, 3, 99]
        rotate_array(nums, 2)
        assert nums == [3, 99, -1, -100]

    def test_rotate_by_1(self, rotate_array):
        nums = [1, 2, 3]
        rotate_array(nums, 1)
        assert nums == [3, 1, 2]


class TestRotateArrayEdgeCases:
    def test_rotate_by_0(self, rotate_array):
        nums = [1, 2, 3]
        rotate_array(nums, 0)
        assert nums == [1, 2, 3]

    def test_rotate_by_length(self, rotate_array):
        nums = [1, 2, 3]
        rotate_array(nums, 3)
        assert nums == [1, 2, 3]

    def test_rotate_more_than_length(self, rotate_array):
        nums = [1, 2, 3]
        rotate_array(nums, 5)  # 5 % 3 = 2
        assert nums == [2, 3, 1]

    def test_single_element(self, rotate_array):
        nums = [1]
        rotate_array(nums, 10)
        assert nums == [1]
