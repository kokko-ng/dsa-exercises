"""Tests for intersection_of_two_arrays problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def intersection_of_two_arrays():
    func = get_function("intersection_of_two_arrays")
    if func is None:
        pytest.skip("Function 'intersection_of_two_arrays' not registered.")
    return func


class TestIntersectionBasic:
    def test_example_1(self, intersection_of_two_arrays):
        result = intersection_of_two_arrays([1, 2, 2, 1], [2, 2])
        assert sorted(result) == [2]

    def test_example_2(self, intersection_of_two_arrays):
        result = intersection_of_two_arrays([4, 9, 5], [9, 4, 9, 8, 4])
        assert sorted(result) == [4, 9]

    def test_no_intersection(self, intersection_of_two_arrays):
        result = intersection_of_two_arrays([1, 2, 3], [4, 5, 6])
        assert result == []


class TestIntersectionEdgeCases:
    def test_single_element_match(self, intersection_of_two_arrays):
        result = intersection_of_two_arrays([1], [1])
        assert result == [1]

    def test_single_element_no_match(self, intersection_of_two_arrays):
        result = intersection_of_two_arrays([1], [2])
        assert result == []

    def test_same_arrays(self, intersection_of_two_arrays):
        result = intersection_of_two_arrays([1, 2, 3], [1, 2, 3])
        assert sorted(result) == [1, 2, 3]

    def test_one_subset(self, intersection_of_two_arrays):
        result = intersection_of_two_arrays([1, 2], [1, 2, 3, 4])
        assert sorted(result) == [1, 2]

    def test_duplicates_in_both(self, intersection_of_two_arrays):
        result = intersection_of_two_arrays([1, 1, 2, 2], [2, 2, 3, 3])
        assert result == [2]
