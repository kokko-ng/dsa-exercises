"""Tests for reorder_list problem."""
import pytest
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


def create_linked_list(values):
    """Create a linked list from values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Convert linked list to Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


@pytest.fixture
def reorder_list():
    func = get_function("reorder_list")
    if func is None:
        pytest.skip("Function 'reorder_list' not registered.")
    return func


class TestReorderListBasic:
    def test_example_1(self, reorder_list):
        head = create_linked_list([1, 2, 3, 4])
        reorder_list(head)
        assert linked_list_to_list(head) == [1, 4, 2, 3]

    def test_example_2(self, reorder_list):
        head = create_linked_list([1, 2, 3, 4, 5])
        reorder_list(head)
        assert linked_list_to_list(head) == [1, 5, 2, 4, 3]


class TestReorderListEdgeCases:
    def test_single_element(self, reorder_list):
        head = ListNode(1)
        reorder_list(head)
        assert linked_list_to_list(head) == [1]

    def test_two_elements(self, reorder_list):
        head = create_linked_list([1, 2])
        reorder_list(head)
        assert linked_list_to_list(head) == [1, 2]

    def test_three_elements(self, reorder_list):
        head = create_linked_list([1, 2, 3])
        reorder_list(head)
        assert linked_list_to_list(head) == [1, 3, 2]

    def test_six_elements(self, reorder_list):
        head = create_linked_list([1, 2, 3, 4, 5, 6])
        reorder_list(head)
        assert linked_list_to_list(head) == [1, 6, 2, 5, 3, 4]
