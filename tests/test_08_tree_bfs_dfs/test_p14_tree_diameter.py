"""Tests for tree_diameter problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def tree_diameter():
    func = get_function("tree_diameter")
    if func is None:
        pytest.skip("Function 'tree_diameter' not registered.")
    return func


def build_tree(values):
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


class TestTreeDiameterBasic:
    def test_example_1(self, tree_diameter):
        root = build_tree([1, 2, 3, 4, 5])
        assert tree_diameter(root) == 3

    def test_single_node(self, tree_diameter):
        root = build_tree([1])
        assert tree_diameter(root) == 0

    def test_two_nodes(self, tree_diameter):
        root = build_tree([1, 2])
        assert tree_diameter(root) == 1

    def test_linear_tree(self, tree_diameter):
        root = build_tree([1, 2, None, 3, None, None, None, 4])
        assert tree_diameter(root) == 3


class TestTreeDiameterEdgeCases:
    def test_diameter_not_through_root(self, tree_diameter):
        # Diameter might not pass through root
        root = build_tree([1, 2, 3, 4, 5, None, None, 6, None, None, 7])
        result = tree_diameter(root)
        assert result >= 4

    def test_balanced_tree(self, tree_diameter):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        assert tree_diameter(root) == 4


@pytest.mark.performance
class TestTreeDiameterPerformance:
    def test_large_tree(self, tree_diameter):
        values = list(range(1, 10001))
        root = build_tree(values)

        start = time.time()
        result = tree_diameter(root)
        elapsed = time.time() - start

        assert result >= 10
        assert elapsed < 1.0
