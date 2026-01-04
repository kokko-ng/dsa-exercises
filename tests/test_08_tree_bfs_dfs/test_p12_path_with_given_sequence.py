"""Tests for path_with_given_sequence problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def path_with_given_sequence():
    func = get_function("path_with_given_sequence")
    if func is None:
        pytest.skip("Function 'path_with_given_sequence' not registered.")
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


class TestPathWithGivenSequenceBasic:
    def test_example_1(self, path_with_given_sequence):
        root = build_tree([1, 7, 9, None, None, 2, 9])
        assert path_with_given_sequence(root, [1, 9, 9]) == True

    def test_example_2(self, path_with_given_sequence):
        root = build_tree([1, 7, 9, None, None, 2, 9])
        assert path_with_given_sequence(root, [1, 9, 2]) == True

    def test_example_3(self, path_with_given_sequence):
        root = build_tree([1, 7, 9, None, None, 2, 9])
        assert path_with_given_sequence(root, [1, 7, 9]) == False  # 7 is a leaf

    def test_single_node(self, path_with_given_sequence):
        root = build_tree([5])
        assert path_with_given_sequence(root, [5]) == True
        assert path_with_given_sequence(root, [1]) == False


class TestPathWithGivenSequenceEdgeCases:
    def test_sequence_longer_than_tree(self, path_with_given_sequence):
        root = build_tree([1, 2])
        assert path_with_given_sequence(root, [1, 2, 3]) == False

    def test_sequence_shorter_than_path(self, path_with_given_sequence):
        root = build_tree([1, 2, 3])
        assert path_with_given_sequence(root, [1]) == False

    def test_wrong_root(self, path_with_given_sequence):
        root = build_tree([1, 2, 3])
        assert path_with_given_sequence(root, [5, 2]) == False


@pytest.mark.performance
class TestPathWithGivenSequencePerformance:
    def test_large_tree(self, path_with_given_sequence):
        values = list(range(1, 1024))
        root = build_tree(values)
        sequence = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

        start = time.time()
        result = path_with_given_sequence(root, sequence)
        elapsed = time.time() - start

        assert result == True
        assert elapsed < 1.0
