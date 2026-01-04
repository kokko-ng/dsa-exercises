"""Tests for odd_even_linked_list problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


@pytest.fixture
def odd_even_linked_list():
    """Get the user's odd_even_linked_list implementation."""
    func = get_function("odd_even_linked_list")
    if func is None:
        pytest.skip("Function 'odd_even_linked_list' not registered. Run check(odd_even_linked_list) in notebook.")
    return func


class TestOddEvenLinkedListBasic:
    """Basic functionality tests."""

    def test_five_nodes(self, odd_even_linked_list):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = odd_even_linked_list(head)
        assert result.to_list() == [1, 3, 5, 2, 4]

    def test_seven_nodes(self, odd_even_linked_list):
        head = ListNode.from_list([2, 1, 3, 5, 6, 4, 7])
        result = odd_even_linked_list(head)
        assert result.to_list() == [2, 3, 6, 7, 1, 5, 4]

    def test_four_nodes(self, odd_even_linked_list):
        head = ListNode.from_list([1, 2, 3, 4])
        result = odd_even_linked_list(head)
        assert result.to_list() == [1, 3, 2, 4]


class TestOddEvenLinkedListEdgeCases:
    """Edge case tests."""

    def test_empty_list(self, odd_even_linked_list):
        result = odd_even_linked_list(None)
        assert result is None

    def test_single_node(self, odd_even_linked_list):
        head = ListNode(1)
        result = odd_even_linked_list(head)
        assert result.to_list() == [1]

    def test_two_nodes(self, odd_even_linked_list):
        head = ListNode.from_list([1, 2])
        result = odd_even_linked_list(head)
        assert result.to_list() == [1, 2]

    def test_three_nodes(self, odd_even_linked_list):
        head = ListNode.from_list([1, 2, 3])
        result = odd_even_linked_list(head)
        assert result.to_list() == [1, 3, 2]


@pytest.mark.performance
class TestOddEvenLinkedListPerformance:
    """Performance tests."""

    def test_large_list(self, odd_even_linked_list):
        n = 10000
        head = ListNode.from_list(list(range(n)))

        start = time.time()
        result = odd_even_linked_list(head)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
