"""Tests for middle_of_linked_list problem."""
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


@pytest.fixture
def middle_of_linked_list():
    func = get_function("middle_of_linked_list")
    if func is None:
        pytest.skip("Function 'middle_of_linked_list' not registered.")
    return func


class TestMiddleOfLinkedListBasic:
    def test_example_1(self, middle_of_linked_list):
        head = create_linked_list([1, 2, 3, 4, 5])
        result = middle_of_linked_list(head)
        assert result.val == 3

    def test_example_2(self, middle_of_linked_list):
        head = create_linked_list([1, 2, 3, 4, 5, 6])
        result = middle_of_linked_list(head)
        assert result.val == 4  # Second middle


class TestMiddleOfLinkedListEdgeCases:
    def test_single_element(self, middle_of_linked_list):
        head = ListNode(1)
        result = middle_of_linked_list(head)
        assert result.val == 1

    def test_two_elements(self, middle_of_linked_list):
        head = create_linked_list([1, 2])
        result = middle_of_linked_list(head)
        assert result.val == 2  # Second middle

    def test_three_elements(self, middle_of_linked_list):
        head = create_linked_list([1, 2, 3])
        result = middle_of_linked_list(head)
        assert result.val == 2

    def test_long_list(self, middle_of_linked_list):
        head = create_linked_list(list(range(1, 101)))
        result = middle_of_linked_list(head)
        assert result.val == 51  # Second middle for even length
