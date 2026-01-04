"""Tests for level_order_successor problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def level_order_successor():
    func = get_function("level_order_successor")
    if func is None:
        pytest.skip("Function 'level_order_successor' not registered.")
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


class TestLevelOrderSuccessorBasic:
    def test_example_1(self, level_order_successor):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        result = level_order_successor(root, 9)
        assert result is not None
        assert result.val == 20

    def test_example_2(self, level_order_successor):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        result = level_order_successor(root, 20)
        assert result is not None
        assert result.val == 15

    def test_last_node(self, level_order_successor):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        result = level_order_successor(root, 7)
        assert result is None


class TestLevelOrderSuccessorEdgeCases:
    def test_root_successor(self, level_order_successor):
        root = build_tree([1, 2, 3])
        result = level_order_successor(root, 1)
        assert result is not None
        assert result.val == 2

    def test_single_node(self, level_order_successor):
        root = build_tree([1])
        result = level_order_successor(root, 1)
        assert result is None


@pytest.mark.performance
class TestLevelOrderSuccessorPerformance:
    def test_large_tree(self, level_order_successor):
        values = list(range(1, 1024))
        root = build_tree(values)

        start = time.time()
        result = level_order_successor(root, 512)
        elapsed = time.time() - start

        assert result is not None
        assert elapsed < 1.0
