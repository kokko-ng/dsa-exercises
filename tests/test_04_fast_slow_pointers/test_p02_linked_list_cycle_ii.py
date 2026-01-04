"""Tests for linked_list_cycle_ii problem."""
import pytest
from dsa_helpers._function_registry import get as get_function
from dsa_helpers.data_structures import ListNode


def create_linked_list_with_cycle(values, pos):
    """Create a linked list with optional cycle, returns (head, cycle_node)."""
    if not values:
        return None, None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)

    cycle_node = None
    if pos >= 0:
        cycle_node = nodes[pos]
        current.next = cycle_node

    return head, cycle_node


@pytest.fixture
def linked_list_cycle_ii():
    func = get_function("linked_list_cycle_ii")
    if func is None:
        pytest.skip("Function 'linked_list_cycle_ii' not registered.")
    return func


class TestLinkedListCycleIIBasic:
    def test_example_1(self, linked_list_cycle_ii):
        head, cycle_node = create_linked_list_with_cycle([3, 2, 0, -4], 1)
        result = linked_list_cycle_ii(head)
        assert result is cycle_node

    def test_example_2(self, linked_list_cycle_ii):
        head, cycle_node = create_linked_list_with_cycle([1, 2], 0)
        result = linked_list_cycle_ii(head)
        assert result is cycle_node

    def test_example_3(self, linked_list_cycle_ii):
        head, _ = create_linked_list_with_cycle([1], -1)
        result = linked_list_cycle_ii(head)
        assert result is None


class TestLinkedListCycleIIEdgeCases:
    def test_empty_list(self, linked_list_cycle_ii):
        assert linked_list_cycle_ii(None) is None

    def test_single_with_cycle(self, linked_list_cycle_ii):
        head = ListNode(1)
        head.next = head
        assert linked_list_cycle_ii(head) is head

    def test_cycle_at_beginning(self, linked_list_cycle_ii):
        head, cycle_node = create_linked_list_with_cycle([1, 2, 3, 4], 0)
        result = linked_list_cycle_ii(head)
        assert result is cycle_node

    def test_cycle_in_middle(self, linked_list_cycle_ii):
        head, cycle_node = create_linked_list_with_cycle([1, 2, 3, 4, 5], 2)
        result = linked_list_cycle_ii(head)
        assert result is cycle_node
