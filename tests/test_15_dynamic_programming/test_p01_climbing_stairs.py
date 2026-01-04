"""Tests for climbing_stairs problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def climbing_stairs():
    func = get_function("climbing_stairs")
    if func is None:
        pytest.skip("Function 'climbing_stairs' not registered.")
    return func


class TestClimbingStairsBasic:
    def test_two_stairs(self, climbing_stairs):
        assert climbing_stairs(2) == 2

    def test_three_stairs(self, climbing_stairs):
        assert climbing_stairs(3) == 3

    def test_one_stair(self, climbing_stairs):
        assert climbing_stairs(1) == 1

    def test_five_stairs(self, climbing_stairs):
        assert climbing_stairs(5) == 8


class TestClimbingStairsEdgeCases:
    def test_ten_stairs(self, climbing_stairs):
        assert climbing_stairs(10) == 89

    def test_twenty_stairs(self, climbing_stairs):
        assert climbing_stairs(20) == 10946


@pytest.mark.performance
class TestClimbingStairsPerformance:
    def test_large_input(self, climbing_stairs):
        start = time.time()
        result = climbing_stairs(45)
        elapsed = time.time() - start

        assert result == 1836311903
        assert elapsed < 1.0
