"""Tests for next_letter problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def next_letter():
    func = get_function("next_letter")
    if func is None:
        pytest.skip("Function 'next_letter' not registered.")
    return func


class TestNextLetterBasic:
    """Basic functionality tests."""

    def test_target_before_all(self, next_letter):
        assert next_letter(['c', 'f', 'j'], 'a') == 'c'

    def test_target_exists(self, next_letter):
        assert next_letter(['c', 'f', 'j'], 'c') == 'f'

    def test_wrap_around(self, next_letter):
        assert next_letter(['c', 'f', 'j'], 'j') == 'c'

    def test_target_between(self, next_letter):
        assert next_letter(['c', 'f', 'j'], 'd') == 'f'

    def test_target_last_letter(self, next_letter):
        assert next_letter(['a', 'b'], 'z') == 'a'


class TestNextLetterEdgeCases:
    """Edge case tests."""

    def test_two_elements(self, next_letter):
        assert next_letter(['a', 'z'], 'a') == 'z'

    def test_duplicate_letters(self, next_letter):
        assert next_letter(['c', 'c', 'f', 'f'], 'c') == 'f'

    def test_all_same(self, next_letter):
        # All same letters - should wrap to first
        assert next_letter(['c', 'c', 'c'], 'c') == 'c'

    def test_consecutive_letters(self, next_letter):
        assert next_letter(['a', 'b', 'c', 'd'], 'b') == 'c'

    def test_target_after_last_before_wrap(self, next_letter):
        assert next_letter(['a', 'c', 'e'], 'f') == 'a'


@pytest.mark.performance
class TestNextLetterPerformance:
    """Performance tests."""

    def test_large_input(self, next_letter):
        # Generate large sorted letter array
        letters = ['a'] * 100000 + ['m'] * 100000 + ['z'] * 100000

        start = time.time()
        result = next_letter(letters, 'b')
        elapsed = time.time() - start

        assert result == 'm'
        assert elapsed < 0.1
