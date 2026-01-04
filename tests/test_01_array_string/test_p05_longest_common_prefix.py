"""Tests for longest_common_prefix problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def longest_common_prefix():
    func = get_function("longest_common_prefix")
    if func is None:
        pytest.skip("Function 'longest_common_prefix' not registered.")
    return func


class TestLongestCommonPrefixBasic:
    def test_common_prefix(self, longest_common_prefix):
        assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

    def test_no_common_prefix(self, longest_common_prefix):
        assert longest_common_prefix(["dog", "racecar", "car"]) == ""

    def test_single_string(self, longest_common_prefix):
        assert longest_common_prefix(["alone"]) == "alone"

    def test_identical_strings(self, longest_common_prefix):
        assert longest_common_prefix(["test", "test", "test"]) == "test"


class TestLongestCommonPrefixEdgeCases:
    def test_empty_string_in_list(self, longest_common_prefix):
        assert longest_common_prefix(["", "abc", "ab"]) == ""

    def test_empty_list(self, longest_common_prefix):
        assert longest_common_prefix([]) == ""

    def test_one_char_common(self, longest_common_prefix):
        assert longest_common_prefix(["abc", "axy", "azz"]) == "a"

    def test_full_match_short(self, longest_common_prefix):
        assert longest_common_prefix(["ab", "abc", "abcd"]) == "ab"
