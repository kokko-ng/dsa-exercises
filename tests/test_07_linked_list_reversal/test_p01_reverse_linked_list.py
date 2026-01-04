"""Tests for reverse_linked_list problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


@pytest.fixture
def reverse_linked_list():
    """Get the user's reverse_linked_list implementation."""
    func = get_function("reverse_linked_list")
    if func is None:
        pytest.skip("Function 'reverse_linked_list' not registered. Run check(reverse_linked_list) in notebook.")
    return func


class TestReverseLinkedListBasic:
    """Basic functionality tests."""

    def test_five_nodes(self, reverse_linked_list):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_linked_list(head)
        assert result.to_list() == [5, 4, 3, 2, 1]

    def test_two_nodes(self, reverse_linked_list):
        head = ListNode.from_list([1, 2])
        result = reverse_linked_list(head)
        assert result.to_list() == [2, 1]

    def test_three_nodes(self, reverse_linked_list):
        head = ListNode.from_list([1, 2, 3])
        result = reverse_linked_list(head)
        assert result.to_list() == [3, 2, 1]


class TestReverseLinkedListEdgeCases:
    """Edge case tests."""

    def test_empty_list(self, reverse_linked_list):
        result = reverse_linked_list(None)
        assert result is None

    def test_single_node(self, reverse_linked_list):
        head = ListNode(1)
        result = reverse_linked_list(head)
        assert result.to_list() == [1]

    def test_negative_values(self, reverse_linked_list):
        head = ListNode.from_list([-1, -2, -3])
        result = reverse_linked_list(head)
        assert result.to_list() == [-3, -2, -1]


@pytest.mark.performance
class TestReverseLinkedListPerformance:
    """Performance tests."""

    def test_large_list(self, reverse_linked_list):
        n = 5000
        head = ListNode.from_list(list(range(n)))

        start = time.time()
        result = reverse_linked_list(head)
        elapsed = time.time() - start

        assert result.to_list() == list(range(n - 1, -1, -1))
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
