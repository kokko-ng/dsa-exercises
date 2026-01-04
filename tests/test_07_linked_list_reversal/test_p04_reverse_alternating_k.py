"""Tests for reverse_alternating_k problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


@pytest.fixture
def reverse_alternating_k():
    """Get the user's reverse_alternating_k implementation."""
    func = get_function("reverse_alternating_k")
    if func is None:
        pytest.skip("Function 'reverse_alternating_k' not registered. Run check(reverse_alternating_k) in notebook.")
    return func


class TestReverseAlternatingKBasic:
    """Basic functionality tests."""

    def test_k_equals_2(self, reverse_alternating_k):
        head = ListNode.from_list([1, 2, 3, 4, 5, 6, 7, 8])
        result = reverse_alternating_k(head, 2)
        assert result.to_list() == [2, 1, 3, 4, 6, 5, 7, 8]

    def test_k_equals_3(self, reverse_alternating_k):
        head = ListNode.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = reverse_alternating_k(head, 3)
        assert result.to_list() == [3, 2, 1, 4, 5, 6, 9, 8, 7]

    def test_not_divisible(self, reverse_alternating_k):
        head = ListNode.from_list([1, 2, 3, 4, 5, 6, 7])
        result = reverse_alternating_k(head, 2)
        assert result.to_list() == [2, 1, 3, 4, 6, 5, 7]


class TestReverseAlternatingKEdgeCases:
    """Edge case tests."""

    def test_k_equals_1(self, reverse_alternating_k):
        head = ListNode.from_list([1, 2, 3, 4])
        result = reverse_alternating_k(head, 1)
        assert result.to_list() == [1, 2, 3, 4]

    def test_single_group(self, reverse_alternating_k):
        head = ListNode.from_list([1, 2, 3])
        result = reverse_alternating_k(head, 3)
        assert result.to_list() == [3, 2, 1]

    def test_two_groups(self, reverse_alternating_k):
        head = ListNode.from_list([1, 2, 3, 4])
        result = reverse_alternating_k(head, 2)
        assert result.to_list() == [2, 1, 3, 4]


@pytest.mark.performance
class TestReverseAlternatingKPerformance:
    """Performance tests."""

    def test_large_list(self, reverse_alternating_k):
        n = 5000
        k = 10
        head = ListNode.from_list(list(range(n)))

        start = time.time()
        result = reverse_alternating_k(head, k)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
