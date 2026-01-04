"""Tests for swap_pairs problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


@pytest.fixture
def swap_pairs():
    """Get the user's swap_pairs implementation."""
    func = get_function("swap_pairs")
    if func is None:
        pytest.skip("Function 'swap_pairs' not registered. Run check(swap_pairs) in notebook.")
    return func


class TestSwapPairsBasic:
    """Basic functionality tests."""

    def test_four_nodes(self, swap_pairs):
        head = ListNode.from_list([1, 2, 3, 4])
        result = swap_pairs(head)
        assert result.to_list() == [2, 1, 4, 3]

    def test_five_nodes(self, swap_pairs):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = swap_pairs(head)
        assert result.to_list() == [2, 1, 4, 3, 5]

    def test_two_nodes(self, swap_pairs):
        head = ListNode.from_list([1, 2])
        result = swap_pairs(head)
        assert result.to_list() == [2, 1]


class TestSwapPairsEdgeCases:
    """Edge case tests."""

    def test_empty_list(self, swap_pairs):
        result = swap_pairs(None)
        assert result is None

    def test_single_node(self, swap_pairs):
        head = ListNode(1)
        result = swap_pairs(head)
        assert result.to_list() == [1]

    def test_three_nodes(self, swap_pairs):
        head = ListNode.from_list([1, 2, 3])
        result = swap_pairs(head)
        assert result.to_list() == [2, 1, 3]


@pytest.mark.performance
class TestSwapPairsPerformance:
    """Performance tests."""

    def test_large_list(self, swap_pairs):
        n = 100
        head = ListNode.from_list(list(range(n)))

        start = time.time()
        result = swap_pairs(head)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
