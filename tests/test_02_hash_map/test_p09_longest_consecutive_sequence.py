"""Tests for longest_consecutive_sequence problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def longest_consecutive_sequence():
    func = get_function("longest_consecutive_sequence")
    if func is None:
        pytest.skip("Function 'longest_consecutive_sequence' not registered.")
    return func


class TestLongestConsecutiveBasic:
    def test_example_1(self, longest_consecutive_sequence):
        assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4

    def test_example_2(self, longest_consecutive_sequence):
        assert longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

    def test_single_element(self, longest_consecutive_sequence):
        assert longest_consecutive_sequence([5]) == 1


class TestLongestConsecutiveEdgeCases:
    def test_empty_array(self, longest_consecutive_sequence):
        assert longest_consecutive_sequence([]) == 0

    def test_no_consecutive(self, longest_consecutive_sequence):
        assert longest_consecutive_sequence([10, 20, 30]) == 1

    def test_all_consecutive(self, longest_consecutive_sequence):
        assert longest_consecutive_sequence([1, 2, 3, 4, 5]) == 5

    def test_with_duplicates(self, longest_consecutive_sequence):
        assert longest_consecutive_sequence([1, 2, 2, 3]) == 3

    def test_negative_numbers(self, longest_consecutive_sequence):
        assert longest_consecutive_sequence([-3, -2, -1, 0, 1]) == 5


@pytest.mark.performance
class TestLongestConsecutivePerformance:
    def test_large_input(self, longest_consecutive_sequence):
        # Numbers scattered with a long consecutive sequence
        nums = list(range(50000)) + [100000, 100002, 100004]

        start = time.time()
        result = longest_consecutive_sequence(nums)
        elapsed = time.time() - start

        assert result == 50000
        assert elapsed < 1.0
