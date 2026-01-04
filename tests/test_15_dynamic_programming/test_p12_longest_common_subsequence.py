"""Tests for longest_common_subsequence problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def longest_common_subsequence():
    func = get_function("longest_common_subsequence")
    if func is None:
        pytest.skip("Function 'longest_common_subsequence' not registered.")
    return func


class TestLCSBasic:
    def test_example_1(self, longest_common_subsequence):
        assert longest_common_subsequence("abcde", "ace") == 3

    def test_example_2(self, longest_common_subsequence):
        assert longest_common_subsequence("abc", "abc") == 3

    def test_example_3(self, longest_common_subsequence):
        assert longest_common_subsequence("abc", "def") == 0


class TestLCSEdgeCases:
    def test_empty_string(self, longest_common_subsequence):
        assert longest_common_subsequence("", "abc") == 0

    def test_single_char_match(self, longest_common_subsequence):
        assert longest_common_subsequence("a", "a") == 1

    def test_single_char_no_match(self, longest_common_subsequence):
        assert longest_common_subsequence("a", "b") == 0


@pytest.mark.performance
class TestLCSPerformance:
    def test_large_input(self, longest_common_subsequence):
        text1 = "abcdefghij" * 100
        text2 = "jihgfedcba" * 100

        start = time.time()
        result = longest_common_subsequence(text1, text2)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 3.0
