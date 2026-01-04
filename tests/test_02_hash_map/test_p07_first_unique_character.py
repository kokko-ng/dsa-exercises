"""Tests for first_unique_character problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def first_unique_character():
    func = get_function("first_unique_character")
    if func is None:
        pytest.skip("Function 'first_unique_character' not registered.")
    return func


class TestFirstUniqueCharacterBasic:
    def test_example_1(self, first_unique_character):
        assert first_unique_character("leetcode") == 0

    def test_example_2(self, first_unique_character):
        assert first_unique_character("loveleetcode") == 2

    def test_example_3(self, first_unique_character):
        assert first_unique_character("aabb") == -1


class TestFirstUniqueCharacterEdgeCases:
    def test_single_char(self, first_unique_character):
        assert first_unique_character("a") == 0

    def test_all_same(self, first_unique_character):
        assert first_unique_character("aaaa") == -1

    def test_unique_at_end(self, first_unique_character):
        assert first_unique_character("aabbccd") == 6

    def test_all_unique(self, first_unique_character):
        assert first_unique_character("abcdef") == 0

    def test_two_chars(self, first_unique_character):
        assert first_unique_character("ab") == 0


@pytest.mark.performance
class TestFirstUniqueCharacterPerformance:
    def test_large_input(self, first_unique_character):
        s = "abcdefghij" * 10000 + "z"

        start = time.time()
        result = first_unique_character(s)
        elapsed = time.time() - start

        assert result == 100000
        assert elapsed < 1.0
