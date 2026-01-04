"""Tests for count_unique_bst problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def count_unique_bst():
    func = get_function("count_unique_bst")
    if func is None:
        pytest.skip("Function 'count_unique_bst' not registered.")
    return func


class TestCountUniqueBstBasic:
    def test_example_1(self, count_unique_bst):
        assert count_unique_bst(3) == 5

    def test_example_2(self, count_unique_bst):
        assert count_unique_bst(1) == 1

    def test_example_3(self, count_unique_bst):
        assert count_unique_bst(4) == 14


class TestCountUniqueBstEdgeCases:
    def test_n_equals_2(self, count_unique_bst):
        assert count_unique_bst(2) == 2

    def test_n_equals_5(self, count_unique_bst):
        assert count_unique_bst(5) == 42

    def test_catalan_sequence(self, count_unique_bst):
        # Catalan numbers: 1, 1, 2, 5, 14, 42, 132, 429, 1430, ...
        expected = [1, 1, 2, 5, 14, 42, 132, 429, 1430]
        for n in range(1, 10):
            assert count_unique_bst(n) == expected[n]


@pytest.mark.performance
class TestCountUniqueBstPerformance:
    def test_large_n(self, count_unique_bst):
        start = time.time()
        result = count_unique_bst(19)
        elapsed = time.time() - start

        assert result == 1767263190  # Catalan(19)
        assert elapsed < 1.0
