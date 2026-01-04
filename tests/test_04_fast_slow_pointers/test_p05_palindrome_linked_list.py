"""Tests for palindrome_linked_list problem."""
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
def palindrome_linked_list():
    func = get_function("palindrome_linked_list")
    if func is None:
        pytest.skip("Function 'palindrome_linked_list' not registered.")
    return func


class TestPalindromeBasic:
    def test_example_1(self, palindrome_linked_list):
        head = create_linked_list([1, 2, 2, 1])
        assert palindrome_linked_list(head) is True

    def test_example_2(self, palindrome_linked_list):
        head = create_linked_list([1, 2])
        assert palindrome_linked_list(head) is False


class TestPalindromeEdgeCases:
    def test_single_element(self, palindrome_linked_list):
        head = ListNode(1)
        assert palindrome_linked_list(head) is True

    def test_two_same(self, palindrome_linked_list):
        head = create_linked_list([1, 1])
        assert palindrome_linked_list(head) is True

    def test_odd_length(self, palindrome_linked_list):
        head = create_linked_list([1, 2, 3, 2, 1])
        assert palindrome_linked_list(head) is True

    def test_not_palindrome(self, palindrome_linked_list):
        head = create_linked_list([1, 2, 3])
        assert palindrome_linked_list(head) is False

    def test_long_palindrome(self, palindrome_linked_list):
        values = list(range(50)) + list(range(49, -1, -1))
        head = create_linked_list(values)
        assert palindrome_linked_list(head) is True
