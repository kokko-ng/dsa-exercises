"""Tests for find_duplicate_number problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def find_duplicate_number():
    func = get_function("find_duplicate_number")
    if func is None:
        pytest.skip("Function 'find_duplicate_number' not registered.")
    return func


class TestFindDuplicateBasic:
    def test_example_1(self, find_duplicate_number):
        assert find_duplicate_number([1, 3, 4, 2, 2]) == 2

    def test_example_2(self, find_duplicate_number):
        assert find_duplicate_number([3, 1, 3, 4, 2]) == 3

    def test_example_3(self, find_duplicate_number):
        assert find_duplicate_number([3, 3, 3, 3, 3]) == 3


class TestFindDuplicateEdgeCases:
    def test_two_elements(self, find_duplicate_number):
        assert find_duplicate_number([1, 1]) == 1

    def test_duplicate_at_beginning(self, find_duplicate_number):
        assert find_duplicate_number([2, 2, 1, 3, 4]) == 2

    def test_duplicate_at_end(self, find_duplicate_number):
        assert find_duplicate_number([1, 2, 3, 4, 4]) == 4

    def test_many_duplicates(self, find_duplicate_number):
        assert find_duplicate_number([2, 2, 2, 2, 2]) == 2


@pytest.mark.performance
class TestFindDuplicatePerformance:
    def test_large_input(self, find_duplicate_number):
        n = 100000
        nums = list(range(1, n + 1)) + [50000]

        start = time.time()
        result = find_duplicate_number(nums)
        elapsed = time.time() - start

        assert result == 50000
        assert elapsed < 1.0
