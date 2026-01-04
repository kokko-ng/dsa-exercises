"""Tests for unique_paths problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def unique_paths():
    func = get_function("unique_paths")
    if func is None:
        pytest.skip("Function 'unique_paths' not registered.")
    return func


class TestUniquePathsBasic:
    def test_example_1(self, unique_paths):
        assert unique_paths(3, 7) == 28

    def test_example_2(self, unique_paths):
        assert unique_paths(3, 2) == 3


class TestUniquePathsEdgeCases:
    def test_single_cell(self, unique_paths):
        assert unique_paths(1, 1) == 1

    def test_single_row(self, unique_paths):
        assert unique_paths(1, 5) == 1

    def test_single_column(self, unique_paths):
        assert unique_paths(5, 1) == 1

    def test_square(self, unique_paths):
        assert unique_paths(3, 3) == 6


@pytest.mark.performance
class TestUniquePathsPerformance:
    def test_large_input(self, unique_paths):
        start = time.time()
        result = unique_paths(100, 100)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0
