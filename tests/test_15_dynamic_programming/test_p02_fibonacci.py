"""Tests for fibonacci problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def fibonacci():
    func = get_function("fibonacci")
    if func is None:
        pytest.skip("Function 'fibonacci' not registered.")
    return func


class TestFibonacciBasic:
    def test_zero(self, fibonacci):
        assert fibonacci(0) == 0

    def test_one(self, fibonacci):
        assert fibonacci(1) == 1

    def test_two(self, fibonacci):
        assert fibonacci(2) == 1

    def test_four(self, fibonacci):
        assert fibonacci(4) == 3

    def test_ten(self, fibonacci):
        assert fibonacci(10) == 55


class TestFibonacciEdgeCases:
    def test_twenty(self, fibonacci):
        assert fibonacci(20) == 6765

    def test_thirty(self, fibonacci):
        assert fibonacci(30) == 832040


@pytest.mark.performance
class TestFibonacciPerformance:
    def test_large_input(self, fibonacci):
        start = time.time()
        result = fibonacci(30)
        elapsed = time.time() - start

        assert result == 832040
        assert elapsed < 1.0
