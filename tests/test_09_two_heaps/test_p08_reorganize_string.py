"""Tests for reorganize_string problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def reorganize_string():
    func = get_function("reorganize_string")
    if func is None:
        pytest.skip("Function 'reorganize_string' not registered.")
    return func


def is_valid_reorganization(s, result):
    """Check if result is a valid reorganization of s."""
    if not result:
        return False
    # Check same characters
    if sorted(s) != sorted(result):
        return False
    # Check no adjacent duplicates
    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            return False
    return True


class TestReorganizeStringBasic:
    def test_example_1(self, reorganize_string):
        result = reorganize_string("aab")
        assert is_valid_reorganization("aab", result)

    def test_example_2(self, reorganize_string):
        result = reorganize_string("aaab")
        assert result == ""

    def test_single_char(self, reorganize_string):
        result = reorganize_string("a")
        assert result == "a"

    def test_two_different(self, reorganize_string):
        result = reorganize_string("ab")
        assert is_valid_reorganization("ab", result)


class TestReorganizeStringEdgeCases:
    def test_all_same(self, reorganize_string):
        result = reorganize_string("aaaa")
        assert result == ""

    def test_balanced(self, reorganize_string):
        result = reorganize_string("aabb")
        assert is_valid_reorganization("aabb", result)

    def test_three_chars(self, reorganize_string):
        result = reorganize_string("aaabbc")
        assert is_valid_reorganization("aaabbc", result)

    def test_just_possible(self, reorganize_string):
        # 5 chars, max can be (5+1)/2 = 3
        result = reorganize_string("aaabb")
        assert is_valid_reorganization("aaabb", result)


@pytest.mark.performance
class TestReorganizeStringPerformance:
    def test_large_input(self, reorganize_string):
        # Create a string that can be reorganized
        s = "ab" * 250

        start = time.time()
        result = reorganize_string(s)
        elapsed = time.time() - start

        assert is_valid_reorganization(s, result)
        assert elapsed < 1.0
