"""Tests for linked_list_cycle problem."""
import pytest
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


def create_linked_list_with_cycle(values, pos):
    """Create a linked list with optional cycle."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)

    if pos >= 0:
        current.next = nodes[pos]

    return head


@pytest.fixture
def linked_list_cycle():
    func = get_function("linked_list_cycle")
    if func is None:
        pytest.skip("Function 'linked_list_cycle' not registered.")
    return func


class TestLinkedListCycleBasic:
    def test_example_1(self, linked_list_cycle):
        head = create_linked_list_with_cycle([3, 2, 0, -4], 1)
        assert linked_list_cycle(head) is True

    def test_example_2(self, linked_list_cycle):
        head = create_linked_list_with_cycle([1, 2], 0)
        assert linked_list_cycle(head) is True

    def test_example_3(self, linked_list_cycle):
        head = create_linked_list_with_cycle([1], -1)
        assert linked_list_cycle(head) is False


class TestLinkedListCycleEdgeCases:
    def test_empty_list(self, linked_list_cycle):
        assert linked_list_cycle(None) is False

    def test_single_no_cycle(self, linked_list_cycle):
        head = ListNode(1)
        assert linked_list_cycle(head) is False

    def test_single_with_cycle(self, linked_list_cycle):
        head = ListNode(1)
        head.next = head
        assert linked_list_cycle(head) is True

    def test_long_list_no_cycle(self, linked_list_cycle):
        head = create_linked_list_with_cycle(list(range(100)), -1)
        assert linked_list_cycle(head) is False

    def test_cycle_at_end(self, linked_list_cycle):
        head = create_linked_list_with_cycle([1, 2, 3, 4, 5], 4)
        assert linked_list_cycle(head) is True
