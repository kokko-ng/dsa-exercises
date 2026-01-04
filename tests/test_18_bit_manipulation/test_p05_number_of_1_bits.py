"""Tests for number_of_1_bits problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def number_of_1_bits():
    """Get the user's number_of_1_bits implementation."""
    func = get_function("number_of_1_bits")
    if func is None:
        pytest.skip("Function 'number_of_1_bits' not registered. Run check(number_of_1_bits) in notebook.")
    return func


class TestNumberOf1BitsBasic:
    """Basic functionality tests."""

    def test_example_11(self, number_of_1_bits):
        # 11 = 1011 in binary
        result = number_of_1_bits(11)
        assert result == 3

    def test_example_128(self, number_of_1_bits):
        # 128 = 10000000 in binary
        result = number_of_1_bits(128)
        assert result == 1

    def test_zero(self, number_of_1_bits):
        result = number_of_1_bits(0)
        assert result == 0

    def test_one(self, number_of_1_bits):
        result = number_of_1_bits(1)
        assert result == 1

    def test_power_of_two(self, number_of_1_bits):
        result = number_of_1_bits(1024)  # 2^10
        assert result == 1


class TestNumberOf1BitsEdgeCases:
    """Edge case tests."""

    def test_all_ones_8bit(self, number_of_1_bits):
        result = number_of_1_bits(255)  # 11111111
        assert result == 8

    def test_all_ones_16bit(self, number_of_1_bits):
        result = number_of_1_bits(65535)  # 16 ones
        assert result == 16

    def test_max_32bit(self, number_of_1_bits):
        result = number_of_1_bits(4294967295)  # 2^32 - 1
        assert result == 32

    def test_alternating_bits(self, number_of_1_bits):
        result = number_of_1_bits(0b10101010)  # 170
        assert result == 4

    def test_large_value(self, number_of_1_bits):
        result = number_of_1_bits(4294967293)  # 32 bits, 31 ones
        assert result == 31

    def test_near_max(self, number_of_1_bits):
        # 2^31 = 10000...0 (31 zeros)
        result = number_of_1_bits(2147483648)
        assert result == 1
