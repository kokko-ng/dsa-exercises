"""Tests for car_pooling problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def car_pooling():
    """Get the user's car_pooling implementation."""
    func = get_function("car_pooling")
    if func is None:
        pytest.skip("Function 'car_pooling' not registered. Run check(car_pooling) in notebook.")
    return func


class TestCarPoolingBasic:
    """Basic functionality tests."""

    def test_over_capacity(self, car_pooling):
        result = car_pooling([[2, 1, 5], [3, 3, 7]], 4)
        assert result == False

    def test_at_capacity(self, car_pooling):
        result = car_pooling([[2, 1, 5], [3, 3, 7]], 5)
        assert result == True

    def test_sequential_trips(self, car_pooling):
        result = car_pooling([[2, 1, 5], [3, 5, 7]], 3)
        assert result == True

    def test_single_trip(self, car_pooling):
        result = car_pooling([[5, 0, 10]], 5)
        assert result == True


class TestCarPoolingEdgeCases:
    """Edge case tests."""

    def test_single_trip_over_capacity(self, car_pooling):
        result = car_pooling([[5, 0, 10]], 4)
        assert result == False

    def test_multiple_pickups_same_location(self, car_pooling):
        result = car_pooling([[2, 1, 5], [3, 1, 5]], 5)
        assert result == True

    def test_drop_before_pickup(self, car_pooling):
        result = car_pooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11)
        assert result == True

    def test_all_same_trip(self, car_pooling):
        result = car_pooling([[2, 0, 5], [2, 0, 5], [2, 0, 5]], 6)
        assert result == True


@pytest.mark.performance
class TestCarPoolingPerformance:
    """Performance tests."""

    def test_large_input(self, car_pooling):
        n = 1000
        trips = [[1, i, i + 10] for i in range(n)]
        capacity = 10

        start = time.time()
        result = car_pooling(trips, capacity)
        elapsed = time.time() - start

        assert result == True
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
