"""Tests for maximum_depth problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def maximum_depth():
    func = get_function("maximum_depth")
    if func is None:
        pytest.skip("Function 'maximum_depth' not registered.")
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


class TestMaximumDepthBasic:
    def test_example_1(self, maximum_depth):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        assert maximum_depth(root) == 3

    def test_single_node(self, maximum_depth):
        root = build_tree([1])
        assert maximum_depth(root) == 1

    def test_empty_tree(self, maximum_depth):
        assert maximum_depth(None) == 0

    def test_two_nodes(self, maximum_depth):
        root = build_tree([1, None, 2])
        assert maximum_depth(root) == 2


class TestMaximumDepthEdgeCases:
    def test_complete_tree(self, maximum_depth):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        assert maximum_depth(root) == 3

    def test_left_skewed(self, maximum_depth):
        root = build_tree([1, 2, None, 3, None, None, None, 4])
        assert maximum_depth(root) == 4


@pytest.mark.performance
class TestMaximumDepthPerformance:
    def test_large_tree(self, maximum_depth):
        values = list(range(1, 10001))
        root = build_tree(values)

        start = time.time()
        result = maximum_depth(root)
        elapsed = time.time() - start

        assert result >= 10
        assert elapsed < 1.0
