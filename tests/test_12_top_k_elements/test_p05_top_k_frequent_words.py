"""Tests for top_k_frequent_words problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def top_k_frequent_words():
    func = get_function("top_k_frequent_words")
    if func is None:
        pytest.skip("Function 'top_k_frequent_words' not registered.")
    return func


class TestTopKFrequentWordsBasic:
    """Basic functionality tests."""

    def test_standard_case(self, top_k_frequent_words):
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        result = top_k_frequent_words(words, 2)
        assert result == ["i", "love"]

    def test_alphabetical_tiebreaker(self, top_k_frequent_words):
        words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
        result = top_k_frequent_words(words, 4)
        assert result == ["the", "is", "sunny", "day"]

    def test_k_equals_1(self, top_k_frequent_words):
        words = ["a", "b", "a"]
        result = top_k_frequent_words(words, 1)
        assert result == ["a"]


class TestTopKFrequentWordsEdgeCases:
    """Edge case tests."""

    def test_single_word(self, top_k_frequent_words):
        assert top_k_frequent_words(["hello"], 1) == ["hello"]

    def test_all_unique(self, top_k_frequent_words):
        words = ["a", "b", "c"]
        result = top_k_frequent_words(words, 3)
        assert result == ["a", "b", "c"]  # Alphabetical order

    def test_same_frequency_alphabetical(self, top_k_frequent_words):
        words = ["z", "a", "m"]
        result = top_k_frequent_words(words, 2)
        assert result == ["a", "m"]  # Alphabetical order

    def test_all_same_word(self, top_k_frequent_words):
        result = top_k_frequent_words(["test", "test", "test"], 1)
        assert result == ["test"]


@pytest.mark.performance
class TestTopKFrequentWordsPerformance:
    """Performance tests."""

    def test_large_input(self, top_k_frequent_words):
        words = ["word" + str(i % 100) for i in range(10000)]

        start = time.time()
        result = top_k_frequent_words(words, 10)
        elapsed = time.time() - start

        assert len(result) == 10
        assert elapsed < 1.0
