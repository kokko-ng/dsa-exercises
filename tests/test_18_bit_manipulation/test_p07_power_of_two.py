"""Tests for power_of_two problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def power_of_two():
    """Get the user's power_of_two implementation."""
    func = get_function("power_of_two")
    if func is None:
        pytest.skip("Function 'power_of_two' not registered. Run check(power_of_two) in notebook.")
    return func


class TestPowerOfTwoBasic:
    """Basic functionality tests."""

    def test_one(self, power_of_two):
        # 2^0 = 1
        assert power_of_two(1) is True

    def test_two(self, power_of_two):
        # 2^1 = 2
        assert power_of_two(2) is True

    def test_sixteen(self, power_of_two):
        # 2^4 = 16
        assert power_of_two(16) is True

    def test_three(self, power_of_two):
        assert power_of_two(3) is False

    def test_five(self, power_of_two):
        assert power_of_two(5) is False


class TestPowerOfTwoEdgeCases:
    """Edge case tests."""

    def test_zero(self, power_of_two):
        assert power_of_two(0) is False

    def test_negative_one(self, power_of_two):
        assert power_of_two(-1) is False

    def test_negative_power_of_two(self, power_of_two):
        assert power_of_two(-16) is False

    def test_large_power_of_two(self, power_of_two):
        # 2^30
        assert power_of_two(1073741824) is True

    def test_large_non_power(self, power_of_two):
        assert power_of_two(1073741823) is False  # 2^30 - 1

    def test_all_powers_up_to_30(self, power_of_two):
        for i in range(31):
            assert power_of_two(2**i) is True

    def test_near_powers(self, power_of_two):
        for i in range(2, 20):
            assert power_of_two(2**i - 1) is False
            assert power_of_two(2**i + 1) is False
