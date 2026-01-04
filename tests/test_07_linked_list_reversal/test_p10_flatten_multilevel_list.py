"""Tests for flatten_multilevel_list problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


# Node class for multilevel list
class Node:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

    def to_list(self):
        """Convert to Python list."""
        result = []
        curr = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


def create_list(values):
    """Create a simple linked list from values."""
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head


@pytest.fixture
def flatten_multilevel_list():
    """Get the user's flatten_multilevel_list implementation."""
    func = get_function("flatten_multilevel_list")
    if func is None:
        pytest.skip("Function 'flatten_multilevel_list' not registered. Run check(flatten_multilevel_list) in notebook.")
    return func


class TestFlattenMultilevelListBasic:
    """Basic functionality tests."""

    def test_single_level(self, flatten_multilevel_list):
        head = create_list([1, 2, 3, 4, 5])
        result = flatten_multilevel_list(head)
        assert result.to_list() == [1, 2, 3, 4, 5]

    def test_one_child(self, flatten_multilevel_list):
        # 1 -> 2 -> 3
        #      |
        #      4 -> 5
        head = create_list([1, 2, 3])
        head.next.child = create_list([4, 5])
        result = flatten_multilevel_list(head)
        assert result.to_list() == [1, 2, 4, 5, 3]

    def test_child_at_start(self, flatten_multilevel_list):
        # 1 -> 2
        # |
        # 3
        head = create_list([1, 2])
        head.child = create_list([3])
        result = flatten_multilevel_list(head)
        assert result.to_list() == [1, 3, 2]


class TestFlattenMultilevelListEdgeCases:
    """Edge case tests."""

    def test_empty_list(self, flatten_multilevel_list):
        result = flatten_multilevel_list(None)
        assert result is None

    def test_single_node(self, flatten_multilevel_list):
        head = Node(1)
        result = flatten_multilevel_list(head)
        assert result.to_list() == [1]

    def test_nested_children(self, flatten_multilevel_list):
        # 1 -> 2
        #      |
        #      3 -> 4
        #      |
        #      5
        head = create_list([1, 2])
        child1 = create_list([3, 4])
        child2 = create_list([5])
        head.next.child = child1
        child1.child = child2
        result = flatten_multilevel_list(head)
        assert result.to_list() == [1, 2, 3, 5, 4]


@pytest.mark.performance
class TestFlattenMultilevelListPerformance:
    """Performance tests."""

    def test_large_list(self, flatten_multilevel_list):
        # Create a list with many children
        head = create_list(list(range(100)))
        curr = head
        for i in range(100, 200):
            if curr.next:
                curr.next.child = Node(i)
                curr = curr.next.next
            else:
                break

        start = time.time()
        result = flatten_multilevel_list(head)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
