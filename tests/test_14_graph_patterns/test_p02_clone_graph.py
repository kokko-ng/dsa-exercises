"""Tests for clone_graph problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(adj_list):
    """Build graph from adjacency list."""
    if not adj_list:
        return None
    nodes = {i: Node(i) for i in range(1, len(adj_list) + 1)}
    for i, neighbors in enumerate(adj_list, 1):
        nodes[i].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def graph_to_adj_list(node):
    """Convert graph back to adjacency list."""
    if not node:
        return []
    visited = {}

    def dfs(n):
        if n.val in visited:
            return
        visited[n.val] = [neighbor.val for neighbor in n.neighbors]
        for neighbor in n.neighbors:
            dfs(neighbor)

    dfs(node)
    return [visited[i] for i in range(1, len(visited) + 1)]


@pytest.fixture
def clone_graph():
    func = get_function("clone_graph")
    if func is None:
        pytest.skip("Function 'clone_graph' not registered.")
    return func


class TestCloneGraphBasic:
    def test_four_nodes(self, clone_graph):
        adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
        original = build_graph(adj_list)
        cloned = clone_graph(original)

        assert cloned is not original
        assert graph_to_adj_list(cloned) == adj_list

    def test_single_node(self, clone_graph):
        adj_list = [[]]
        original = build_graph(adj_list)
        cloned = clone_graph(original)

        assert cloned is not original
        assert cloned.val == 1
        assert cloned.neighbors == []

    def test_two_nodes(self, clone_graph):
        adj_list = [[2], [1]]
        original = build_graph(adj_list)
        cloned = clone_graph(original)

        assert cloned is not original
        assert graph_to_adj_list(cloned) == adj_list


class TestCloneGraphEdgeCases:
    def test_empty_graph(self, clone_graph):
        assert clone_graph(None) is None

    def test_deep_copy_verification(self, clone_graph):
        """Verify that it's a deep copy, not shallow."""
        adj_list = [[2], [1]]
        original = build_graph(adj_list)
        cloned = clone_graph(original)

        # Modify original
        original.val = 999
        assert cloned.val == 1  # Clone should be unchanged
