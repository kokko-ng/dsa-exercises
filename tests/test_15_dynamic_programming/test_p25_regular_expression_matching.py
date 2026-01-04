"""Tests for regular_expression_matching problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def regular_expression_matching():
    func = get_function("regular_expression_matching")
    if func is None:
        pytest.skip("Function 'regular_expression_matching' not registered.")
    return func


class TestRegularExpressionMatchingBasic:
    def test_example_1(self, regular_expression_matching):
        assert regular_expression_matching("aa", "a") is False

    def test_example_2(self, regular_expression_matching):
        assert regular_expression_matching("aa", "a*") is True

    def test_example_3(self, regular_expression_matching):
        assert regular_expression_matching("ab", ".*") is True


class TestRegularExpressionMatchingEdgeCases:
    def test_empty_pattern(self, regular_expression_matching):
        assert regular_expression_matching("", "") is True
        assert regular_expression_matching("a", "") is False

    def test_dot(self, regular_expression_matching):
        assert regular_expression_matching("ab", "..") is True
        assert regular_expression_matching("abc", "..") is False

    def test_star_zero(self, regular_expression_matching):
        assert regular_expression_matching("", "a*") is True

    def test_complex(self, regular_expression_matching):
        assert regular_expression_matching("aab", "c*a*b") is True

    def test_mississippi(self, regular_expression_matching):
        assert regular_expression_matching("mississippi", "mis*is*p*.") is False


@pytest.mark.performance
class TestRegularExpressionMatchingPerformance:
    def test_medium_input(self, regular_expression_matching):
        s = "a" * 20
        p = "a*" * 10

        start = time.time()
        result = regular_expression_matching(s, p)
        elapsed = time.time() - start

        assert result is True
        assert elapsed < 1.0
