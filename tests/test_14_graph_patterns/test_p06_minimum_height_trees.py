"""Tests for minimum_height_trees problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def minimum_height_trees():
    func = get_function("minimum_height_trees")
    if func is None:
        pytest.skip("Function 'minimum_height_trees' not registered.")
    return func


class TestMinimumHeightTreesBasic:
    def test_star_graph(self, minimum_height_trees):
        result = minimum_height_trees(4, [[1, 0], [1, 2], [1, 3]])
        assert sorted(result) == [1]

    def test_path_graph_even(self, minimum_height_trees):
        result = minimum_height_trees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])
        assert sorted(result) == [3, 4]

    def test_single_node(self, minimum_height_trees):
        result = minimum_height_trees(1, [])
        assert result == [0]


class TestMinimumHeightTreesEdgeCases:
    def test_two_nodes(self, minimum_height_trees):
        result = minimum_height_trees(2, [[0, 1]])
        assert sorted(result) == [0, 1]

    def test_three_node_line(self, minimum_height_trees):
        result = minimum_height_trees(3, [[0, 1], [1, 2]])
        assert result == [1]

    def test_four_node_line(self, minimum_height_trees):
        result = minimum_height_trees(4, [[0, 1], [1, 2], [2, 3]])
        assert sorted(result) == [1, 2]


@pytest.mark.performance
class TestMinimumHeightTreesPerformance:
    def test_large_tree(self, minimum_height_trees):
        n = 10000
        edges = [[i, i + 1] for i in range(n - 1)]

        start = time.time()
        result = minimum_height_trees(n, edges)
        elapsed = time.time() - start

        assert len(result) in [1, 2]
        assert elapsed < 2.0
