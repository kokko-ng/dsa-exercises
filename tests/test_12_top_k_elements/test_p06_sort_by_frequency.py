"""Tests for sort_by_frequency problem."""
import pytest
import time
from collections import Counter
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def sort_by_frequency():
    func = get_function("sort_by_frequency")
    if func is None:
        pytest.skip("Function 'sort_by_frequency' not registered.")
    return func


class TestSortByFrequencyBasic:
    """Basic functionality tests."""

    def test_standard_case(self, sort_by_frequency):
        result = sort_by_frequency("tree")
        assert result in ["eert", "eetr"]

    def test_same_frequency(self, sort_by_frequency):
        result = sort_by_frequency("cccaaa")
        assert result in ["cccaaa", "aaaccc"]

    def test_case_sensitive(self, sort_by_frequency):
        result = sort_by_frequency("Aabb")
        # 'b' appears twice, 'A' and 'a' each once
        assert result.startswith("bb")
        assert Counter(result) == Counter("Aabb")


class TestSortByFrequencyEdgeCases:
    """Edge case tests."""

    def test_single_char(self, sort_by_frequency):
        assert sort_by_frequency("a") == "a"

    def test_all_same(self, sort_by_frequency):
        assert sort_by_frequency("aaaa") == "aaaa"

    def test_all_unique(self, sort_by_frequency):
        result = sort_by_frequency("abc")
        assert Counter(result) == Counter("abc")

    def test_with_digits(self, sort_by_frequency):
        result = sort_by_frequency("2a554442f544asfasssffffasss")
        count = Counter(result)
        # Verify result has same characters
        assert count == Counter("2a554442f544asfasssffffasss")


@pytest.mark.performance
class TestSortByFrequencyPerformance:
    """Performance tests."""

    def test_large_input(self, sort_by_frequency):
        s = "abcdefghij" * 10000

        start = time.time()
        result = sort_by_frequency(s)
        elapsed = time.time() - start

        assert len(result) == len(s)
        assert Counter(result) == Counter(s)
        assert elapsed < 1.0
