"""Tests for decode_ways problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def decode_ways():
    func = get_function("decode_ways")
    if func is None:
        pytest.skip("Function 'decode_ways' not registered.")
    return func


class TestDecodeWaysBasic:
    def test_example_1(self, decode_ways):
        assert decode_ways("12") == 2

    def test_example_2(self, decode_ways):
        assert decode_ways("226") == 3

    def test_example_3(self, decode_ways):
        assert decode_ways("06") == 0


class TestDecodeWaysEdgeCases:
    def test_single_digit(self, decode_ways):
        assert decode_ways("1") == 1

    def test_zero_start(self, decode_ways):
        assert decode_ways("0") == 0

    def test_contains_zero(self, decode_ways):
        assert decode_ways("10") == 1

    def test_invalid_zero(self, decode_ways):
        assert decode_ways("100") == 0

    def test_all_ones(self, decode_ways):
        assert decode_ways("111") == 3


@pytest.mark.performance
class TestDecodeWaysPerformance:
    def test_large_input(self, decode_ways):
        s = "1" * 100

        start = time.time()
        result = decode_ways(s)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0
