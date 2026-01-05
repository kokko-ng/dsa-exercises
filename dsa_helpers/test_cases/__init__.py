"""
Test case definitions for all DSA exercises.

Test cases are organized by category and combined into a single TEST_CASES registry.
"""

from dataclasses import dataclass
from typing import Any, Callable, Optional

from ..comparators import (
    nested_set_compare,
    set_compare,
    sorted_compare,
    topological_order_compare,
    unordered_list_compare,
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
from .array_string import ARRAY_STRING_TESTS  # noqa: E402
from .binary_search import BINARY_SEARCH_TESTS  # noqa: E402
from .cyclic_sort import CYCLIC_SORT_TESTS  # noqa: E402
from .graph import GRAPH_TESTS  # noqa: E402
from .hash_map import HASH_MAP_TESTS  # noqa: E402
from .merge_intervals import MERGE_INTERVALS_TESTS  # noqa: E402
from .monotonic_stack import MONOTONIC_STACK_TESTS  # noqa: E402
from .top_k import TOP_K_TESTS  # noqa: E402

# Combine all test cases into a single registry
TEST_CASES: dict[str, list[TestCase]] = {
    **ARRAY_STRING_TESTS,
    **HASH_MAP_TESTS,
    **MERGE_INTERVALS_TESTS,
    **CYCLIC_SORT_TESTS,
    **BINARY_SEARCH_TESTS,
    **TOP_K_TESTS,
    **GRAPH_TESTS,
    **MONOTONIC_STACK_TESTS,
}

__all__ = [
    "TestCase",
    "TEST_CASES",
    # Comparators re-exported for submodules
    "sorted_compare",
    "set_compare",
    "nested_set_compare",
    "unordered_list_compare",
    "topological_order_compare",
]
