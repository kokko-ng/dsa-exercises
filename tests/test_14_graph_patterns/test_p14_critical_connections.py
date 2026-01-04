"""Tests for critical_connections problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def critical_connections():
    func = get_function("critical_connections")
    if func is None:
        pytest.skip("Function 'critical_connections' not registered.")
    return func


class TestCriticalConnectionsBasic:
    def test_example_1(self, critical_connections):
        result = critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
        # Sort for comparison
        result = [sorted(e) for e in result]
        assert sorted(result) == [[1, 3]]

    def test_example_2(self, critical_connections):
        result = critical_connections(2, [[0, 1]])
        result = [sorted(e) for e in result]
        assert sorted(result) == [[0, 1]]


class TestCriticalConnectionsEdgeCases:
    def test_no_bridges(self, critical_connections):
        # Complete graph with 3 nodes - no bridges
        result = critical_connections(3, [[0, 1], [1, 2], [2, 0]])
        assert result == []

    def test_all_bridges(self, critical_connections):
        # Linear graph - all edges are bridges
        result = critical_connections(4, [[0, 1], [1, 2], [2, 3]])
        result = [sorted(e) for e in result]
        expected = [[0, 1], [1, 2], [2, 3]]
        assert sorted(result) == sorted(expected)

    def test_tree_structure(self, critical_connections):
        # Tree - all edges are bridges
        result = critical_connections(5, [[0, 1], [0, 2], [1, 3], [1, 4]])
        result = [sorted(e) for e in result]
        assert len(result) == 4


@pytest.mark.performance
class TestCriticalConnectionsPerformance:
    def test_large_input(self, critical_connections):
        n = 1000
        connections = [[i, i + 1] for i in range(n - 1)]

        start = time.time()
        result = critical_connections(n, connections)
        elapsed = time.time() - start

        assert len(result) == n - 1
        assert elapsed < 2.0
