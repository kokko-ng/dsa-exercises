"""Tests for reverse_linked_list_ii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


@pytest.fixture
def reverse_linked_list_ii():
    """Get the user's reverse_linked_list_ii implementation."""
    func = get_function("reverse_linked_list_ii")
    if func is None:
        pytest.skip("Function 'reverse_linked_list_ii' not registered. Run check(reverse_linked_list_ii) in notebook.")
    return func


class TestReverseLinkedListIIBasic:
    """Basic functionality tests."""

    def test_middle_section(self, reverse_linked_list_ii):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_linked_list_ii(head, 2, 4)
        assert result.to_list() == [1, 4, 3, 2, 5]

    def test_full_list(self, reverse_linked_list_ii):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_linked_list_ii(head, 1, 5)
        assert result.to_list() == [5, 4, 3, 2, 1]

    def test_from_start(self, reverse_linked_list_ii):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_linked_list_ii(head, 1, 3)
        assert result.to_list() == [3, 2, 1, 4, 5]

    def test_to_end(self, reverse_linked_list_ii):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_linked_list_ii(head, 3, 5)
        assert result.to_list() == [1, 2, 5, 4, 3]


class TestReverseLinkedListIIEdgeCases:
    """Edge case tests."""

    def test_single_node(self, reverse_linked_list_ii):
        head = ListNode(5)
        result = reverse_linked_list_ii(head, 1, 1)
        assert result.to_list() == [5]

    def test_same_left_right(self, reverse_linked_list_ii):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_linked_list_ii(head, 3, 3)
        assert result.to_list() == [1, 2, 3, 4, 5]

    def test_two_nodes(self, reverse_linked_list_ii):
        head = ListNode.from_list([1, 2])
        result = reverse_linked_list_ii(head, 1, 2)
        assert result.to_list() == [2, 1]


@pytest.mark.performance
class TestReverseLinkedListIIPerformance:
    """Performance tests."""

    def test_large_list(self, reverse_linked_list_ii):
        n = 500
        head = ListNode.from_list(list(range(n)))

        start = time.time()
        result = reverse_linked_list_ii(head, 100, 400)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
