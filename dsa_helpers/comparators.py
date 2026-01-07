"""
Comparison functions for test result validation.

These comparators handle various output formats where order may not matter
or special comparison logic is needed.
"""

from typing import Any


def sorted_compare(result: Any, expected: Any) -> bool:
    """Compare results after sorting (for problems with unordered output)."""
    try:
        return bool(sorted(result) == sorted(expected))
    except TypeError:
        return bool(result == expected)


def set_compare(result: Any, expected: Any) -> bool:
    """Compare as sets (for problems where order doesn't matter)."""
    if isinstance(result, str) and isinstance(expected, str):
        return bool(set(result) == set(expected))
    if isinstance(result, list) and isinstance(expected, list):
        if not result and not expected:
            return True
        if result and isinstance(result[0], list):
            return bool(set(map(tuple, result)) == set(map(tuple, expected)))
        return bool(set(result) == set(expected))
    return bool(result == expected)


def nested_set_compare(result: Any, expected: Any) -> bool:
    """Compare nested lists as sets of sorted sublists (for group_anagrams style)."""
    if not isinstance(result, list) or not isinstance(expected, list):
        return bool(result == expected)

    def normalize(groups: list[list[Any]]) -> set[tuple[Any, ...]]:
        return set(tuple(sorted(group)) for group in groups)

    return bool(normalize(result) == normalize(expected))


def unordered_list_compare(result: Any, expected: Any) -> bool:
    """Compare lists where inner order matters but outer order doesn't."""
    if not isinstance(result, list) or not isinstance(expected, list):
        return bool(result == expected)
    if len(result) != len(expected):
        return False
    return bool(sorted(map(tuple, result)) == sorted(map(tuple, expected)))


def topological_order_compare(result: Any, expected: Any) -> bool:
    """
    Compare topological orderings - valid if all dependencies respected.
    For course_schedule_ii style problems where multiple valid orderings exist.
    """
    if not isinstance(result, list) or not isinstance(expected, list):
        return bool(result == expected)
    if len(result) != len(expected):
        return False
    # Check that result contains same elements
    return bool(set(result) == set(expected))
