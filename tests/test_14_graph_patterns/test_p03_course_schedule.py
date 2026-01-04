"""Tests for course_schedule problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def course_schedule():
    func = get_function("course_schedule")
    if func is None:
        pytest.skip("Function 'course_schedule' not registered.")
    return func


class TestCourseScheduleBasic:
    def test_simple_prerequisite(self, course_schedule):
        assert course_schedule(2, [[1, 0]]) is True

    def test_cycle(self, course_schedule):
        assert course_schedule(2, [[1, 0], [0, 1]]) is False

    def test_no_prerequisites(self, course_schedule):
        assert course_schedule(3, []) is True

    def test_chain(self, course_schedule):
        assert course_schedule(3, [[1, 0], [2, 1]]) is True


class TestCourseScheduleEdgeCases:
    def test_single_course(self, course_schedule):
        assert course_schedule(1, []) is True

    def test_multiple_prerequisites(self, course_schedule):
        assert course_schedule(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True

    def test_larger_cycle(self, course_schedule):
        assert course_schedule(3, [[0, 1], [1, 2], [2, 0]]) is False

    def test_disconnected_components(self, course_schedule):
        assert course_schedule(4, [[1, 0], [3, 2]]) is True


@pytest.mark.performance
class TestCourseSchedulePerformance:
    def test_large_input(self, course_schedule):
        n = 2000
        prereqs = [[i, i - 1] for i in range(1, n)]

        start = time.time()
        result = course_schedule(n, prereqs)
        elapsed = time.time() - start

        assert result is True
        assert elapsed < 1.0
