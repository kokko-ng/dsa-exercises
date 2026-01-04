"""Tests for string_permutations_by_changing_case problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def string_permutations_by_changing_case():
    func = get_function("string_permutations_by_changing_case")
    if func is None:
        pytest.skip("Function 'string_permutations_by_changing_case' not registered.")
    return func


class TestStringPermutationsByChangingCaseBasic:
    def test_example_1(self, string_permutations_by_changing_case):
        result = string_permutations_by_changing_case("a1b2")
        expected = ["a1b2", "a1B2", "A1b2", "A1B2"]
        assert len(result) == 4
        for s in expected:
            assert s in result

    def test_example_2(self, string_permutations_by_changing_case):
        result = string_permutations_by_changing_case("3z4")
        expected = ["3z4", "3Z4"]
        assert len(result) == 2
        for s in expected:
            assert s in result

    def test_example_3(self, string_permutations_by_changing_case):
        result = string_permutations_by_changing_case("12345")
        assert result == ["12345"]


class TestStringPermutationsByChangingCaseEdgeCases:
    def test_all_letters(self, string_permutations_by_changing_case):
        result = string_permutations_by_changing_case("ab")
        assert len(result) == 4  # 2^2

    def test_single_letter(self, string_permutations_by_changing_case):
        result = string_permutations_by_changing_case("a")
        assert len(result) == 2
        assert "a" in result
        assert "A" in result


@pytest.mark.performance
class TestStringPermutationsByChangingCasePerformance:
    def test_max_letters(self, string_permutations_by_changing_case):
        s = "abcdefghij"  # 10 letters = 2^10 = 1024 permutations

        start = time.time()
        result = string_permutations_by_changing_case(s)
        elapsed = time.time() - start

        assert len(result) == 1024
        assert elapsed < 1.0
