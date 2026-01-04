"""Tests for partition_equal_subset problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def partition_equal_subset():
    func = get_function("partition_equal_subset")
    if func is None:
        pytest.skip("Function 'partition_equal_subset' not registered.")
    return func


class TestPartitionEqualSubsetBasic:
    def test_example_1(self, partition_equal_subset):
        assert partition_equal_subset([1, 5, 11, 5]) is True

    def test_example_2(self, partition_equal_subset):
        assert partition_equal_subset([1, 2, 3, 5]) is False


class TestPartitionEqualSubsetEdgeCases:
    def test_single_element(self, partition_equal_subset):
        assert partition_equal_subset([1]) is False

    def test_two_equal(self, partition_equal_subset):
        assert partition_equal_subset([5, 5]) is True

    def test_odd_sum(self, partition_equal_subset):
        assert partition_equal_subset([1, 2, 3]) is True

    def test_all_ones(self, partition_equal_subset):
        assert partition_equal_subset([1, 1, 1, 1]) is True


@pytest.mark.performance
class TestPartitionEqualSubsetPerformance:
    def test_large_input(self, partition_equal_subset):
        nums = [1] * 100 + [2] * 100

        start = time.time()
        result = partition_equal_subset(nums)
        elapsed = time.time() - start

        assert result is True
        assert elapsed < 2.0
