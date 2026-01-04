"""Tests for two_sum_ii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def two_sum_ii():
    func = get_function("two_sum_ii")
    if func is None:
        pytest.skip("Function 'two_sum_ii' not registered.")
    return func


class TestTwoSumIIBasic:
    def test_example_1(self, two_sum_ii):
        assert two_sum_ii([2, 7, 11, 15], 9) == [1, 2]

    def test_example_2(self, two_sum_ii):
        assert two_sum_ii([2, 3, 4], 6) == [1, 3]

    def test_example_3(self, two_sum_ii):
        assert two_sum_ii([-1, 0], -1) == [1, 2]

    def test_duplicates(self, two_sum_ii):
        assert two_sum_ii([1, 2, 2, 4], 4) == [2, 3]


class TestTwoSumIIEdgeCases:
    def test_two_elements(self, two_sum_ii):
        assert two_sum_ii([1, 5], 6) == [1, 2]

    def test_negative_numbers(self, two_sum_ii):
        assert two_sum_ii([-5, -3, 0, 2, 8], -8) == [1, 2]

    def test_zeros(self, two_sum_ii):
        assert two_sum_ii([0, 0, 3, 4], 0) == [1, 2]

    def test_target_at_end(self, two_sum_ii):
        assert two_sum_ii([1, 2, 3, 4, 5], 9) == [4, 5]


@pytest.mark.performance
class TestTwoSumIIPerformance:
    def test_large_input(self, two_sum_ii):
        n = 30000
        numbers = list(range(1, n + 1))
        target = numbers[-1] + numbers[-2]

        start = time.time()
        result = two_sum_ii(numbers, target)
        elapsed = time.time() - start

        assert result == [n - 1, n]
        assert elapsed < 1.0
