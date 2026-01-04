"""Tests for happy_number_fast_slow problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def happy_number_fast_slow():
    func = get_function("happy_number_fast_slow")
    if func is None:
        pytest.skip("Function 'happy_number_fast_slow' not registered.")
    return func


class TestHappyNumberFastSlowBasic:
    def test_example_1(self, happy_number_fast_slow):
        assert happy_number_fast_slow(19) is True

    def test_example_2(self, happy_number_fast_slow):
        assert happy_number_fast_slow(2) is False

    def test_one(self, happy_number_fast_slow):
        assert happy_number_fast_slow(1) is True

    def test_seven(self, happy_number_fast_slow):
        assert happy_number_fast_slow(7) is True


class TestHappyNumberFastSlowEdgeCases:
    def test_small_happy(self, happy_number_fast_slow):
        # Known happy numbers under 20: 1, 7, 10, 13, 19
        assert happy_number_fast_slow(10) is True
        assert happy_number_fast_slow(13) is True

    def test_small_unhappy(self, happy_number_fast_slow):
        assert happy_number_fast_slow(4) is False
        assert happy_number_fast_slow(5) is False
        assert happy_number_fast_slow(6) is False

    def test_larger_happy(self, happy_number_fast_slow):
        assert happy_number_fast_slow(100) is True

    def test_larger_unhappy(self, happy_number_fast_slow):
        assert happy_number_fast_slow(116) is False
