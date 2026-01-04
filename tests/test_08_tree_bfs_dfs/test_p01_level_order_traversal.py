"""Tests for level_order_traversal problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def level_order_traversal():
    """Get the user's level_order_traversal implementation."""
    func = get_function("level_order_traversal")
    if func is None:
        pytest.skip("Function 'level_order_traversal' not registered. Run check(level_order_traversal) in notebook.")
    return func


def build_tree(values):
    """Build a tree from level-order list representation."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestLevelOrderTraversalBasic:
    """Basic functionality tests."""

    def test_example_1(self, level_order_traversal):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        result = level_order_traversal(root)
        assert result == [[3], [9, 20], [15, 7]]

    def test_single_node(self, level_order_traversal):
        root = build_tree([1])
        result = level_order_traversal(root)
        assert result == [[1]]

    def test_empty_tree(self, level_order_traversal):
        result = level_order_traversal(None)
        assert result == []

    def test_left_skewed(self, level_order_traversal):
        root = build_tree([1, 2, None, 3, None, None, None, 4])
        result = level_order_traversal(root)
        assert result == [[1], [2], [3], [4]]

    def test_right_skewed(self, level_order_traversal):
        root = build_tree([1, None, 2, None, None, None, 3])
        result = level_order_traversal(root)
        assert result == [[1], [2], [3]]


class TestLevelOrderTraversalEdgeCases:
    """Edge case tests."""

    def test_complete_tree(self, level_order_traversal):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        result = level_order_traversal(root)
        assert result == [[1], [2, 3], [4, 5, 6, 7]]

    def test_negative_values(self, level_order_traversal):
        root = build_tree([-10, -20, -30])
        result = level_order_traversal(root)
        assert result == [[-10], [-20, -30]]


@pytest.mark.performance
class TestLevelOrderTraversalPerformance:
    """Performance tests."""

    def test_large_tree(self, level_order_traversal):
        # Build a complete binary tree with 1000+ nodes
        values = list(range(1, 1024))
        root = build_tree(values)

        start = time.time()
        result = level_order_traversal(root)
        elapsed = time.time() - start

        assert len(result) == 10  # 2^10 - 1 = 1023 nodes, 10 levels
        assert elapsed < 1.0
