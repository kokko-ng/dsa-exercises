"""Tests for counting_bits problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def counting_bits():
    """Get the user's counting_bits implementation."""
    func = get_function("counting_bits")
    if func is None:
        pytest.skip("Function 'counting_bits' not registered. Run check(counting_bits) in notebook.")
    return func


class TestCountingBitsBasic:
    """Basic functionality tests."""

    def test_n_equals_2(self, counting_bits):
        result = counting_bits(2)
        assert result == [0, 1, 1]

    def test_n_equals_5(self, counting_bits):
        result = counting_bits(5)
        assert result == [0, 1, 1, 2, 1, 2]

    def test_n_equals_0(self, counting_bits):
        result = counting_bits(0)
        assert result == [0]

    def test_n_equals_1(self, counting_bits):
        result = counting_bits(1)
        assert result == [0, 1]

    def test_n_equals_10(self, counting_bits):
        result = counting_bits(10)
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
        assert result == expected


class TestCountingBitsEdgeCases:
    """Edge case tests."""

    def test_power_of_two(self, counting_bits):
        result = counting_bits(8)
        # 0:0, 1:1, 2:1, 3:2, 4:1, 5:2, 6:2, 7:3, 8:1
        assert result == [0, 1, 1, 2, 1, 2, 2, 3, 1]

    def test_n_equals_15(self, counting_bits):
        result = counting_bits(15)
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
        assert result == expected

    def test_n_equals_16(self, counting_bits):
        result = counting_bits(16)
        assert len(result) == 17
        assert result[16] == 1  # 10000 has 1 bit


@pytest.mark.performance
class TestCountingBitsPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, counting_bits):
        n = 100000

        start = time.time()
        result = counting_bits(n)
        elapsed = time.time() - start

        assert len(result) == n + 1
        assert result[0] == 0
        assert result[1] == 1
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
