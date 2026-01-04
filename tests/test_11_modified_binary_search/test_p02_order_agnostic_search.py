"""Tests for order_agnostic_search problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def order_agnostic_search():
    func = get_function("order_agnostic_search")
    if func is None:
        pytest.skip("Function 'order_agnostic_search' not registered.")
    return func


class TestOrderAgnosticSearchBasic:
    """Basic functionality tests."""

    def test_ascending_found(self, order_agnostic_search):
        assert order_agnostic_search([1, 2, 3, 4, 5, 6, 7], 5) == 4

    def test_descending_found_first(self, order_agnostic_search):
        assert order_agnostic_search([10, 6, 4], 10) == 0

    def test_descending_found_last(self, order_agnostic_search):
        assert order_agnostic_search([10, 6, 4], 4) == 2

    def test_ascending_not_found(self, order_agnostic_search):
        assert order_agnostic_search([1, 2, 3, 4, 5], 6) == -1

    def test_descending_not_found(self, order_agnostic_search):
        assert order_agnostic_search([10, 8, 6, 4, 2], 5) == -1


class TestOrderAgnosticSearchEdgeCases:
    """Edge case tests."""

    def test_single_element_found(self, order_agnostic_search):
        assert order_agnostic_search([5], 5) == 0

    def test_single_element_not_found(self, order_agnostic_search):
        assert order_agnostic_search([5], 3) == -1

    def test_two_elements_ascending(self, order_agnostic_search):
        assert order_agnostic_search([1, 2], 2) == 1

    def test_two_elements_descending(self, order_agnostic_search):
        assert order_agnostic_search([2, 1], 2) == 0

    def test_descending_middle(self, order_agnostic_search):
        assert order_agnostic_search([100, 80, 60, 40, 20], 60) == 2


@pytest.mark.performance
class TestOrderAgnosticSearchPerformance:
    """Performance tests."""

    def test_large_ascending(self, order_agnostic_search):
        n = 1000000
        nums = list(range(n))

        start = time.time()
        result = order_agnostic_search(nums, n - 1)
        elapsed = time.time() - start

        assert result == n - 1
        assert elapsed < 0.1

    def test_large_descending(self, order_agnostic_search):
        n = 1000000
        nums = list(range(n - 1, -1, -1))

        start = time.time()
        result = order_agnostic_search(nums, 0)
        elapsed = time.time() - start

        assert result == n - 1
        assert elapsed < 0.1
