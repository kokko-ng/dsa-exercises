"""Tests for coin_change problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def coin_change():
    func = get_function("coin_change")
    if func is None:
        pytest.skip("Function 'coin_change' not registered.")
    return func


class TestCoinChangeBasic:
    def test_example_1(self, coin_change):
        assert coin_change([1, 2, 5], 11) == 3

    def test_example_2(self, coin_change):
        assert coin_change([2], 3) == -1

    def test_example_3(self, coin_change):
        assert coin_change([1], 0) == 0


class TestCoinChangeEdgeCases:
    def test_single_coin_exact(self, coin_change):
        assert coin_change([5], 10) == 2

    def test_large_amount(self, coin_change):
        assert coin_change([1, 2, 5], 100) == 20

    def test_impossible(self, coin_change):
        assert coin_change([3, 7], 5) == -1


@pytest.mark.performance
class TestCoinChangePerformance:
    def test_large_input(self, coin_change):
        start = time.time()
        result = coin_change([1, 2, 5], 10000)
        elapsed = time.time() - start

        assert result == 2000
        assert elapsed < 1.0
