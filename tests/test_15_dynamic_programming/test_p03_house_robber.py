"""Tests for house_robber problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def house_robber():
    func = get_function("house_robber")
    if func is None:
        pytest.skip("Function 'house_robber' not registered.")
    return func


class TestHouseRobberBasic:
    def test_example_1(self, house_robber):
        assert house_robber([1, 2, 3, 1]) == 4

    def test_example_2(self, house_robber):
        assert house_robber([2, 7, 9, 3, 1]) == 12

    def test_single_house(self, house_robber):
        assert house_robber([5]) == 5


class TestHouseRobberEdgeCases:
    def test_two_houses(self, house_robber):
        assert house_robber([1, 2]) == 2

    def test_all_same(self, house_robber):
        assert house_robber([5, 5, 5, 5]) == 10

    def test_decreasing(self, house_robber):
        assert house_robber([10, 5, 3, 1]) == 13

    def test_empty(self, house_robber):
        assert house_robber([]) == 0


@pytest.mark.performance
class TestHouseRobberPerformance:
    def test_large_input(self, house_robber):
        nums = [i % 100 for i in range(100)]

        start = time.time()
        result = house_robber(nums)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0
