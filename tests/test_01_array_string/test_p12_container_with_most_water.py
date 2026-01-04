"""Tests for container_with_most_water problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def container_with_most_water():
    func = get_function("container_with_most_water")
    if func is None:
        pytest.skip("Function 'container_with_most_water' not registered.")
    return func


class TestContainerWithMostWaterBasic:
    def test_example_case(self, container_with_most_water):
        assert container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_two_lines(self, container_with_most_water):
        assert container_with_most_water([1, 1]) == 1

    def test_increasing_heights(self, container_with_most_water):
        assert container_with_most_water([1, 2, 3, 4, 5]) == 6  # 2 * 3


class TestContainerWithMostWaterEdgeCases:
    def test_same_heights(self, container_with_most_water):
        assert container_with_most_water([5, 5, 5, 5]) == 15  # 5 * 3

    def test_one_tall_line(self, container_with_most_water):
        assert container_with_most_water([1, 1, 100, 1, 1]) == 4  # 1 * 4

    def test_decreasing_heights(self, container_with_most_water):
        assert container_with_most_water([5, 4, 3, 2, 1]) == 6  # 2 * 3


@pytest.mark.performance
class TestContainerWithMostWaterPerformance:
    def test_large_input(self, container_with_most_water):
        n = 100000
        height = list(range(1, n + 1))

        start = time.time()
        result = container_with_most_water(height)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0
