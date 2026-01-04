"""Tests for network_delay_time problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def network_delay_time():
    func = get_function("network_delay_time")
    if func is None:
        pytest.skip("Function 'network_delay_time' not registered.")
    return func


class TestNetworkDelayTimeBasic:
    def test_example_1(self, network_delay_time):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        assert network_delay_time(times, 4, 2) == 2

    def test_example_2(self, network_delay_time):
        times = [[1, 2, 1]]
        assert network_delay_time(times, 2, 1) == 1

    def test_unreachable(self, network_delay_time):
        times = [[1, 2, 1]]
        assert network_delay_time(times, 2, 2) == -1


class TestNetworkDelayTimeEdgeCases:
    def test_single_node(self, network_delay_time):
        assert network_delay_time([], 1, 1) == 0

    def test_disconnected_graph(self, network_delay_time):
        times = [[1, 2, 1], [3, 4, 1]]
        assert network_delay_time(times, 4, 1) == -1

    def test_multiple_paths(self, network_delay_time):
        times = [[1, 2, 5], [1, 3, 1], [3, 2, 1]]
        assert network_delay_time(times, 3, 1) == 2


@pytest.mark.performance
class TestNetworkDelayTimePerformance:
    def test_large_input(self, network_delay_time):
        n = 100
        times = []
        for i in range(1, n):
            times.append([i, i + 1, 1])

        start = time.time()
        result = network_delay_time(times, n, 1)
        elapsed = time.time() - start

        assert result == n - 1
        assert elapsed < 1.0
