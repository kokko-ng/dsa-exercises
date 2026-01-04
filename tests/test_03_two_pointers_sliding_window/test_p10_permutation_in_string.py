"""Tests for permutation_in_string problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def permutation_in_string():
    func = get_function("permutation_in_string")
    if func is None:
        pytest.skip("Function 'permutation_in_string' not registered.")
    return func


class TestPermutationBasic:
    def test_example_1(self, permutation_in_string):
        assert permutation_in_string("ab", "eidbaooo") is True

    def test_example_2(self, permutation_in_string):
        assert permutation_in_string("ab", "eidboaoo") is False

    def test_exact_match(self, permutation_in_string):
        assert permutation_in_string("abc", "abc") is True


class TestPermutationEdgeCases:
    def test_s1_longer(self, permutation_in_string):
        assert permutation_in_string("abcd", "ab") is False

    def test_single_char(self, permutation_in_string):
        assert permutation_in_string("a", "a") is True

    def test_single_char_not_found(self, permutation_in_string):
        assert permutation_in_string("a", "b") is False

    def test_at_end(self, permutation_in_string):
        assert permutation_in_string("ab", "xxxba") is True

    def test_repeated_chars(self, permutation_in_string):
        assert permutation_in_string("aab", "cbdaaboa") is False


@pytest.mark.performance
class TestPermutationPerformance:
    def test_large_input(self, permutation_in_string):
        s1 = "abc"
        s2 = "x" * 10000 + "cab"

        start = time.time()
        result = permutation_in_string(s1, s2)
        elapsed = time.time() - start

        assert result is True
        assert elapsed < 1.0
