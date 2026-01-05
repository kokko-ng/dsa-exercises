"""
Test case definitions for all DSA exercises.

Test cases are organized by category and combined into a single TEST_CASES registry.
"""

from dataclasses import dataclass
from typing import Any, Callable, Optional, List

from ..comparators import (
    sorted_compare,
    set_compare,
    nested_set_compare,
    unordered_list_compare,
    topological_order_compare,
)


@dataclass
class TestCase:
    """A single test case."""
    name: str
    args: tuple
    expected: Any
    comparator: Optional[Callable[[Any, Any], bool]] = None
    is_performance: bool = False
    max_time: Optional[float] = None


# Import test cases from each category module
from .array_string import ARRAY_STRING_TESTS
from .hash_map import HASH_MAP_TESTS
from .merge_intervals import MERGE_INTERVALS_TESTS
from .cyclic_sort import CYCLIC_SORT_TESTS
from .binary_search import BINARY_SEARCH_TESTS
from .top_k import TOP_K_TESTS
from .graph import GRAPH_TESTS
from .monotonic_stack import MONOTONIC_STACK_TESTS

# Combine all test cases into a single registry
TEST_CASES: dict[str, List[TestCase]] = {
    **ARRAY_STRING_TESTS,
    **HASH_MAP_TESTS,
    **MERGE_INTERVALS_TESTS,
    **CYCLIC_SORT_TESTS,
    **BINARY_SEARCH_TESTS,
    **TOP_K_TESTS,
    **GRAPH_TESTS,
    **MONOTONIC_STACK_TESTS,
}

__all__ = ['TestCase', 'TEST_CASES']
