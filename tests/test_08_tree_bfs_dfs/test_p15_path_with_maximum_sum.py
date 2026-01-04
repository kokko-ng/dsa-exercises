"""Tests for path_with_maximum_sum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def path_with_maximum_sum():
    func = get_function("path_with_maximum_sum")
    if func is None:
        pytest.skip("Function 'path_with_maximum_sum' not registered.")
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


class TestPathWithMaximumSumBasic:
    def test_example_1(self, path_with_maximum_sum):
        root = build_tree([1, 2, 3])
        assert path_with_maximum_sum(root) == 6  # 2 -> 1 -> 3

    def test_example_2(self, path_with_maximum_sum):
        root = build_tree([-10, 9, 20, None, None, 15, 7])
        assert path_with_maximum_sum(root) == 42  # 15 -> 20 -> 7

    def test_single_node(self, path_with_maximum_sum):
        root = build_tree([5])
        assert path_with_maximum_sum(root) == 5

    def test_single_negative(self, path_with_maximum_sum):
        root = build_tree([-3])
        assert path_with_maximum_sum(root) == -3


class TestPathWithMaximumSumEdgeCases:
    def test_all_negative(self, path_with_maximum_sum):
        root = build_tree([-1, -2, -3])
        assert path_with_maximum_sum(root) == -1

    def test_mixed_values(self, path_with_maximum_sum):
        root = build_tree([2, -1, -2])
        assert path_with_maximum_sum(root) == 2

    def test_skip_negative_subtree(self, path_with_maximum_sum):
        root = build_tree([5, 4, 8, 11, None, -100, 4, 7, 2, None, None, None, 1])
        result = path_with_maximum_sum(root)
        assert result >= 27  # At least 5 + 4 + 11 + 7


@pytest.mark.performance
class TestPathWithMaximumSumPerformance:
    def test_large_tree(self, path_with_maximum_sum):
        values = list(range(1, 1001))
        root = build_tree(values)

        start = time.time()
        result = path_with_maximum_sum(root)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0
