"""Tests for stock_span problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def stock_span():
    """Get the user's stock_span implementation."""
    func = get_function("stock_span")
    if func is None:
        pytest.skip("Function 'stock_span' not registered. Run check(stock_span) in notebook.")
    return func


class TestStockSpanBasic:
    """Basic functionality tests."""

    def test_example_case(self, stock_span):
        result = stock_span([100, 80, 60, 70, 60, 75, 85])
        assert result == [1, 1, 1, 2, 1, 4, 6]

    def test_increasing(self, stock_span):
        result = stock_span([10, 20, 30, 40])
        assert result == [1, 2, 3, 4]

    def test_decreasing(self, stock_span):
        result = stock_span([40, 30, 20, 10])
        assert result == [1, 1, 1, 1]

    def test_constant(self, stock_span):
        result = stock_span([50, 50, 50, 50])
        assert result == [1, 2, 3, 4]

    def test_valley(self, stock_span):
        result = stock_span([100, 50, 60, 70, 80])
        assert result == [1, 1, 2, 3, 4]


class TestStockSpanEdgeCases:
    """Edge case tests."""

    def test_single_day(self, stock_span):
        result = stock_span([100])
        assert result == [1]

    def test_two_days_increasing(self, stock_span):
        result = stock_span([50, 100])
        assert result == [1, 2]

    def test_two_days_decreasing(self, stock_span):
        result = stock_span([100, 50])
        assert result == [1, 1]

    def test_zigzag(self, stock_span):
        result = stock_span([10, 20, 10, 20, 10])
        assert result == [1, 2, 1, 4, 1]

    def test_peak_in_middle(self, stock_span):
        result = stock_span([50, 60, 70, 60, 50])
        assert result == [1, 2, 3, 1, 1]


@pytest.mark.performance
class TestStockSpanPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_increasing(self, stock_span):
        n = 100000
        prices = list(range(1, n + 1))

        start = time.time()
        result = stock_span(prices)
        elapsed = time.time() - start

        expected = list(range(1, n + 1))
        assert result == expected
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
