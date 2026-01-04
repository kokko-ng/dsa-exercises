"""Tests for longest_string_chain problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def longest_string_chain():
    func = get_function("longest_string_chain")
    if func is None:
        pytest.skip("Function 'longest_string_chain' not registered.")
    return func


class TestLongestStringChainBasic:
    def test_example_1(self, longest_string_chain):
        assert longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4

    def test_example_2(self, longest_string_chain):
        assert longest_string_chain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5


class TestLongestStringChainEdgeCases:
    def test_single_word(self, longest_string_chain):
        assert longest_string_chain(["a"]) == 1

    def test_no_chain(self, longest_string_chain):
        assert longest_string_chain(["abc", "def", "ghi"]) == 1

    def test_all_same_length(self, longest_string_chain):
        assert longest_string_chain(["ab", "cd", "ef"]) == 1


@pytest.mark.performance
class TestLongestStringChainPerformance:
    def test_large_input(self, longest_string_chain):
        words = ["a" * i for i in range(1, 17)]

        start = time.time()
        result = longest_string_chain(words)
        elapsed = time.time() - start

        assert result == 16
        assert elapsed < 1.0
