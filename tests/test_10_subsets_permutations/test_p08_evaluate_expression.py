"""Tests for evaluate_expression problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def evaluate_expression():
    func = get_function("evaluate_expression")
    if func is None:
        pytest.skip("Function 'evaluate_expression' not registered.")
    return func


class TestEvaluateExpressionBasic:
    def test_example_1(self, evaluate_expression):
        result = evaluate_expression("2-1-1")
        expected = [0, 2]
        assert sorted(result) == sorted(expected)

    def test_example_2(self, evaluate_expression):
        result = evaluate_expression("2*3-4*5")
        expected = [-34, -14, -10, -10, 10]
        assert sorted(result) == sorted(expected)

    def test_single_number(self, evaluate_expression):
        result = evaluate_expression("5")
        assert result == [5]


class TestEvaluateExpressionEdgeCases:
    def test_addition(self, evaluate_expression):
        result = evaluate_expression("1+2+3")
        # (1+2)+3 = 6, 1+(2+3) = 6
        assert sorted(result) == [6, 6]

    def test_mixed_operators(self, evaluate_expression):
        result = evaluate_expression("2+3*4")
        # (2+3)*4 = 20, 2+(3*4) = 14
        assert sorted(result) == [14, 20]


@pytest.mark.performance
class TestEvaluateExpressionPerformance:
    def test_longer_expression(self, evaluate_expression):
        expr = "1+2*3-4+5"

        start = time.time()
        result = evaluate_expression(expr)
        elapsed = time.time() - start

        assert len(result) > 0
        assert elapsed < 1.0
