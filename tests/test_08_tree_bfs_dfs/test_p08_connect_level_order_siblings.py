"""Tests for connect_level_order_siblings problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import TreeNode


@pytest.fixture
def connect_level_order_siblings():
    func = get_function("connect_level_order_siblings")
    if func is None:
        pytest.skip("Function 'connect_level_order_siblings' not registered.")
    return func


def build_tree_with_next(values):
    """Build a tree where nodes have a 'next' attribute."""
    if not values:
        return None
    root = TreeNode(values[0])
    root.next = None
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            node.left.next = None
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            node.right.next = None
            queue.append(node.right)
        i += 1
    return root


def get_level_connections(root):
    """Get the next connections for each level."""
    if not root:
        return []

    result = []
    level_start = root

    while level_start:
        level = []
        current = level_start
        next_level_start = None

        while current:
            level.append(current.val)
            if not next_level_start:
                next_level_start = current.left or current.right
            current = current.next

        result.append(level)

        # Find start of next level
        current = level_start
        next_level_start = None
        while current and not next_level_start:
            next_level_start = current.left or current.right
            current = current.next
        level_start = next_level_start

    return result


class TestConnectLevelOrderSiblingsBasic:
    def test_example_1(self, connect_level_order_siblings):
        root = build_tree_with_next([1, 2, 3, 4, 5, 6, 7])
        result = connect_level_order_siblings(root)

        # Check root level
        assert result.next is None

        # Check level 2
        assert result.left.next == result.right
        assert result.right.next is None

        # Check level 3
        assert result.left.left.next == result.left.right
        assert result.left.right.next == result.right.left
        assert result.right.left.next == result.right.right
        assert result.right.right.next is None

    def test_single_node(self, connect_level_order_siblings):
        root = build_tree_with_next([1])
        result = connect_level_order_siblings(root)
        assert result.next is None

    def test_empty_tree(self, connect_level_order_siblings):
        result = connect_level_order_siblings(None)
        assert result is None


class TestConnectLevelOrderSiblingsEdgeCases:
    def test_two_levels(self, connect_level_order_siblings):
        root = build_tree_with_next([1, 2, 3])
        result = connect_level_order_siblings(root)
        assert result.left.next == result.right
        assert result.right.next is None


@pytest.mark.performance
class TestConnectLevelOrderSiblingsPerformance:
    def test_large_tree(self, connect_level_order_siblings):
        values = list(range(1, 1024))
        root = build_tree_with_next(values)

        start = time.time()
        result = connect_level_order_siblings(root)
        elapsed = time.time() - start

        assert result is not None
        assert elapsed < 1.0
