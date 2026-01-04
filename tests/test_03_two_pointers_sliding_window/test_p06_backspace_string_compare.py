"""Tests for backspace_string_compare problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def backspace_string_compare():
    func = get_function("backspace_string_compare")
    if func is None:
        pytest.skip("Function 'backspace_string_compare' not registered.")
    return func


class TestBackspaceBasic:
    def test_example_1(self, backspace_string_compare):
        assert backspace_string_compare("ab#c", "ad#c") is True

    def test_example_2(self, backspace_string_compare):
        assert backspace_string_compare("ab##", "c#d#") is True

    def test_example_3(self, backspace_string_compare):
        assert backspace_string_compare("a#c", "b") is False


class TestBackspaceEdgeCases:
    def test_no_backspace(self, backspace_string_compare):
        assert backspace_string_compare("abc", "abc") is True

    def test_all_backspace(self, backspace_string_compare):
        assert backspace_string_compare("a#", "b#") is True

    def test_extra_backspace(self, backspace_string_compare):
        assert backspace_string_compare("###a", "a") is True

    def test_empty_result(self, backspace_string_compare):
        assert backspace_string_compare("a#", "#") is True

    def test_consecutive_backspace(self, backspace_string_compare):
        assert backspace_string_compare("abc###", "") is True

    def test_different_length(self, backspace_string_compare):
        assert backspace_string_compare("a", "aa#") is True
