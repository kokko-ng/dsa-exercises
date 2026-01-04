"""Tests for all_paths_from_source problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def all_paths_from_source():
    func = get_function("all_paths_from_source")
    if func is None:
        pytest.skip("Function 'all_paths_from_source' not registered.")
    return func


class TestAllPathsFromSourceBasic:
    def test_simple_dag(self, all_paths_from_source):
        graph = [[1, 2], [3], [3], []]
        result = all_paths_from_source(graph)
        expected = [[0, 1, 3], [0, 2, 3]]
        assert sorted(result) == sorted(expected)

    def test_multiple_paths(self, all_paths_from_source):
        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        result = all_paths_from_source(graph)
        assert len(result) == 5
        for path in result:
            assert path[0] == 0
            assert path[-1] == 4


class TestAllPathsFromSourceEdgeCases:
    def test_two_nodes(self, all_paths_from_source):
        graph = [[1], []]
        result = all_paths_from_source(graph)
        assert result == [[0, 1]]

    def test_direct_path_only(self, all_paths_from_source):
        graph = [[1], [2], []]
        result = all_paths_from_source(graph)
        assert result == [[0, 1, 2]]

    def test_multiple_direct_edges(self, all_paths_from_source):
        graph = [[1, 2, 3], [], [], []]
        result = all_paths_from_source(graph)
        assert [0, 3] in result
