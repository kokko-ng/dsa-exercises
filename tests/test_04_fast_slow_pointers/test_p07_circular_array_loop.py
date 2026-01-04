"""Tests for circular_array_loop problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def circular_array_loop():
    func = get_function("circular_array_loop")
    if func is None:
        pytest.skip("Function 'circular_array_loop' not registered.")
    return func


class TestCircularArrayLoopBasic:
    def test_example_1(self, circular_array_loop):
        assert circular_array_loop([2, -1, 1, 2, 2]) is True

    def test_example_2(self, circular_array_loop):
        # Cycle length is 1 (self-loop)
        assert circular_array_loop([-1, 2]) is False

    def test_example_3(self, circular_array_loop):
        # Mixed directions in cycle
        assert circular_array_loop([-2, 1, -1, -2, -2]) is False


class TestCircularArrayLoopEdgeCases:
    def test_single_element(self, circular_array_loop):
        # Self-loop has length 1
        assert circular_array_loop([1]) is False
        assert circular_array_loop([-1]) is False

    def test_all_positive_cycle(self, circular_array_loop):
        assert circular_array_loop([1, 1, 1, 1]) is True

    def test_all_negative_cycle(self, circular_array_loop):
        assert circular_array_loop([-1, -1, -1, -1]) is True

    def test_no_cycle(self, circular_array_loop):
        assert circular_array_loop([1, 2, 3, 4, 5]) is False

    def test_mixed_directions_invalid(self, circular_array_loop):
        # Would form cycle but directions are mixed
        assert circular_array_loop([1, -1]) is False
