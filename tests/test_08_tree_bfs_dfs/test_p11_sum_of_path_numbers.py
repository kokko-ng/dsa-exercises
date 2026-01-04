"""Tests for sum_of_path_numbers problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def sum_of_path_numbers():
    func = get_function("sum_of_path_numbers")
    if func is None:
        pytest.skip("Function 'sum_of_path_numbers' not registered.")
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


class TestSumOfPathNumbersBasic:
    def test_example_1(self, sum_of_path_numbers):
        root = build_tree([1, 2, 3])
        assert sum_of_path_numbers(root) == 25  # 12 + 13

    def test_example_2(self, sum_of_path_numbers):
        root = build_tree([4, 9, 0, 5, 1])
        assert sum_of_path_numbers(root) == 1026  # 495 + 491 + 40

    def test_single_node(self, sum_of_path_numbers):
        root = build_tree([5])
        assert sum_of_path_numbers(root) == 5


class TestSumOfPathNumbersEdgeCases:
    def test_all_zeros(self, sum_of_path_numbers):
        root = build_tree([0, 0, 0])
        assert sum_of_path_numbers(root) == 0

    def test_deep_tree(self, sum_of_path_numbers):
        root = build_tree([1, 2, None, 3])
        assert sum_of_path_numbers(root) == 123

    def test_right_skewed(self, sum_of_path_numbers):
        root = build_tree([1, None, 2, None, None, None, 3])
        assert sum_of_path_numbers(root) == 123


@pytest.mark.performance
class TestSumOfPathNumbersPerformance:
    def test_large_tree(self, sum_of_path_numbers):
        # Build a balanced tree with single digits
        values = [i % 10 for i in range(1, 1024)]
        root = build_tree(values)

        start = time.time()
        result = sum_of_path_numbers(root)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0
