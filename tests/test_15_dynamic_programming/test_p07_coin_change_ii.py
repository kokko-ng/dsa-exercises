"""Tests for coin_change_ii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def coin_change_ii():
    func = get_function("coin_change_ii")
    if func is None:
        pytest.skip("Function 'coin_change_ii' not registered.")
    return func


class TestCoinChangeIIBasic:
    def test_example_1(self, coin_change_ii):
        assert coin_change_ii(5, [1, 2, 5]) == 4

    def test_example_2(self, coin_change_ii):
        assert coin_change_ii(3, [2]) == 0

    def test_example_3(self, coin_change_ii):
        assert coin_change_ii(10, [10]) == 1


class TestCoinChangeIIEdgeCases:
    def test_zero_amount(self, coin_change_ii):
        assert coin_change_ii(0, [1, 2, 5]) == 1

    def test_single_coin(self, coin_change_ii):
        assert coin_change_ii(5, [1]) == 1

    def test_multiple_ways(self, coin_change_ii):
        assert coin_change_ii(4, [1, 2]) == 3  # 1111, 112, 22


@pytest.mark.performance
class TestCoinChangeIIPerformance:
    def test_large_input(self, coin_change_ii):
        start = time.time()
        result = coin_change_ii(500, [1, 2, 5])
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0
