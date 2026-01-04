"""Tests for reverse_k_group problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


@pytest.fixture
def reverse_k_group():
    """Get the user's reverse_k_group implementation."""
    func = get_function("reverse_k_group")
    if func is None:
        pytest.skip("Function 'reverse_k_group' not registered. Run check(reverse_k_group) in notebook.")
    return func


class TestReverseKGroupBasic:
    """Basic functionality tests."""

    def test_k_equals_2(self, reverse_k_group):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_k_group(head, 2)
        assert result.to_list() == [2, 1, 4, 3, 5]

    def test_k_equals_3(self, reverse_k_group):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_k_group(head, 3)
        assert result.to_list() == [3, 2, 1, 4, 5]

    def test_k_equals_length(self, reverse_k_group):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_k_group(head, 5)
        assert result.to_list() == [5, 4, 3, 2, 1]

    def test_perfect_groups(self, reverse_k_group):
        head = ListNode.from_list([1, 2, 3, 4, 5, 6])
        result = reverse_k_group(head, 2)
        assert result.to_list() == [2, 1, 4, 3, 6, 5]


class TestReverseKGroupEdgeCases:
    """Edge case tests."""

    def test_k_equals_1(self, reverse_k_group):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = reverse_k_group(head, 1)
        assert result.to_list() == [1, 2, 3, 4, 5]

    def test_single_node(self, reverse_k_group):
        head = ListNode(1)
        result = reverse_k_group(head, 1)
        assert result.to_list() == [1]

    def test_k_greater_than_length(self, reverse_k_group):
        head = ListNode.from_list([1, 2, 3])
        result = reverse_k_group(head, 4)
        assert result.to_list() == [1, 2, 3]


@pytest.mark.performance
class TestReverseKGroupPerformance:
    """Performance tests."""

    def test_large_list(self, reverse_k_group):
        n = 5000
        k = 10
        head = ListNode.from_list(list(range(n)))

        start = time.time()
        result = reverse_k_group(head, k)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
