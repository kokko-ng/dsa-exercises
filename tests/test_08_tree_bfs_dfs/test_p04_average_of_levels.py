"""Tests for average_of_levels problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def average_of_levels():
    func = get_function("average_of_levels")
    if func is None:
        pytest.skip("Function 'average_of_levels' not registered.")
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


class TestAverageOfLevelsBasic:
    def test_example_1(self, average_of_levels):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        result = average_of_levels(root)
        assert len(result) == 3
        assert abs(result[0] - 3.0) < 0.001
        assert abs(result[1] - 14.5) < 0.001
        assert abs(result[2] - 11.0) < 0.001

    def test_single_node(self, average_of_levels):
        root = build_tree([5])
        result = average_of_levels(root)
        assert result == [5.0]

    def test_complete_tree(self, average_of_levels):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        result = average_of_levels(root)
        assert abs(result[0] - 1.0) < 0.001
        assert abs(result[1] - 2.5) < 0.001
        assert abs(result[2] - 5.5) < 0.001


class TestAverageOfLevelsEdgeCases:
    def test_negative_values(self, average_of_levels):
        root = build_tree([-10, -5, -15])
        result = average_of_levels(root)
        assert abs(result[0] - (-10.0)) < 0.001
        assert abs(result[1] - (-10.0)) < 0.001

    def test_large_values(self, average_of_levels):
        root = build_tree([2147483647, 2147483647, 2147483647])
        result = average_of_levels(root)
        assert abs(result[0] - 2147483647.0) < 1
        assert abs(result[1] - 2147483647.0) < 1


@pytest.mark.performance
class TestAverageOfLevelsPerformance:
    def test_large_tree(self, average_of_levels):
        values = list(range(1, 1024))
        root = build_tree(values)

        start = time.time()
        result = average_of_levels(root)
        elapsed = time.time() - start

        assert len(result) == 10
        assert elapsed < 1.0
