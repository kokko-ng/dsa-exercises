"""Tests for fruit_into_baskets problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def fruit_into_baskets():
    func = get_function("fruit_into_baskets")
    if func is None:
        pytest.skip("Function 'fruit_into_baskets' not registered.")
    return func


class TestFruitBasic:
    def test_example_1(self, fruit_into_baskets):
        assert fruit_into_baskets([1, 2, 1]) == 3

    def test_example_2(self, fruit_into_baskets):
        assert fruit_into_baskets([0, 1, 2, 2]) == 3

    def test_example_3(self, fruit_into_baskets):
        assert fruit_into_baskets([1, 2, 3, 2, 2]) == 4


class TestFruitEdgeCases:
    def test_single_type(self, fruit_into_baskets):
        assert fruit_into_baskets([1, 1, 1, 1]) == 4

    def test_two_types(self, fruit_into_baskets):
        assert fruit_into_baskets([1, 2, 1, 2, 1, 2]) == 6

    def test_single_element(self, fruit_into_baskets):
        assert fruit_into_baskets([1]) == 1

    def test_three_types_alternating(self, fruit_into_baskets):
        assert fruit_into_baskets([1, 2, 3, 1, 2, 3]) == 2


@pytest.mark.performance
class TestFruitPerformance:
    def test_large_input(self, fruit_into_baskets):
        fruits = [1, 2] * 50000

        start = time.time()
        result = fruit_into_baskets(fruits)
        elapsed = time.time() - start

        assert result == 100000
        assert elapsed < 1.0
