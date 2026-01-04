"""Tests for min_cost_climbing_stairs problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def min_cost_climbing_stairs():
    func = get_function("min_cost_climbing_stairs")
    if func is None:
        pytest.skip("Function 'min_cost_climbing_stairs' not registered.")
    return func


class TestMinCostClimbingStairsBasic:
    def test_example_1(self, min_cost_climbing_stairs):
        assert min_cost_climbing_stairs([10, 15, 20]) == 15

    def test_example_2(self, min_cost_climbing_stairs):
        assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


class TestMinCostClimbingStairsEdgeCases:
    def test_two_stairs(self, min_cost_climbing_stairs):
        assert min_cost_climbing_stairs([10, 15]) == 10

    def test_all_same(self, min_cost_climbing_stairs):
        assert min_cost_climbing_stairs([5, 5, 5, 5]) == 10

    def test_increasing(self, min_cost_climbing_stairs):
        assert min_cost_climbing_stairs([1, 2, 3, 4, 5]) == 6


@pytest.mark.performance
class TestMinCostClimbingStairsPerformance:
    def test_large_input(self, min_cost_climbing_stairs):
        cost = [i % 100 for i in range(1000)]

        start = time.time()
        result = min_cost_climbing_stairs(cost)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0
