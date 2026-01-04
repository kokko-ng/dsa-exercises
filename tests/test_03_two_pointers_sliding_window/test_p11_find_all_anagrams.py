"""Tests for find_all_anagrams problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def find_all_anagrams():
    func = get_function("find_all_anagrams")
    if func is None:
        pytest.skip("Function 'find_all_anagrams' not registered.")
    return func


class TestFindAnagramsBasic:
    def test_example_1(self, find_all_anagrams):
        assert find_all_anagrams("cbaebabacd", "abc") == [0, 6]

    def test_example_2(self, find_all_anagrams):
        assert find_all_anagrams("abab", "ab") == [0, 1, 2]


class TestFindAnagramsEdgeCases:
    def test_no_anagrams(self, find_all_anagrams):
        assert find_all_anagrams("xyz", "abc") == []

    def test_p_longer_than_s(self, find_all_anagrams):
        assert find_all_anagrams("ab", "abc") == []

    def test_single_char(self, find_all_anagrams):
        assert find_all_anagrams("aaaa", "a") == [0, 1, 2, 3]

    def test_exact_match(self, find_all_anagrams):
        assert find_all_anagrams("abc", "bca") == [0]


@pytest.mark.performance
class TestFindAnagramsPerformance:
    def test_large_input(self, find_all_anagrams):
        s = "abc" * 10000
        p = "cab"

        start = time.time()
        result = find_all_anagrams(s, p)
        elapsed = time.time() - start

        assert len(result) == 29999
        assert elapsed < 1.0
