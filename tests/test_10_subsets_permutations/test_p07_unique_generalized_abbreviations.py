"""Tests for unique_generalized_abbreviations problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def unique_generalized_abbreviations():
    func = get_function("unique_generalized_abbreviations")
    if func is None:
        pytest.skip("Function 'unique_generalized_abbreviations' not registered.")
    return func


class TestUniqueGeneralizedAbbreviationsBasic:
    def test_example_1(self, unique_generalized_abbreviations):
        result = unique_generalized_abbreviations("word")
        # 2^4 = 16 abbreviations
        assert len(result) == 16
        assert "word" in result
        assert "4" in result
        assert "w3" in result
        assert "1o1d" in result

    def test_example_2(self, unique_generalized_abbreviations):
        result = unique_generalized_abbreviations("a")
        assert len(result) == 2
        assert "a" in result
        assert "1" in result


class TestUniqueGeneralizedAbbreviationsEdgeCases:
    def test_two_chars(self, unique_generalized_abbreviations):
        result = unique_generalized_abbreviations("ab")
        expected = ["ab", "a1", "1b", "2"]
        assert len(result) == 4
        for abbr in expected:
            assert abbr in result

    def test_three_chars(self, unique_generalized_abbreviations):
        result = unique_generalized_abbreviations("abc")
        assert len(result) == 8  # 2^3


@pytest.mark.performance
class TestUniqueGeneralizedAbbreviationsPerformance:
    def test_long_word(self, unique_generalized_abbreviations):
        word = "abcdefghij"  # 10 chars = 2^10 = 1024

        start = time.time()
        result = unique_generalized_abbreviations(word)
        elapsed = time.time() - start

        assert len(result) == 1024
        assert elapsed < 2.0
