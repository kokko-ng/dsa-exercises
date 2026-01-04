"""Tests for happy_number problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def happy_number():
    func = get_function("happy_number")
    if func is None:
        pytest.skip("Function 'happy_number' not registered.")
    return func


class TestHappyNumberBasic:
    def test_example_1(self, happy_number):
        assert happy_number(19) is True

    def test_example_2(self, happy_number):
        assert happy_number(2) is False

    def test_one(self, happy_number):
        assert happy_number(1) is True

    def test_seven(self, happy_number):
        assert happy_number(7) is True


class TestHappyNumberEdgeCases:
    def test_small_happy(self, happy_number):
        # Known happy numbers under 20: 1, 7, 10, 13, 19
        assert happy_number(10) is True
        assert happy_number(13) is True

    def test_small_unhappy(self, happy_number):
        assert happy_number(4) is False
        assert happy_number(5) is False
        assert happy_number(6) is False

    def test_larger_happy(self, happy_number):
        assert happy_number(100) is True  # 1^2 + 0^2 + 0^2 = 1

    def test_larger_unhappy(self, happy_number):
        assert happy_number(116) is False
