"""Tests for maximize_capital problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def maximize_capital():
    func = get_function("maximize_capital")
    if func is None:
        pytest.skip("Function 'maximize_capital' not registered.")
    return func


class TestMaximizeCapitalBasic:
    def test_example_1(self, maximize_capital):
        result = maximize_capital(2, 0, [1, 2, 3], [0, 1, 1])
        assert result == 4

    def test_example_2(self, maximize_capital):
        result = maximize_capital(3, 0, [1, 2, 3], [0, 1, 2])
        assert result == 6

    def test_single_project(self, maximize_capital):
        result = maximize_capital(1, 0, [1], [0])
        assert result == 1

    def test_no_affordable_projects(self, maximize_capital):
        result = maximize_capital(2, 0, [1, 2], [5, 10])
        assert result == 0


class TestMaximizeCapitalEdgeCases:
    def test_more_k_than_projects(self, maximize_capital):
        result = maximize_capital(10, 0, [1, 2, 3], [0, 0, 0])
        assert result == 6

    def test_high_initial_capital(self, maximize_capital):
        result = maximize_capital(2, 100, [1, 2, 3], [0, 1, 2])
        assert result == 105  # Can do any 2, pick 2 and 3

    def test_zero_profits(self, maximize_capital):
        result = maximize_capital(2, 0, [0, 0, 0], [0, 0, 0])
        assert result == 0


@pytest.mark.performance
class TestMaximizeCapitalPerformance:
    def test_large_input(self, maximize_capital):
        n = 10000
        profits = list(range(1, n + 1))
        capital = list(range(n))

        start = time.time()
        result = maximize_capital(100, 0, profits, capital)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 2.0
