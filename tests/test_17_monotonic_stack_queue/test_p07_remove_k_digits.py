"""Tests for remove_k_digits problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def remove_k_digits():
    """Get the user's remove_k_digits implementation."""
    func = get_function("remove_k_digits")
    if func is None:
        pytest.skip("Function 'remove_k_digits' not registered. Run check(remove_k_digits) in notebook.")
    return func


class TestRemoveKDigitsBasic:
    """Basic functionality tests."""

    def test_example_case(self, remove_k_digits):
        result = remove_k_digits("1432219", 3)
        assert result == "1219"

    def test_leading_zeros(self, remove_k_digits):
        result = remove_k_digits("10200", 1)
        assert result == "200"

    def test_remove_all(self, remove_k_digits):
        result = remove_k_digits("10", 2)
        assert result == "0"

    def test_remove_from_increasing(self, remove_k_digits):
        result = remove_k_digits("12345", 2)
        assert result == "123"

    def test_remove_from_decreasing(self, remove_k_digits):
        result = remove_k_digits("54321", 2)
        assert result == "321"


class TestRemoveKDigitsEdgeCases:
    """Edge case tests."""

    def test_single_digit_remove(self, remove_k_digits):
        result = remove_k_digits("9", 1)
        assert result == "0"

    def test_all_same_digits(self, remove_k_digits):
        result = remove_k_digits("1111", 2)
        assert result == "11"

    def test_all_nines(self, remove_k_digits):
        result = remove_k_digits("99999", 3)
        assert result == "99"

    def test_zero_in_middle(self, remove_k_digits):
        result = remove_k_digits("10001", 1)
        assert result == "1"

    def test_multiple_leading_zeros(self, remove_k_digits):
        result = remove_k_digits("100200", 2)
        assert result == "0"

    def test_k_equals_zero(self, remove_k_digits):
        result = remove_k_digits("12345", 0)
        assert result == "12345"


@pytest.mark.performance
class TestRemoveKDigitsPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, remove_k_digits):
        n = 100000
        num = "9" * n

        start = time.time()
        result = remove_k_digits(num, n // 2)
        elapsed = time.time() - start

        assert result == "9" * (n // 2)
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
