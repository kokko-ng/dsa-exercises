"""Tests for structurally_unique_bst problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def structurally_unique_bst():
    func = get_function("structurally_unique_bst")
    if func is None:
        pytest.skip("Function 'structurally_unique_bst' not registered.")
    return func


def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    """Check if tree is a valid BST."""
    if node is None:
        return True
    if node.val <= min_val or node.val >= max_val:
        return False
    return (is_valid_bst(node.left, min_val, node.val) and
            is_valid_bst(node.right, node.val, max_val))


def get_values(node, values=None):
    """Get all values in the tree."""
    if values is None:
        values = []
    if node:
        get_values(node.left, values)
        values.append(node.val)
        get_values(node.right, values)
    return values


class TestStructurallyUniqueBstBasic:
    def test_n_equals_3(self, structurally_unique_bst):
        result = structurally_unique_bst(3)
        assert len(result) == 5  # Catalan(3)
        for tree in result:
            assert is_valid_bst(tree)
            assert sorted(get_values(tree)) == [1, 2, 3]

    def test_n_equals_1(self, structurally_unique_bst):
        result = structurally_unique_bst(1)
        assert len(result) == 1
        assert result[0].val == 1
        assert result[0].left is None
        assert result[0].right is None

    def test_n_equals_2(self, structurally_unique_bst):
        result = structurally_unique_bst(2)
        assert len(result) == 2  # Catalan(2)


class TestStructurallyUniqueBstEdgeCases:
    def test_n_equals_4(self, structurally_unique_bst):
        result = structurally_unique_bst(4)
        assert len(result) == 14  # Catalan(4)


@pytest.mark.performance
class TestStructurallyUniqueBstPerformance:
    def test_n_equals_7(self, structurally_unique_bst):
        start = time.time()
        result = structurally_unique_bst(7)
        elapsed = time.time() - start

        assert len(result) == 429  # Catalan(7)
        assert elapsed < 2.0
