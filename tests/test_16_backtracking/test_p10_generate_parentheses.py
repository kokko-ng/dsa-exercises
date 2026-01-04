"""Tests for generate_parentheses problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


def is_valid_parentheses(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0


@pytest.fixture
def generate_parentheses():
    func = get_function("generate_parentheses")
    if func is None:
        pytest.skip("Function 'generate_parentheses' not registered.")
    return func


class TestGenerateParenthesesBasic:
    def test_n_3(self, generate_parentheses):
        result = generate_parentheses(3)
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        assert sorted(result) == sorted(expected)
        for p in result:
            assert is_valid_parentheses(p)

    def test_n_1(self, generate_parentheses):
        result = generate_parentheses(1)
        assert result == ["()"]


class TestGenerateParenthesesEdgeCases:
    def test_n_2(self, generate_parentheses):
        result = generate_parentheses(2)
        expected = ["(())", "()()"]
        assert sorted(result) == sorted(expected)

    def test_n_4(self, generate_parentheses):
        result = generate_parentheses(4)
        assert len(result) == 14  # Catalan number C(4)
        for p in result:
            assert is_valid_parentheses(p)
            assert len(p) == 8
