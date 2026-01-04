"""Tests for k_closest_points problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def k_closest_points():
    func = get_function("k_closest_points")
    if func is None:
        pytest.skip("Function 'k_closest_points' not registered.")
    return func


def distance_sq(point):
    return point[0] ** 2 + point[1] ** 2


class TestKClosestPointsBasic:
    """Basic functionality tests."""

    def test_single_closest(self, k_closest_points):
        result = k_closest_points([[1, 3], [-2, 2]], 1)
        assert len(result) == 1
        assert result[0] == [-2, 2]

    def test_two_closest(self, k_closest_points):
        result = k_closest_points([[3, 3], [5, -1], [-2, 4]], 2)
        assert len(result) == 2
        result_set = {tuple(p) for p in result}
        assert (3, 3) in result_set
        assert (-2, 4) in result_set

    def test_all_points(self, k_closest_points):
        points = [[1, 1], [2, 2], [3, 3]]
        result = k_closest_points(points, 3)
        assert len(result) == 3


class TestKClosestPointsEdgeCases:
    """Edge case tests."""

    def test_single_point(self, k_closest_points):
        result = k_closest_points([[1, 1]], 1)
        assert result == [[1, 1]]

    def test_origin_point(self, k_closest_points):
        result = k_closest_points([[0, 0], [1, 1], [2, 2]], 1)
        assert result == [[0, 0]]

    def test_negative_coordinates(self, k_closest_points):
        result = k_closest_points([[-1, -1], [-2, -2]], 1)
        assert result == [[-1, -1]]

    def test_same_distance(self, k_closest_points):
        result = k_closest_points([[1, 0], [0, 1], [-1, 0], [0, -1]], 2)
        assert len(result) == 2
        for p in result:
            assert distance_sq(p) == 1


@pytest.mark.performance
class TestKClosestPointsPerformance:
    """Performance tests."""

    def test_large_input(self, k_closest_points):
        import random
        points = [[random.randint(-10000, 10000), random.randint(-10000, 10000)]
                  for _ in range(10000)]
        k = 100

        start = time.time()
        result = k_closest_points(points, k)
        elapsed = time.time() - start

        assert len(result) == k
        assert elapsed < 1.0
