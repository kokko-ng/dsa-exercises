"""Tests for letter_combinations_phone problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def letter_combinations_phone():
    func = get_function("letter_combinations_phone")
    if func is None:
        pytest.skip("Function 'letter_combinations_phone' not registered.")
    return func


class TestLetterCombinationsPhoneBasic:
    def test_example_1(self, letter_combinations_phone):
        result = letter_combinations_phone("23")
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        assert sorted(result) == sorted(expected)

    def test_example_2(self, letter_combinations_phone):
        result = letter_combinations_phone("")
        assert result == []

    def test_example_3(self, letter_combinations_phone):
        result = letter_combinations_phone("2")
        expected = ["a", "b", "c"]
        assert sorted(result) == sorted(expected)


class TestLetterCombinationsPhoneEdgeCases:
    def test_digit_7(self, letter_combinations_phone):
        result = letter_combinations_phone("7")
        expected = ["p", "q", "r", "s"]
        assert sorted(result) == sorted(expected)

    def test_digit_9(self, letter_combinations_phone):
        result = letter_combinations_phone("9")
        expected = ["w", "x", "y", "z"]
        assert sorted(result) == sorted(expected)

    def test_three_digits(self, letter_combinations_phone):
        result = letter_combinations_phone("234")
        assert len(result) == 3 * 3 * 3  # 27 combinations
