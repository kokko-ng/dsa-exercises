"""Tests for alien_dictionary problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


def is_valid_order(order, words):
    """Check if the order produces a valid sorted word list."""
    if not order:
        return False

    char_rank = {c: i for i, c in enumerate(order)}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                if char_rank.get(w1[j], -1) > char_rank.get(w2[j], -1):
                    return False
                break
        else:
            if len(w1) > len(w2):
                return False

    return True


@pytest.fixture
def alien_dictionary():
    func = get_function("alien_dictionary")
    if func is None:
        pytest.skip("Function 'alien_dictionary' not registered.")
    return func


class TestAlienDictionaryBasic:
    def test_example_1(self, alien_dictionary):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        result = alien_dictionary(words)
        assert is_valid_order(result, words)

    def test_simple(self, alien_dictionary):
        words = ["z", "x"]
        result = alien_dictionary(words)
        assert is_valid_order(result, words)

    def test_three_words(self, alien_dictionary):
        words = ["ab", "ac", "bc"]
        result = alien_dictionary(words)
        assert is_valid_order(result, words)


class TestAlienDictionaryEdgeCases:
    def test_invalid_order(self, alien_dictionary):
        words = ["z", "x", "z"]
        result = alien_dictionary(words)
        assert result == ""

    def test_invalid_prefix(self, alien_dictionary):
        words = ["abc", "ab"]
        result = alien_dictionary(words)
        assert result == ""

    def test_single_word(self, alien_dictionary):
        words = ["abc"]
        result = alien_dictionary(words)
        assert set(result) == {'a', 'b', 'c'}

    def test_same_words(self, alien_dictionary):
        words = ["a", "a"]
        result = alien_dictionary(words)
        assert result == "a"
