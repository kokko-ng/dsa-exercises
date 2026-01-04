"""Tests for all_paths_for_sum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def all_paths_for_sum():
    func = get_function("all_paths_for_sum")
    if func is None:
        pytest.skip("Function 'all_paths_for_sum' not registered.")
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


class TestAllPathsForSumBasic:
    def test_example_1(self, all_paths_for_sum):
        root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        result = all_paths_for_sum(root, 22)
        expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
        assert sorted(result) == sorted(expected)

    def test_no_paths(self, all_paths_for_sum):
        root = build_tree([1, 2, 3])
        result = all_paths_for_sum(root, 5)
        assert result == []

    def test_single_node(self, all_paths_for_sum):
        root = build_tree([5])
        result = all_paths_for_sum(root, 5)
        assert result == [[5]]

    def test_empty_tree(self, all_paths_for_sum):
        result = all_paths_for_sum(None, 0)
        assert result == []


class TestAllPathsForSumEdgeCases:
    def test_multiple_paths(self, all_paths_for_sum):
        root = build_tree([1, 2, 2, 1, 1, 1, 1])
        result = all_paths_for_sum(root, 4)
        assert len(result) == 4

    def test_negative_values(self, all_paths_for_sum):
        root = build_tree([0, 1, -1])
        result = all_paths_for_sum(root, 0)
        assert len(result) == 2


@pytest.mark.performance
class TestAllPathsForSumPerformance:
    def test_large_tree(self, all_paths_for_sum):
        values = list(range(1, 1001))
        root = build_tree(values)

        start = time.time()
        result = all_paths_for_sum(root, 10000)
        elapsed = time.time() - start

        assert elapsed < 1.0
