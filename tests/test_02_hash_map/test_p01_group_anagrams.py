"""Tests for group_anagrams problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def group_anagrams():
    """Get the user's group_anagrams implementation."""
    func = get_function("group_anagrams")
    if func is None:
        pytest.skip("Function 'group_anagrams' not registered. Run check(group_anagrams) in notebook.")
    return func


def normalize_groups(groups):
    """Sort each group and the list of groups for comparison."""
    return sorted([sorted(group) for group in groups])


class TestGroupAnagramsBasic:
    """Basic functionality tests."""

    def test_example_1(self, group_anagrams):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        assert normalize_groups(result) == normalize_groups(expected)

    def test_empty_string(self, group_anagrams):
        result = group_anagrams([""])
        assert normalize_groups(result) == [[""]]

    def test_single_char(self, group_anagrams):
        result = group_anagrams(["a"])
        assert normalize_groups(result) == [["a"]]

    def test_no_anagrams(self, group_anagrams):
        result = group_anagrams(["abc", "def", "ghi"])
        expected = [["abc"], ["def"], ["ghi"]]
        assert normalize_groups(result) == normalize_groups(expected)


class TestGroupAnagramsEdgeCases:
    """Edge case tests."""

    def test_all_anagrams(self, group_anagrams):
        result = group_anagrams(["abc", "bca", "cab", "acb"])
        assert len(result) == 1
        assert sorted(result[0]) == ["abc", "acb", "bca", "cab"]

    def test_multiple_empty_strings(self, group_anagrams):
        result = group_anagrams(["", ""])
        assert normalize_groups(result) == [["", ""]]

    def test_same_letters_different_counts(self, group_anagrams):
        result = group_anagrams(["aab", "aba", "baa", "ab"])
        expected = [["aab", "aba", "baa"], ["ab"]]
        assert normalize_groups(result) == normalize_groups(expected)


@pytest.mark.performance
class TestGroupAnagramsPerformance:
    """Performance tests."""

    def test_large_input(self, group_anagrams):
        # Generate many anagrams
        strs = ["abc", "bca", "cab"] * 1000 + ["xyz", "zyx"] * 500

        start = time.time()
        result = group_anagrams(strs)
        elapsed = time.time() - start

        assert len(result) == 2
        assert elapsed < 1.0
