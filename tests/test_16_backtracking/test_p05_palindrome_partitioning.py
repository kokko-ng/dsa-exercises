"""Tests for palindrome_partitioning problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def palindrome_partitioning():
    func = get_function("palindrome_partitioning")
    if func is None:
        pytest.skip("Function 'palindrome_partitioning' not registered.")
    return func


class TestPalindromePartitioningBasic:
    def test_example_1(self, palindrome_partitioning):
        result = palindrome_partitioning("aab")
        expected = [["a", "a", "b"], ["aa", "b"]]
        assert sorted([tuple(r) for r in result]) == sorted([tuple(e) for e in expected])

    def test_example_2(self, palindrome_partitioning):
        result = palindrome_partitioning("a")
        assert result == [["a"]]


class TestPalindromePartitioningEdgeCases:
    def test_all_same(self, palindrome_partitioning):
        result = palindrome_partitioning("aaa")
        # Should have multiple partitions
        assert len(result) == 4  # [a,a,a], [aa,a], [a,aa], [aaa]

    def test_no_palindrome_longer_than_1(self, palindrome_partitioning):
        result = palindrome_partitioning("abc")
        assert result == [["a", "b", "c"]]

    def test_whole_palindrome(self, palindrome_partitioning):
        result = palindrome_partitioning("aba")
        # Should include ["aba"] as one option
        assert ["aba"] in result
