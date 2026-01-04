"""Tests for move_zeroes problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def move_zeroes():
    func = get_function("move_zeroes")
    if func is None:
        pytest.skip("Function 'move_zeroes' not registered.")
    return func


class TestMoveZeroesBasic:
    def test_mixed_zeros(self, move_zeroes):
        nums = [0, 1, 0, 3, 12]
        move_zeroes(nums)
        assert nums == [1, 3, 12, 0, 0]

    def test_single_zero(self, move_zeroes):
        nums = [0]
        move_zeroes(nums)
        assert nums == [0]

    def test_zeros_at_start(self, move_zeroes):
        nums = [0, 0, 1]
        move_zeroes(nums)
        assert nums == [1, 0, 0]


class TestMoveZeroesEdgeCases:
    def test_no_zeros(self, move_zeroes):
        nums = [1, 2, 3]
        move_zeroes(nums)
        assert nums == [1, 2, 3]

    def test_all_zeros(self, move_zeroes):
        nums = [0, 0, 0]
        move_zeroes(nums)
        assert nums == [0, 0, 0]

    def test_zeros_at_end(self, move_zeroes):
        nums = [1, 2, 0, 0]
        move_zeroes(nums)
        assert nums == [1, 2, 0, 0]

    def test_alternating(self, move_zeroes):
        nums = [0, 1, 0, 2, 0, 3]
        move_zeroes(nums)
        assert nums == [1, 2, 3, 0, 0, 0]
