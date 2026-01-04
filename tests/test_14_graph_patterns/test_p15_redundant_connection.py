"""Tests for redundant_connection problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def redundant_connection():
    func = get_function("redundant_connection")
    if func is None:
        pytest.skip("Function 'redundant_connection' not registered.")
    return func


class TestRedundantConnectionBasic:
    def test_example_1(self, redundant_connection):
        assert redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]

    def test_example_2(self, redundant_connection):
        assert redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]


class TestRedundantConnectionEdgeCases:
    def test_three_node_cycle(self, redundant_connection):
        result = redundant_connection([[1, 2], [2, 3], [1, 3]])
        assert result == [1, 3]

    def test_longer_cycle(self, redundant_connection):
        edges = [[1, 2], [2, 3], [3, 4], [4, 1]]
        result = redundant_connection(edges)
        assert result == [4, 1]

    def test_complex_graph(self, redundant_connection):
        edges = [[1, 2], [1, 3], [2, 3], [3, 4], [4, 5]]
        result = redundant_connection(edges)
        # The redundant edge is [2, 3] since it completes a cycle
        assert result == [2, 3]


@pytest.mark.performance
class TestRedundantConnectionPerformance:
    def test_large_input(self, redundant_connection):
        n = 1000
        edges = [[i, i + 1] for i in range(1, n)]
        edges.append([1, n - 1])  # Add redundant edge

        start = time.time()
        result = redundant_connection(edges)
        elapsed = time.time() - start

        assert result == [1, n - 1]
        assert elapsed < 1.0
