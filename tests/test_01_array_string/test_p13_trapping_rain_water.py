"""Tests for trapping_rain_water problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def trapping_rain_water():
    func = get_function("trapping_rain_water")
    if func is None:
        pytest.skip("Function 'trapping_rain_water' not registered.")
    return func


class TestTrappingRainWaterBasic:
    def test_example_1(self, trapping_rain_water):
        assert trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    def test_example_2(self, trapping_rain_water):
        assert trapping_rain_water([4, 2, 0, 3, 2, 5]) == 9

    def test_simple_valley(self, trapping_rain_water):
        assert trapping_rain_water([3, 0, 3]) == 3


class TestTrappingRainWaterEdgeCases:
    def test_no_trap(self, trapping_rain_water):
        assert trapping_rain_water([1, 2, 3, 4, 5]) == 0

    def test_decreasing(self, trapping_rain_water):
        assert trapping_rain_water([5, 4, 3, 2, 1]) == 0

    def test_single_element(self, trapping_rain_water):
        assert trapping_rain_water([5]) == 0

    def test_two_elements(self, trapping_rain_water):
        assert trapping_rain_water([5, 5]) == 0

    def test_empty(self, trapping_rain_water):
        assert trapping_rain_water([]) == 0

    def test_all_zeros(self, trapping_rain_water):
        assert trapping_rain_water([0, 0, 0]) == 0


@pytest.mark.performance
class TestTrappingRainWaterPerformance:
    def test_large_input(self, trapping_rain_water):
        n = 20000
        # Create alternating pattern
        height = [i % 100 for i in range(n)]

        start = time.time()
        result = trapping_rain_water(height)
        elapsed = time.time() - start

        assert result >= 0
        assert elapsed < 1.0
