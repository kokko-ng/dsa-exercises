"""Tests for expression_add_operators problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def expression_add_operators():
    func = get_function("expression_add_operators")
    if func is None:
        pytest.skip("Function 'expression_add_operators' not registered.")
    return func


class TestExpressionAddOperatorsBasic:
    def test_example_1(self, expression_add_operators):
        result = expression_add_operators("123", 6)
        expected = ["1*2*3", "1+2+3"]
        assert sorted(result) == sorted(expected)

    def test_example_2(self, expression_add_operators):
        result = expression_add_operators("232", 8)
        expected = ["2*3+2", "2+3*2"]
        assert sorted(result) == sorted(expected)

    def test_example_3(self, expression_add_operators):
        result = expression_add_operators("3456237490", 9191)
        assert result == []


class TestExpressionAddOperatorsEdgeCases:
    def test_single_digit(self, expression_add_operators):
        result = expression_add_operators("5", 5)
        assert result == ["5"]

    def test_no_solution(self, expression_add_operators):
        result = expression_add_operators("12", 100)
        assert result == []

    def test_with_zeros(self, expression_add_operators):
        result = expression_add_operators("105", 5)
        # Should have "1*0+5" and "10-5" but not "1*05"
        for expr in result:
            # Check no leading zeros in operands
            assert "0+" not in expr.replace("*0+", "").replace("-0+", "")

    def test_subtraction(self, expression_add_operators):
        result = expression_add_operators("123", 0)
        assert "1+2-3" in result
