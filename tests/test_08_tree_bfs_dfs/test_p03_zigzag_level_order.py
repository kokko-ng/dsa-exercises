"""Tests for zigzag_level_order problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def zigzag_level_order():
    func = get_function("zigzag_level_order")
    if func is None:
        pytest.skip("Function 'zigzag_level_order' not registered.")
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


class TestZigzagLevelOrderBasic:
    def test_example_1(self, zigzag_level_order):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        result = zigzag_level_order(root)
        assert result == [[3], [20, 9], [15, 7]]

    def test_single_node(self, zigzag_level_order):
        root = build_tree([1])
        result = zigzag_level_order(root)
        assert result == [[1]]

    def test_empty_tree(self, zigzag_level_order):
        result = zigzag_level_order(None)
        assert result == []

    def test_complete_tree(self, zigzag_level_order):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        result = zigzag_level_order(root)
        assert result == [[1], [3, 2], [4, 5, 6, 7]]


class TestZigzagLevelOrderEdgeCases:
    def test_four_levels(self, zigzag_level_order):
        root = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        result = zigzag_level_order(root)
        assert result == [[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8]]


@pytest.mark.performance
class TestZigzagLevelOrderPerformance:
    def test_large_tree(self, zigzag_level_order):
        values = list(range(1, 1024))
        root = build_tree(values)

        start = time.time()
        result = zigzag_level_order(root)
        elapsed = time.time() - start

        assert len(result) == 10
        assert elapsed < 1.0
