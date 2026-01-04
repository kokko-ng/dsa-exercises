"""Tests for reverse_bits problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def reverse_bits():
    """Get the user's reverse_bits implementation."""
    func = get_function("reverse_bits")
    if func is None:
        pytest.skip("Function 'reverse_bits' not registered. Run check(reverse_bits) in notebook.")
    return func


class TestReverseBitsBasic:
    """Basic functionality tests."""

    def test_example_1(self, reverse_bits):
        # 43261596 -> 964176192
        result = reverse_bits(43261596)
        assert result == 964176192

    def test_example_2(self, reverse_bits):
        # 4294967293 -> 3221225471
        result = reverse_bits(4294967293)
        assert result == 3221225471

    def test_zero(self, reverse_bits):
        result = reverse_bits(0)
        assert result == 0

    def test_one(self, reverse_bits):
        # 1 = 00...001 -> 10...000 = 2^31
        result = reverse_bits(1)
        assert result == 2147483648

    def test_power_of_two(self, reverse_bits):
        # 2 = 00...010 -> 01...000 = 2^30
        result = reverse_bits(2)
        assert result == 1073741824


class TestReverseBitsEdgeCases:
    """Edge case tests."""

    def test_all_ones(self, reverse_bits):
        # All 1s stays all 1s
        result = reverse_bits(4294967295)
        assert result == 4294967295

    def test_half_ones(self, reverse_bits):
        # 0xFFFF0000 (16 ones, 16 zeros) -> 0x0000FFFF
        result = reverse_bits(0xFFFF0000)
        assert result == 0x0000FFFF

    def test_alternating(self, reverse_bits):
        # 0xAAAAAAAA (1010...) -> 0x55555555 (0101...)
        result = reverse_bits(0xAAAAAAAA)
        assert result == 0x55555555

    def test_palindrome(self, reverse_bits):
        # Some numbers are palindromes in binary
        # 0xFF0000FF stays same
        result = reverse_bits(0xFF0000FF)
        assert result == 0xFF0000FF

    def test_high_bit_set(self, reverse_bits):
        # 2^31 (1 followed by 31 zeros) -> 1
        result = reverse_bits(2147483648)
        assert result == 1
