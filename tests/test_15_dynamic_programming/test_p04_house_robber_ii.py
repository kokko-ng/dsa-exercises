"""Tests for house_robber_ii problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def house_robber_ii():
    func = get_function("house_robber_ii")
    if func is None:
        pytest.skip("Function 'house_robber_ii' not registered.")
    return func


class TestHouseRobberIIBasic:
    def test_example_1(self, house_robber_ii):
        assert house_robber_ii([2, 3, 2]) == 3

    def test_example_2(self, house_robber_ii):
        assert house_robber_ii([1, 2, 3, 1]) == 4

    def test_example_3(self, house_robber_ii):
        assert house_robber_ii([1, 2, 3]) == 3


class TestHouseRobberIIEdgeCases:
    def test_single_house(self, house_robber_ii):
        assert house_robber_ii([5]) == 5

    def test_two_houses(self, house_robber_ii):
        assert house_robber_ii([1, 2]) == 2

    def test_all_same(self, house_robber_ii):
        assert house_robber_ii([5, 5, 5, 5]) == 10
