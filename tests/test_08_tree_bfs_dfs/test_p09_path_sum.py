"""Tests for path_sum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def path_sum():
    func = get_function("path_sum")
    if func is None:
        pytest.skip("Function 'path_sum' not registered.")
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


class TestPathSumBasic:
    def test_example_1(self, path_sum):
        root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        assert path_sum(root, 22) == True

    def test_no_path(self, path_sum):
        root = build_tree([1, 2, 3])
        assert path_sum(root, 5) == False

    def test_single_node_match(self, path_sum):
        root = build_tree([5])
        assert path_sum(root, 5) == True

    def test_single_node_no_match(self, path_sum):
        root = build_tree([5])
        assert path_sum(root, 1) == False

    def test_empty_tree(self, path_sum):
        assert path_sum(None, 0) == False


class TestPathSumEdgeCases:
    def test_negative_values(self, path_sum):
        root = build_tree([1, -2, -3, 1, 3, -2, None, -1])
        assert path_sum(root, -1) == True

    def test_zero_target(self, path_sum):
        root = build_tree([1, -1])
        assert path_sum(root, 0) == True

    def test_must_be_leaf(self, path_sum):
        # Path sum must end at a leaf, not just any node
        root = build_tree([1, 2])
        assert path_sum(root, 1) == False  # 1 is not a leaf


@pytest.mark.performance
class TestPathSumPerformance:
    def test_large_tree(self, path_sum):
        values = list(range(1, 1001))
        root = build_tree(values)

        start = time.time()
        result = path_sum(root, sum(range(1, 11)))  # Path to first leaf
        elapsed = time.time() - start

        assert elapsed < 1.0
