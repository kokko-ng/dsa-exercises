"""Tests for burst_balloons problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def burst_balloons():
    func = get_function("burst_balloons")
    if func is None:
        pytest.skip("Function 'burst_balloons' not registered.")
    return func


class TestBurstBalloonsBasic:
    def test_example_1(self, burst_balloons):
        assert burst_balloons([3, 1, 5, 8]) == 167

    def test_example_2(self, burst_balloons):
        assert burst_balloons([1, 5]) == 10


class TestBurstBalloonsEdgeCases:
    def test_single_balloon(self, burst_balloons):
        assert burst_balloons([3]) == 3

    def test_two_same(self, burst_balloons):
        assert burst_balloons([5, 5]) == 30  # 5*5 + 5 = 30

    def test_zeros(self, burst_balloons):
        assert burst_balloons([0, 1, 0]) == 0


@pytest.mark.performance
class TestBurstBalloonsPerformance:
    def test_medium_input(self, burst_balloons):
        nums = [i % 10 + 1 for i in range(100)]

        start = time.time()
        result = burst_balloons(nums)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 5.0
