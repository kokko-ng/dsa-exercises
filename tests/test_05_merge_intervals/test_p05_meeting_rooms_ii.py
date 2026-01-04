"""Tests for meeting_rooms_ii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def meeting_rooms_ii():
    """Get the user's meeting_rooms_ii implementation."""
    func = get_function("meeting_rooms_ii")
    if func is None:
        pytest.skip("Function 'meeting_rooms_ii' not registered. Run check(meeting_rooms_ii) in notebook.")
    return func


class TestMeetingRoomsIIBasic:
    """Basic functionality tests."""

    def test_two_rooms(self, meeting_rooms_ii):
        result = meeting_rooms_ii([[0, 30], [5, 10], [15, 20]])
        assert result == 2

    def test_one_room(self, meeting_rooms_ii):
        result = meeting_rooms_ii([[7, 10], [2, 4]])
        assert result == 1

    def test_all_overlap(self, meeting_rooms_ii):
        result = meeting_rooms_ii([[1, 5], [2, 6], [3, 7], [4, 8]])
        assert result == 4

    def test_sequential_meetings(self, meeting_rooms_ii):
        result = meeting_rooms_ii([[1, 2], [2, 3], [3, 4]])
        assert result == 1


class TestMeetingRoomsIIEdgeCases:
    """Edge case tests."""

    def test_single_meeting(self, meeting_rooms_ii):
        result = meeting_rooms_ii([[1, 5]])
        assert result == 1

    def test_same_start_time(self, meeting_rooms_ii):
        result = meeting_rooms_ii([[1, 10], [1, 5], [1, 3]])
        assert result == 3

    def test_partial_overlaps(self, meeting_rooms_ii):
        result = meeting_rooms_ii([[0, 5], [4, 10], [9, 15]])
        assert result == 2

    def test_chain_of_two(self, meeting_rooms_ii):
        result = meeting_rooms_ii([[1, 5], [2, 6], [6, 10], [7, 11]])
        assert result == 2


@pytest.mark.performance
class TestMeetingRoomsIIPerformance:
    """Performance tests."""

    def test_large_input(self, meeting_rooms_ii):
        n = 10000
        intervals = [[i, i + 100] for i in range(n)]

        start = time.time()
        result = meeting_rooms_ii(intervals)
        elapsed = time.time() - start

        assert result == 100
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
