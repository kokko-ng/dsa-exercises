"""Tests for minimum_platforms problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def minimum_platforms():
    """Get the user's minimum_platforms implementation."""
    func = get_function("minimum_platforms")
    if func is None:
        pytest.skip("Function 'minimum_platforms' not registered. Run check(minimum_platforms) in notebook.")
    return func


class TestMinimumPlatformsBasic:
    """Basic functionality tests."""

    def test_three_platforms(self, minimum_platforms):
        arrivals = [900, 940, 950, 1100, 1500, 1800]
        departures = [910, 1200, 1120, 1130, 1900, 2000]
        result = minimum_platforms(arrivals, departures)
        assert result == 3

    def test_one_platform(self, minimum_platforms):
        arrivals = [900, 1100, 1235]
        departures = [1000, 1200, 1240]
        result = minimum_platforms(arrivals, departures)
        assert result == 1

    def test_all_overlap(self, minimum_platforms):
        arrivals = [100, 100, 100]
        departures = [200, 200, 200]
        result = minimum_platforms(arrivals, departures)
        assert result == 3

    def test_sequential(self, minimum_platforms):
        arrivals = [100, 200, 300]
        departures = [150, 250, 350]
        result = minimum_platforms(arrivals, departures)
        assert result == 1


class TestMinimumPlatformsEdgeCases:
    """Edge case tests."""

    def test_single_train(self, minimum_platforms):
        result = minimum_platforms([900], [1000])
        assert result == 1

    def test_same_arrival_as_departure(self, minimum_platforms):
        arrivals = [900, 1000]
        departures = [1000, 1100]
        result = minimum_platforms(arrivals, departures)
        assert result == 2  # Both at platform at time 1000

    def test_two_platforms(self, minimum_platforms):
        arrivals = [900, 950, 1100]
        departures = [1000, 1050, 1200]
        result = minimum_platforms(arrivals, departures)
        assert result == 2


@pytest.mark.performance
class TestMinimumPlatformsPerformance:
    """Performance tests."""

    def test_large_input(self, minimum_platforms):
        n = 10000
        arrivals = list(range(0, n * 2, 2))
        departures = list(range(100, n * 2 + 100, 2))

        start = time.time()
        result = minimum_platforms(arrivals, departures)
        elapsed = time.time() - start

        assert result == 50
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
