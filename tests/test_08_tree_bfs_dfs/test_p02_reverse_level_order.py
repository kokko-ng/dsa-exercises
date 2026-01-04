"""Tests for reverse_level_order problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def reverse_level_order():
    func = get_function("reverse_level_order")
    if func is None:
        pytest.skip("Function 'reverse_level_order' not registered.")
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


class TestReverseLevelOrderBasic:
    def test_example_1(self, reverse_level_order):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        result = reverse_level_order(root)
        assert result == [[15, 7], [9, 20], [3]]

    def test_single_node(self, reverse_level_order):
        root = build_tree([1])
        result = reverse_level_order(root)
        assert result == [[1]]

    def test_empty_tree(self, reverse_level_order):
        result = reverse_level_order(None)
        assert result == []

    def test_complete_tree(self, reverse_level_order):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        result = reverse_level_order(root)
        assert result == [[4, 5, 6, 7], [2, 3], [1]]


class TestReverseLevelOrderEdgeCases:
    def test_two_levels(self, reverse_level_order):
        root = build_tree([1, 2, 3])
        result = reverse_level_order(root)
        assert result == [[2, 3], [1]]


@pytest.mark.performance
class TestReverseLevelOrderPerformance:
    def test_large_tree(self, reverse_level_order):
        values = list(range(1, 1024))
        root = build_tree(values)

        start = time.time()
        result = reverse_level_order(root)
        elapsed = time.time() - start

        assert len(result) == 10
        assert result[0] == list(range(512, 1024))
        assert elapsed < 1.0
