"""Tests for meeting_rooms problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def meeting_rooms():
    """Get the user's meeting_rooms implementation."""
    func = get_function("meeting_rooms")
    if func is None:
        pytest.skip("Function 'meeting_rooms' not registered. Run check(meeting_rooms) in notebook.")
    return func


class TestMeetingRoomsBasic:
    """Basic functionality tests."""

    def test_overlapping_meetings(self, meeting_rooms):
        result = meeting_rooms([[0, 30], [5, 10], [15, 20]])
        assert result == False

    def test_no_overlap(self, meeting_rooms):
        result = meeting_rooms([[7, 10], [2, 4]])
        assert result == True

    def test_adjacent_meetings(self, meeting_rooms):
        result = meeting_rooms([[1, 2], [2, 3], [3, 4]])
        assert result == True

    def test_single_meeting(self, meeting_rooms):
        result = meeting_rooms([[1, 5]])
        assert result == True


class TestMeetingRoomsEdgeCases:
    """Edge case tests."""

    def test_empty_list(self, meeting_rooms):
        result = meeting_rooms([])
        assert result == True

    def test_all_same_time(self, meeting_rooms):
        result = meeting_rooms([[1, 5], [1, 5], [1, 5]])
        assert result == False

    def test_partial_overlap(self, meeting_rooms):
        result = meeting_rooms([[1, 3], [2, 4]])
        assert result == False

    def test_nested_meeting(self, meeting_rooms):
        result = meeting_rooms([[1, 10], [3, 5]])
        assert result == False


@pytest.mark.performance
class TestMeetingRoomsPerformance:
    """Performance tests."""

    def test_large_input_no_overlap(self, meeting_rooms):
        n = 10000
        intervals = [[i * 2, i * 2 + 1] for i in range(n)]

        start = time.time()
        result = meeting_rooms(intervals)
        elapsed = time.time() - start

        assert result == True
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
