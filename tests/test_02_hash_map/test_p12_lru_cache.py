"""Tests for LRUCache problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def LRUCache():
    cls = get_function("LRUCache")
    if cls is None:
        pytest.skip("Class 'LRUCache' not registered.")
    return cls


class TestLRUCacheBasic:
    def test_example_1(self, LRUCache):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1
        cache.put(3, 3)  # Evicts key 2
        assert cache.get(2) == -1
        cache.put(4, 4)  # Evicts key 1
        assert cache.get(1) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4

    def test_single_capacity(self, LRUCache):
        cache = LRUCache(1)
        cache.put(1, 1)
        assert cache.get(1) == 1
        cache.put(2, 2)  # Evicts key 1
        assert cache.get(1) == -1
        assert cache.get(2) == 2


class TestLRUCacheEdgeCases:
    def test_update_existing(self, LRUCache):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)  # Update existing key
        assert cache.get(1) == 10
        cache.put(3, 3)  # Should evict 2 (LRU), not 1
        assert cache.get(2) == -1
        assert cache.get(1) == 10

    def test_get_updates_recency(self, LRUCache):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)  # Access key 1, making 2 the LRU
        cache.put(3, 3)  # Should evict 2
        assert cache.get(2) == -1
        assert cache.get(1) == 1
        assert cache.get(3) == 3

    def test_get_nonexistent(self, LRUCache):
        cache = LRUCache(2)
        assert cache.get(1) == -1
        cache.put(1, 1)
        assert cache.get(2) == -1


@pytest.mark.performance
class TestLRUCachePerformance:
    def test_many_operations(self, LRUCache):
        cache = LRUCache(1000)

        start = time.time()
        for i in range(100000):
            cache.put(i, i)
        for i in range(100000):
            cache.get(i)
        elapsed = time.time() - start

        assert elapsed < 2.0
