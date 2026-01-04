"""Tests for connect_ropes problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def connect_ropes():
    func = get_function("connect_ropes")
    if func is None:
        pytest.skip("Function 'connect_ropes' not registered.")
    return func


class TestConnectRopesBasic:
    """Basic functionality tests."""

    def test_standard_case(self, connect_ropes):
        assert connect_ropes([1, 2, 3, 4, 5]) == 33

    def test_four_ropes(self, connect_ropes):
        assert connect_ropes([1, 3, 11, 5]) == 33

    def test_two_ropes(self, connect_ropes):
        assert connect_ropes([2, 3]) == 5


class TestConnectRopesEdgeCases:
    """Edge case tests."""

    def test_single_rope(self, connect_ropes):
        assert connect_ropes([5]) == 0

    def test_same_length_ropes(self, connect_ropes):
        assert connect_ropes([4, 4, 4, 4]) == 32  # 8+16+8 = 32? Let me recalculate
        # 4+4=8 (cost 8), 4+4=8 (cost 8), 8+8=16 (cost 16)
        # Total = 8+8+16 = 32

    def test_sorted_ascending(self, connect_ropes):
        assert connect_ropes([1, 2, 3]) == 9  # 1+2=3 (cost 3), 3+3=6 (cost 6) = 9

    def test_sorted_descending(self, connect_ropes):
        assert connect_ropes([5, 4, 3, 2, 1]) == 33


@pytest.mark.performance
class TestConnectRopesPerformance:
    """Performance tests."""

    def test_large_input(self, connect_ropes):
        ropes = list(range(1, 10001))

        start = time.time()
        result = connect_ropes(ropes)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0
