"""Tests for reverse_between problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


@pytest.fixture
def reverse_between():
    """Get the user's reverse_between implementation."""
    func = get_function("reverse_between")
    if func is None:
        pytest.skip("Function 'reverse_between' not registered. Run check(reverse_between) in notebook.")
    return func


class TestReverseBetweenBasic:
    """Basic functionality tests."""

    def test_middle_section(self, reverse_between):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_between(head, 2, 4)
        assert result.to_list() == [1, 4, 3, 2, 5]

    def test_full_list(self, reverse_between):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_between(head, 1, 5)
        assert result.to_list() == [5, 4, 3, 2, 1]

    def test_from_start(self, reverse_between):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_between(head, 1, 3)
        assert result.to_list() == [3, 2, 1, 4, 5]

    def test_to_end(self, reverse_between):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_between(head, 3, 5)
        assert result.to_list() == [1, 2, 5, 4, 3]


class TestReverseBetweenEdgeCases:
    """Edge case tests."""

    def test_single_node(self, reverse_between):
        head = ListNode(5)
        result = reverse_between(head, 1, 1)
        assert result.to_list() == [5]

    def test_same_m_n(self, reverse_between):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_between(head, 3, 3)
        assert result.to_list() == [1, 2, 3, 4, 5]

    def test_adjacent_nodes(self, reverse_between):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_between(head, 2, 3)
        assert result.to_list() == [1, 3, 2, 4, 5]


@pytest.mark.performance
class TestReverseBetweenPerformance:
    """Performance tests."""

    def test_large_list(self, reverse_between):
        n = 500
        head = ListNode.from_list(list(range(n)))

        start = time.time()
        result = reverse_between(head, 100, 400)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
