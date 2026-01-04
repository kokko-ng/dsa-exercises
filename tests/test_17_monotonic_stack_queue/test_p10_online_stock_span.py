"""Tests for online_stock_span problem (StockSpanner class)."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def StockSpanner():
    """Get the user's StockSpanner implementation."""
    cls = get_function("StockSpanner")
    if cls is None:
        pytest.skip("Class 'StockSpanner' not registered. Run check(StockSpanner) in notebook.")
    return cls


class TestStockSpannerBasic:
    """Basic functionality tests."""

    def test_example_case(self, StockSpanner):
        spanner = StockSpanner()
        results = []
        for price in [100, 80, 60, 70, 60, 75, 85]:
            results.append(spanner.next(price))
        assert results == [1, 1, 1, 2, 1, 4, 6]

    def test_increasing_prices(self, StockSpanner):
        spanner = StockSpanner()
        results = []
        for price in [10, 20, 30, 40]:
            results.append(spanner.next(price))
        assert results == [1, 2, 3, 4]

    def test_decreasing_prices(self, StockSpanner):
        spanner = StockSpanner()
        results = []
        for price in [40, 30, 20, 10]:
            results.append(spanner.next(price))
        assert results == [1, 1, 1, 1]

    def test_constant_prices(self, StockSpanner):
        spanner = StockSpanner()
        results = []
        for price in [50, 50, 50, 50]:
            results.append(spanner.next(price))
        assert results == [1, 2, 3, 4]


class TestStockSpannerEdgeCases:
    """Edge case tests."""

    def test_single_price(self, StockSpanner):
        spanner = StockSpanner()
        assert spanner.next(100) == 1

    def test_two_prices_increasing(self, StockSpanner):
        spanner = StockSpanner()
        assert spanner.next(50) == 1
        assert spanner.next(100) == 2

    def test_two_prices_decreasing(self, StockSpanner):
        spanner = StockSpanner()
        assert spanner.next(100) == 1
        assert spanner.next(50) == 1

    def test_zigzag(self, StockSpanner):
        spanner = StockSpanner()
        results = []
        for price in [10, 20, 10, 20, 10]:
            results.append(spanner.next(price))
        assert results == [1, 2, 1, 4, 1]

    def test_peak_then_valley(self, StockSpanner):
        spanner = StockSpanner()
        results = []
        for price in [50, 60, 70, 60, 50]:
            results.append(spanner.next(price))
        assert results == [1, 2, 3, 1, 1]


@pytest.mark.performance
class TestStockSpannerPerformance:
    """Performance tests - require O(1) amortized per call."""

    def test_large_input(self, StockSpanner):
        spanner = StockSpanner()
        n = 100000

        start = time.time()
        last_span = 0
        for i in range(1, n + 1):
            last_span = spanner.next(i)
        elapsed = time.time() - start

        assert last_span == n
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
