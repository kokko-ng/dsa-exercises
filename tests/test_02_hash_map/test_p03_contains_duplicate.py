"""Tests for contains_duplicate problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def contains_duplicate():
    func = get_function("contains_duplicate")
    if func is None:
        pytest.skip("Function 'contains_duplicate' not registered.")
    return func


class TestContainsDuplicateBasic:
    def test_has_duplicate(self, contains_duplicate):
        assert contains_duplicate([1, 2, 3, 1]) is True

    def test_no_duplicate(self, contains_duplicate):
        assert contains_duplicate([1, 2, 3, 4]) is False

    def test_multiple_duplicates(self, contains_duplicate):
        assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


class TestContainsDuplicateEdgeCases:
    def test_single_element(self, contains_duplicate):
        assert contains_duplicate([1]) is False

    def test_two_same(self, contains_duplicate):
        assert contains_duplicate([5, 5]) is True

    def test_two_different(self, contains_duplicate):
        assert contains_duplicate([5, 6]) is False

    def test_negative_numbers(self, contains_duplicate):
        assert contains_duplicate([-1, -2, -3, -1]) is True

    def test_zeros(self, contains_duplicate):
        assert contains_duplicate([0, 0]) is True


@pytest.mark.performance
class TestContainsDuplicatePerformance:
    def test_large_no_duplicate(self, contains_duplicate):
        nums = list(range(100000))

        start = time.time()
        result = contains_duplicate(nums)
        elapsed = time.time() - start

        assert result is False
        assert elapsed < 1.0

    def test_large_with_duplicate_at_end(self, contains_duplicate):
        nums = list(range(99999)) + [0]

        start = time.time()
        result = contains_duplicate(nums)
        elapsed = time.time() - start

        assert result is True
        assert elapsed < 1.0
