"""Tests for balanced_parentheses problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def balanced_parentheses():
    func = get_function("balanced_parentheses")
    if func is None:
        pytest.skip("Function 'balanced_parentheses' not registered.")
    return func


def is_balanced(s):
    """Check if parentheses string is balanced."""
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


class TestBalancedParenthesesBasic:
    def test_example_1(self, balanced_parentheses):
        result = balanced_parentheses(3)
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        assert len(result) == 5
        for s in result:
            assert is_balanced(s)
            assert len(s) == 6

    def test_example_2(self, balanced_parentheses):
        result = balanced_parentheses(1)
        assert result == ["()"]

    def test_n_equals_2(self, balanced_parentheses):
        result = balanced_parentheses(2)
        expected = ["(())", "()()"]
        assert len(result) == 2
        for s in expected:
            assert s in result


class TestBalancedParenthesesEdgeCases:
    def test_n_equals_4(self, balanced_parentheses):
        result = balanced_parentheses(4)
        # Catalan(4) = 14
        assert len(result) == 14
        for s in result:
            assert is_balanced(s)


@pytest.mark.performance
class TestBalancedParenthesesPerformance:
    def test_n_equals_8(self, balanced_parentheses):
        start = time.time()
        result = balanced_parentheses(8)
        elapsed = time.time() - start

        # Catalan(8) = 1430
        assert len(result) == 1430
        assert elapsed < 2.0
