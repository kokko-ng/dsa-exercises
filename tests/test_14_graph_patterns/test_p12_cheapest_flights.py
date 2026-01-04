"""Tests for cheapest_flights problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def cheapest_flights():
    func = get_function("cheapest_flights")
    if func is None:
        pytest.skip("Function 'cheapest_flights' not registered.")
    return func


class TestCheapestFlightsBasic:
    def test_example_1(self, cheapest_flights):
        flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        assert cheapest_flights(4, flights, 0, 3, 1) == 700

    def test_example_2(self, cheapest_flights):
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        assert cheapest_flights(3, flights, 0, 2, 1) == 200

    def test_example_3(self, cheapest_flights):
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        assert cheapest_flights(3, flights, 0, 2, 0) == 500


class TestCheapestFlightsEdgeCases:
    def test_no_path(self, cheapest_flights):
        flights = [[0, 1, 100]]
        assert cheapest_flights(3, flights, 0, 2, 1) == -1

    def test_direct_flight(self, cheapest_flights):
        flights = [[0, 1, 100]]
        assert cheapest_flights(2, flights, 0, 1, 0) == 100

    def test_too_many_stops_needed(self, cheapest_flights):
        flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100]]
        assert cheapest_flights(4, flights, 0, 3, 1) == -1


@pytest.mark.performance
class TestCheapestFlightsPerformance:
    def test_large_input(self, cheapest_flights):
        n = 100
        flights = [[i, j, (i + j) % 100 + 1] for i in range(n) for j in range(n) if i != j]

        start = time.time()
        result = cheapest_flights(n, flights[:1000], 0, n - 1, 50)
        elapsed = time.time() - start

        assert elapsed < 2.0
