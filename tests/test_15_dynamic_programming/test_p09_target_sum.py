"""Tests for target_sum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def target_sum():
    func = get_function("target_sum")
    if func is None:
        pytest.skip("Function 'target_sum' not registered.")
    return func


class TestTargetSumBasic:
    def test_example_1(self, target_sum):
        assert target_sum([1, 1, 1, 1, 1], 3) == 5

    def test_example_2(self, target_sum):
        assert target_sum([1], 1) == 1


class TestTargetSumEdgeCases:
    def test_zero_target(self, target_sum):
        assert target_sum([1, 1], 0) == 2

    def test_impossible(self, target_sum):
        assert target_sum([1], 2) == 0

    def test_all_zeros(self, target_sum):
        assert target_sum([0, 0, 0], 0) == 8  # 2^3 ways


@pytest.mark.performance
class TestTargetSumPerformance:
    def test_large_input(self, target_sum):
        start = time.time()
        result = target_sum([1] * 20, 10)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 2.0
