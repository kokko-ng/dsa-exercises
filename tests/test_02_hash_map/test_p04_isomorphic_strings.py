"""Tests for isomorphic_strings problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def isomorphic_strings():
    func = get_function("isomorphic_strings")
    if func is None:
        pytest.skip("Function 'isomorphic_strings' not registered.")
    return func


class TestIsomorphicStringsBasic:
    def test_example_1(self, isomorphic_strings):
        assert isomorphic_strings("egg", "add") is True

    def test_example_2(self, isomorphic_strings):
        assert isomorphic_strings("foo", "bar") is False

    def test_example_3(self, isomorphic_strings):
        assert isomorphic_strings("paper", "title") is True

    def test_same_string(self, isomorphic_strings):
        assert isomorphic_strings("abc", "abc") is True


class TestIsomorphicStringsEdgeCases:
    def test_single_char(self, isomorphic_strings):
        assert isomorphic_strings("a", "b") is True

    def test_all_same_chars(self, isomorphic_strings):
        assert isomorphic_strings("aaa", "bbb") is True

    def test_two_to_one_mapping(self, isomorphic_strings):
        # 'a' and 'b' both mapping to 'a' - invalid
        assert isomorphic_strings("ab", "aa") is False

    def test_one_to_two_mapping(self, isomorphic_strings):
        # 'a' mapping to both 'a' and 'b' - invalid
        assert isomorphic_strings("aa", "ab") is False

    def test_longer_strings(self, isomorphic_strings):
        assert isomorphic_strings("abcdefghij", "klmnopqrst") is True

    def test_special_chars(self, isomorphic_strings):
        assert isomorphic_strings("a.b", "x.y") is True
