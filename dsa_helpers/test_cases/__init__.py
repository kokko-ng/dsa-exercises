"""Test case definitions for all DSA exercises.

Test cases are organized by category and combined into a single TEST_CASES registry.
"""

from dataclasses import dataclass
from typing import Any, Callable, Optional

from ..comparators import (
    frequency_sort_compare,
    nested_set_compare,
    palindrome_substring_compare,
    set_compare,
    sorted_compare,
    topological_order_compare,
    unordered_list_compare,
)


@dataclass
class TestCase:
    """A single test case."""

    name: str
    args: tuple[tuple[Any, ...], ...]
    expected: Any
    comparator: Optional[Callable[[Any, Any], bool]] = None
    is_performance: bool = False
    max_time: Optional[float] = None
    check_modified_arg: Optional[int] = None  # Index of arg to check if function modifies in-place
    is_class_test: bool = False  # True if testing a class with method calls


# Import test cases from each category module
from .array_string import ARRAY_STRING_TESTS  # noqa: E402
from .backtracking import BACKTRACKING_TESTS  # noqa: E402
from .binary_search import BINARY_SEARCH_TESTS  # noqa: E402
from .bit_manipulation import BIT_MANIPULATION_TESTS  # noqa: E402
from .cyclic_sort import CYCLIC_SORT_TESTS  # noqa: E402
from .dp import DP_TESTS  # noqa: E402
from .fast_slow import FAST_SLOW_TESTS  # noqa: E402
from .graph import GRAPH_TESTS  # noqa: E402
from .hash_map import HASH_MAP_TESTS  # noqa: E402
from .k_way_merge import K_WAY_MERGE_TESTS  # noqa: E402
from .linked_list import LINKED_LIST_TESTS  # noqa: E402
from .merge_intervals import MERGE_INTERVALS_TESTS  # noqa: E402
from .monotonic_stack import MONOTONIC_STACK_TESTS  # noqa: E402
from .subsets import SUBSETS_TESTS  # noqa: E402
from .top_k import TOP_K_TESTS  # noqa: E402
from .tree import TREE_TESTS  # noqa: E402
from .two_heaps import TWO_HEAPS_TESTS  # noqa: E402
from .two_pointers import TWO_POINTERS_TESTS  # noqa: E402

# Combine all test cases into a single registry
TEST_CASES: dict[str, list[TestCase]] = {
    **ARRAY_STRING_TESTS,
    **HASH_MAP_TESTS,
    **TWO_POINTERS_TESTS,
    **FAST_SLOW_TESTS,
    **MERGE_INTERVALS_TESTS,
    **CYCLIC_SORT_TESTS,
    **LINKED_LIST_TESTS,
    **TREE_TESTS,
    **TWO_HEAPS_TESTS,
    **SUBSETS_TESTS,
    **BINARY_SEARCH_TESTS,
    **TOP_K_TESTS,
    **K_WAY_MERGE_TESTS,
    **GRAPH_TESTS,
    **DP_TESTS,
    **BACKTRACKING_TESTS,
    **MONOTONIC_STACK_TESTS,
    **BIT_MANIPULATION_TESTS,
}

__all__ = [
    "TestCase",
    "TEST_CASES",
    # Comparators re-exported for submodules
    "frequency_sort_compare",
    "palindrome_substring_compare",
    "sorted_compare",
    "set_compare",
    "nested_set_compare",
    "unordered_list_compare",
    "topological_order_compare",
]
