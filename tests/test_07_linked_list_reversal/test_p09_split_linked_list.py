"""Tests for split_linked_list problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


@pytest.fixture
def split_linked_list():
    """Get the user's split_linked_list implementation."""
    func = get_function("split_linked_list")
    if func is None:
        pytest.skip("Function 'split_linked_list' not registered. Run check(split_linked_list) in notebook.")
    return func


def to_lists(parts):
    """Convert list of ListNodes to list of lists."""
    result = []
    for part in parts:
        if part is None:
            result.append([])
        else:
            result.append(part.to_list())
    return result


class TestSplitLinkedListBasic:
    """Basic functionality tests."""

    def test_more_parts_than_nodes(self, split_linked_list):
        head = ListNode.from_list([1, 2, 3])
        result = split_linked_list(head, 5)
        assert to_lists(result) == [[1], [2], [3], [], []]

    def test_even_split(self, split_linked_list):
        head = ListNode.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = split_linked_list(head, 3)
        assert to_lists(result) == [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

    def test_uneven_split(self, split_linked_list):
        head = ListNode.from_list([1, 2, 3, 4, 5, 6, 7])
        result = split_linked_list(head, 3)
        assert to_lists(result) == [[1, 2, 3], [4, 5], [6, 7]]


class TestSplitLinkedListEdgeCases:
    """Edge case tests."""

    def test_empty_list(self, split_linked_list):
        result = split_linked_list(None, 3)
        assert len(result) == 3
        assert all(part is None for part in result)

    def test_single_part(self, split_linked_list):
        head = ListNode.from_list([1, 2, 3])
        result = split_linked_list(head, 1)
        assert to_lists(result) == [[1, 2, 3]]

    def test_single_node(self, split_linked_list):
        head = ListNode(1)
        result = split_linked_list(head, 3)
        assert to_lists(result) == [[1], [], []]


@pytest.mark.performance
class TestSplitLinkedListPerformance:
    """Performance tests."""

    def test_large_list(self, split_linked_list):
        n = 1000
        k = 50
        head = ListNode.from_list(list(range(n)))

        start = time.time()
        result = split_linked_list(head, k)
        elapsed = time.time() - start

        assert len(result) == k
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
