"""Tests for longest_repeating_character_replacement problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def longest_repeating_character_replacement():
    func = get_function("longest_repeating_character_replacement")
    if func is None:
        pytest.skip("Function 'longest_repeating_character_replacement' not registered.")
    return func


class TestLongestRepeatingBasic:
    def test_example_1(self, longest_repeating_character_replacement):
        assert longest_repeating_character_replacement("ABAB", 2) == 4

    def test_example_2(self, longest_repeating_character_replacement):
        assert longest_repeating_character_replacement("AABABBA", 1) == 4


class TestLongestRepeatingEdgeCases:
    def test_all_same(self, longest_repeating_character_replacement):
        assert longest_repeating_character_replacement("AAAA", 2) == 4

    def test_k_zero(self, longest_repeating_character_replacement):
        assert longest_repeating_character_replacement("ABAB", 0) == 1

    def test_single_char(self, longest_repeating_character_replacement):
        assert longest_repeating_character_replacement("A", 1) == 1

    def test_k_greater_than_length(self, longest_repeating_character_replacement):
        assert longest_repeating_character_replacement("ABC", 5) == 3


@pytest.mark.performance
class TestLongestRepeatingPerformance:
    def test_large_input(self, longest_repeating_character_replacement):
        s = "ABCD" * 25000

        start = time.time()
        result = longest_repeating_character_replacement(s, 50000)
        elapsed = time.time() - start

        assert elapsed < 1.0
