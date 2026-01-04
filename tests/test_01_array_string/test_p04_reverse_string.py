"""Tests for reverse_string problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def reverse_string():
    func = get_function("reverse_string")
    if func is None:
        pytest.skip("Function 'reverse_string' not registered.")
    return func


class TestReverseStringBasic:
    def test_hello(self, reverse_string):
        s = ["h", "e", "l", "l", "o"]
        reverse_string(s)
        assert s == ["o", "l", "l", "e", "h"]

    def test_hannah(self, reverse_string):
        s = ["H", "a", "n", "n", "a", "h"]
        reverse_string(s)
        assert s == ["h", "a", "n", "n", "a", "H"]

    def test_two_chars(self, reverse_string):
        s = ["a", "b"]
        reverse_string(s)
        assert s == ["b", "a"]


class TestReverseStringEdgeCases:
    def test_single_char(self, reverse_string):
        s = ["a"]
        reverse_string(s)
        assert s == ["a"]

    def test_palindrome(self, reverse_string):
        s = ["r", "a", "c", "e", "c", "a", "r"]
        reverse_string(s)
        assert s == ["r", "a", "c", "e", "c", "a", "r"]

    def test_numbers_as_strings(self, reverse_string):
        s = ["1", "2", "3"]
        reverse_string(s)
        assert s == ["3", "2", "1"]
