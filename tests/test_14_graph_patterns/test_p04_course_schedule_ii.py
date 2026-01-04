"""Tests for course_schedule_ii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


def is_valid_order(order, numCourses, prerequisites):
    """Check if the order is a valid topological sort."""
    if len(order) != numCourses:
        return False

    position = {course: i for i, course in enumerate(order)}

    for course, prereq in prerequisites:
        if position[prereq] > position[course]:
            return False

    return True


@pytest.fixture
def course_schedule_ii():
    func = get_function("course_schedule_ii")
    if func is None:
        pytest.skip("Function 'course_schedule_ii' not registered.")
    return func


class TestCourseScheduleIIBasic:
    def test_simple_prerequisite(self, course_schedule_ii):
        result = course_schedule_ii(2, [[1, 0]])
        assert is_valid_order(result, 2, [[1, 0]])

    def test_multiple_prerequisites(self, course_schedule_ii):
        prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = course_schedule_ii(4, prereqs)
        assert is_valid_order(result, 4, prereqs)

    def test_no_prerequisites(self, course_schedule_ii):
        result = course_schedule_ii(3, [])
        assert len(result) == 3
        assert set(result) == {0, 1, 2}


class TestCourseScheduleIIEdgeCases:
    def test_cycle(self, course_schedule_ii):
        result = course_schedule_ii(2, [[1, 0], [0, 1]])
        assert result == []

    def test_single_course(self, course_schedule_ii):
        result = course_schedule_ii(1, [])
        assert result == [0]

    def test_larger_cycle(self, course_schedule_ii):
        result = course_schedule_ii(3, [[0, 1], [1, 2], [2, 0]])
        assert result == []


@pytest.mark.performance
class TestCourseScheduleIIPerformance:
    def test_large_input(self, course_schedule_ii):
        n = 2000
        prereqs = [[i, i - 1] for i in range(1, n)]

        start = time.time()
        result = course_schedule_ii(n, prereqs)
        elapsed = time.time() - start

        assert is_valid_order(result, n, prereqs)
        assert elapsed < 1.0
