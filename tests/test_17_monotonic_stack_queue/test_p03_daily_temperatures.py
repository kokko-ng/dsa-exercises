"""Tests for daily_temperatures problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def daily_temperatures():
    """Get the user's daily_temperatures implementation."""
    func = get_function("daily_temperatures")
    if func is None:
        pytest.skip("Function 'daily_temperatures' not registered. Run check(daily_temperatures) in notebook.")
    return func


class TestDailyTemperaturesBasic:
    """Basic functionality tests."""

    def test_mixed_temperatures(self, daily_temperatures):
        result = daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
        assert result == [1, 1, 4, 2, 1, 1, 0, 0]

    def test_increasing(self, daily_temperatures):
        result = daily_temperatures([30, 40, 50, 60])
        assert result == [1, 1, 1, 0]

    def test_simple_increasing(self, daily_temperatures):
        result = daily_temperatures([30, 60, 90])
        assert result == [1, 1, 0]

    def test_decreasing(self, daily_temperatures):
        result = daily_temperatures([90, 80, 70, 60])
        assert result == [0, 0, 0, 0]

    def test_constant(self, daily_temperatures):
        result = daily_temperatures([50, 50, 50, 50])
        assert result == [0, 0, 0, 0]


class TestDailyTemperaturesEdgeCases:
    """Edge case tests."""

    def test_single_day(self, daily_temperatures):
        result = daily_temperatures([75])
        assert result == [0]

    def test_two_days_warmer(self, daily_temperatures):
        result = daily_temperatures([70, 80])
        assert result == [1, 0]

    def test_two_days_colder(self, daily_temperatures):
        result = daily_temperatures([80, 70])
        assert result == [0, 0]

    def test_valley_pattern(self, daily_temperatures):
        result = daily_temperatures([80, 60, 70, 90])
        assert result == [3, 1, 1, 0]

    def test_peak_pattern(self, daily_temperatures):
        result = daily_temperatures([60, 80, 90, 70])
        assert result == [1, 1, 0, 0]


@pytest.mark.performance
class TestDailyTemperaturesPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, daily_temperatures):
        n = 100000
        temps = list(range(30, 30 + n))  # Increasing temperatures

        start = time.time()
        result = daily_temperatures(temps)
        elapsed = time.time() - start

        expected = [1] * (n - 1) + [0]
        assert result == expected
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
