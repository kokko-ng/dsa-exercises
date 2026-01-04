"""Tests for reconstruct_itinerary problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def reconstruct_itinerary():
    func = get_function("reconstruct_itinerary")
    if func is None:
        pytest.skip("Function 'reconstruct_itinerary' not registered.")
    return func


class TestReconstructItineraryBasic:
    def test_example_1(self, reconstruct_itinerary):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        assert reconstruct_itinerary(tickets) == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    def test_example_2(self, reconstruct_itinerary):
        tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        assert reconstruct_itinerary(tickets) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]


class TestReconstructItineraryEdgeCases:
    def test_single_ticket(self, reconstruct_itinerary):
        tickets = [["JFK", "ATL"]]
        assert reconstruct_itinerary(tickets) == ["JFK", "ATL"]

    def test_lexical_order(self, reconstruct_itinerary):
        tickets = [["JFK", "ZZZ"], ["JFK", "AAA"], ["AAA", "JFK"]]
        result = reconstruct_itinerary(tickets)
        assert result == ["JFK", "AAA", "JFK", "ZZZ"]

    def test_multiple_visits_same_city(self, reconstruct_itinerary):
        tickets = [["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"], ["ATL", "SFO"]]
        result = reconstruct_itinerary(tickets)
        assert result[0] == "JFK"
        assert result[-1] == "SFO"
        assert len(result) == 5
