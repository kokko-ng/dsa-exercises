"""Tests for count_paths_for_sum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def count_paths_for_sum():
    func = get_function("count_paths_for_sum")
    if func is None:
        pytest.skip("Function 'count_paths_for_sum' not registered.")
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


class TestCountPathsForSumBasic:
    def test_example_1(self, count_paths_for_sum):
        root = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        assert count_paths_for_sum(root, 8) == 3

    def test_single_node_match(self, count_paths_for_sum):
        root = build_tree([5])
        assert count_paths_for_sum(root, 5) == 1

    def test_single_node_no_match(self, count_paths_for_sum):
        root = build_tree([5])
        assert count_paths_for_sum(root, 10) == 0

    def test_empty_tree(self, count_paths_for_sum):
        assert count_paths_for_sum(None, 0) == 0


class TestCountPathsForSumEdgeCases:
    def test_negative_target(self, count_paths_for_sum):
        root = build_tree([1, -2, -3])
        assert count_paths_for_sum(root, -2) == 1

    def test_multiple_paths_same_sum(self, count_paths_for_sum):
        root = build_tree([1, 2, 2, 3, 3, 3, 3])
        assert count_paths_for_sum(root, 3) == 6  # Multiple paths sum to 3

    def test_path_not_from_root(self, count_paths_for_sum):
        root = build_tree([1, 2, 3, 4, 5])
        assert count_paths_for_sum(root, 7) == 1  # Path: 2 -> 5 or 3 -> 4


@pytest.mark.performance
class TestCountPathsForSumPerformance:
    def test_large_tree(self, count_paths_for_sum):
        values = list(range(1, 1001))
        root = build_tree(values)

        start = time.time()
        result = count_paths_for_sum(root, 100)
        elapsed = time.time() - start

        assert result >= 0
        assert elapsed < 2.0
