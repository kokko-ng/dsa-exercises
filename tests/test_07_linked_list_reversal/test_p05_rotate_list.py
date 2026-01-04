"""Tests for rotate_list problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


@pytest.fixture
def rotate_list():
    """Get the user's rotate_list implementation."""
    func = get_function("rotate_list")
    if func is None:
        pytest.skip("Function 'rotate_list' not registered. Run check(rotate_list) in notebook.")
    return func


class TestRotateListBasic:
    """Basic functionality tests."""

    def test_rotate_by_2(self, rotate_list):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = rotate_list(head, 2)
        assert result.to_list() == [4, 5, 1, 2, 3]

    def test_rotate_by_4(self, rotate_list):
        head = ListNode.from_list([0, 1, 2])
        result = rotate_list(head, 4)
        assert result.to_list() == [2, 0, 1]

    def test_rotate_by_1(self, rotate_list):
        head = ListNode.from_list([1, 2, 3])
        result = rotate_list(head, 1)
        assert result.to_list() == [3, 1, 2]


class TestRotateListEdgeCases:
    """Edge case tests."""

    def test_empty_list(self, rotate_list):
        result = rotate_list(None, 5)
        assert result is None

    def test_single_node(self, rotate_list):
        head = ListNode(1)
        result = rotate_list(head, 100)
        assert result.to_list() == [1]

    def test_rotate_by_0(self, rotate_list):
        head = ListNode.from_list([1, 2, 3])
        result = rotate_list(head, 0)
        assert result.to_list() == [1, 2, 3]

    def test_rotate_by_length(self, rotate_list):
        head = ListNode.from_list([1, 2, 3])
        result = rotate_list(head, 3)
        assert result.to_list() == [1, 2, 3]

    def test_large_k(self, rotate_list):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = rotate_list(head, 2000000000)
        # 2000000000 % 5 = 0, so no change
        assert result.to_list() == [1, 2, 3, 4, 5]


@pytest.mark.performance
class TestRotateListPerformance:
    """Performance tests."""

    def test_large_list_large_k(self, rotate_list):
        n = 500
        head = ListNode.from_list(list(range(n)))

        start = time.time()
        result = rotate_list(head, 2000000000)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
