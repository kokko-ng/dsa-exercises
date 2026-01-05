"""
Test checker for DSA exercises.

Provides the check() function that runs inline tests for user implementations
and displays formatted results in Jupyter notebooks. No pytest required.
"""

import time
import traceback
from typing import Callable, Union, Optional, Any, List, Tuple
from dataclasses import dataclass

try:
    from IPython.display import display, HTML
    HAS_IPYTHON = True
except ImportError:
    HAS_IPYTHON = False


@dataclass
class TestCase:
    """A single test case."""
    name: str
    args: tuple
    expected: Any
    comparator: Optional[Callable[[Any, Any], bool]] = None
    is_performance: bool = False
    max_time: Optional[float] = None  # seconds


@dataclass
class TestResult:
    """Result of running a test case."""
    name: str
    passed: bool
    error_msg: Optional[str] = None
    actual: Any = None
    expected: Any = None
    elapsed: Optional[float] = None


def sorted_result(result: Any, expected: Any) -> bool:
    """Compare results after sorting (for problems with unordered output)."""
    return sorted(result) == sorted(expected)


def set_compare(result: Any, expected: Any) -> bool:
    """Compare as sets (for problems where order doesn't matter)."""
    if isinstance(result, list) and isinstance(expected, list):
        return set(map(tuple, result)) == set(map(tuple, expected)) if result and isinstance(result[0], list) else set(result) == set(expected)
    return result == expected


# =============================================================================
# TEST CASES REGISTRY
# =============================================================================

TEST_CASES: dict[str, List[TestCase]] = {
    # -------------------------------------------------------------------------
    # 01_array_string
    # -------------------------------------------------------------------------
    "two_sum": [
        TestCase("simple case", (([2, 7, 11, 15], 9),), [0, 1], sorted_result),
        TestCase("middle elements", (([3, 2, 4], 6),), [1, 2], sorted_result),
        TestCase("duplicate values", (([3, 3], 6),), [0, 1], sorted_result),
        TestCase("negative numbers", (([-1, -2, -3, -4, -5], -8),), [2, 4], sorted_result),
        TestCase("mixed signs", (([-3, 4, 3, 90], 0),), [0, 2], sorted_result),
        TestCase("zeros", (([0, 4, 3, 0], 0),), [0, 3], sorted_result),
        TestCase("large numbers", (([1000000000, 2, 1000000000], 2000000000),), [0, 2], sorted_result),
        TestCase("performance", ((list(range(100000)), 199997),), [99998, 99999], sorted_result, is_performance=True, max_time=1.0),
    ],

    "valid_anagram": [
        TestCase("simple anagram", (("anagram", "nagaram"),), True),
        TestCase("not anagram", (("rat", "car"),), False),
        TestCase("empty strings", (("", ""),), True),
        TestCase("single char same", (("a", "a"),), True),
        TestCase("single char diff", (("a", "b"),), False),
        TestCase("same letters diff count", (("aab", "abb"),), False),
    ],

    "valid_palindrome": [
        TestCase("simple palindrome", (("A man, a plan, a canal: Panama",),), True),
        TestCase("not palindrome", (("race a car",),), False),
        TestCase("empty string", ((" ",),), True),
        TestCase("with numbers", (("0P",),), False),
    ],

    "reverse_string": [
        TestCase("simple", ((["h","e","l","l","o"],),), ["o","l","l","e","h"]),
        TestCase("even length", ((["H","a","n","n","a","h"],),), ["h","a","n","n","a","H"]),
        TestCase("single char", ((["a"],),), ["a"]),
        TestCase("two chars", ((["a","b"],),), ["b","a"]),
    ],

    "longest_common_prefix": [
        TestCase("common prefix", ((["flower","flow","flight"],),), "fl"),
        TestCase("no common prefix", ((["dog","racecar","car"],),), ""),
        TestCase("all same", ((["test","test","test"],),), "test"),
        TestCase("empty list", (([],),), ""),
        TestCase("single word", ((["alone"],),), "alone"),
    ],

    "remove_duplicates": [
        TestCase("with duplicates", (([1,1,2],),), 2),
        TestCase("more duplicates", (([0,0,1,1,1,2,2,3,3,4],),), 5),
        TestCase("no duplicates", (([1,2,3],),), 3),
        TestCase("all same", (([1,1,1,1],),), 1),
        TestCase("empty", (([],),), 0),
    ],

    "rotate_array": [
        TestCase("rotate by 3", (([1,2,3,4,5,6,7], 3),), [5,6,7,1,2,3,4]),
        TestCase("rotate by 2", (([-1,-100,3,99], 2),), [3,99,-1,-100]),
        TestCase("rotate by length", (([1,2,3], 3),), [1,2,3]),
        TestCase("rotate single", (([1], 1),), [1]),
    ],

    "move_zeroes": [
        TestCase("mixed", (([0,1,0,3,12],),), [1,3,12,0,0]),
        TestCase("single zero", (([0],),), [0]),
        TestCase("no zeros", (([1,2,3],),), [1,2,3]),
        TestCase("all zeros", (([0,0,0],),), [0,0,0]),
    ],

    "plus_one": [
        TestCase("simple", (([1,2,3],),), [1,2,4]),
        TestCase("carry", (([9],),), [1,0]),
        TestCase("multiple carry", (([9,9,9],),), [1,0,0,0]),
        TestCase("no carry", (([1,2,9],),), [1,3,0]),
    ],

    "merge_sorted_arrays": [
        TestCase("simple merge", (([1,2,3,0,0,0], 3, [2,5,6], 3),), [1,2,2,3,5,6]),
        TestCase("empty second", (([1], 1, [], 0),), [1]),
        TestCase("empty first", (([0], 0, [1], 1),), [1]),
    ],

    "product_except_self": [
        TestCase("simple", (([1,2,3,4],),), [24,12,8,6]),
        TestCase("with zero", (([-1,1,0,-3,3],),), [0,0,9,0,0]),
        TestCase("two elements", (([1,2],),), [2,1]),
    ],

    "container_with_most_water": [
        TestCase("example 1", (([1,8,6,2,5,4,8,3,7],),), 49),
        TestCase("example 2", (([1,1],),), 1),
        TestCase("decreasing", (([4,3,2,1,4],),), 16),
    ],

    "trapping_rain_water": [
        TestCase("example 1", (([0,1,0,2,1,0,1,3,2,1,2,1],),), 6),
        TestCase("example 2", (([4,2,0,3,2,5],),), 9),
        TestCase("no water", (([1,2,3],),), 0),
    ],

    "longest_substring_without_repeating": [
        TestCase("abcabcbb", (("abcabcbb",),), 3),
        TestCase("bbbbb", (("bbbbb",),), 1),
        TestCase("pwwkew", (("pwwkew",),), 3),
        TestCase("empty", (("",),), 0),
    ],

    "minimum_window_substring": [
        TestCase("example 1", (("ADOBECODEBANC", "ABC"),), "BANC"),
        TestCase("example 2", (("a", "a"),), "a"),
        TestCase("no window", (("a", "aa"),), ""),
    ],

    # -------------------------------------------------------------------------
    # 02_hash_map
    # -------------------------------------------------------------------------
    "group_anagrams": [
        TestCase("example", ((["eat","tea","tan","ate","nat","bat"],),), [["bat"],["nat","tan"],["ate","eat","tea"]], set_compare),
        TestCase("empty string", (([""]),), [[""]]),
        TestCase("single char", ((["a"],),), [["a"]]),
    ],

    "two_sum_ii": [
        TestCase("example 1", (([2,7,11,15], 9),), [1, 2]),
        TestCase("example 2", (([2,3,4], 6),), [1, 3]),
        TestCase("example 3", (([-1,0], -1),), [1, 2]),
    ],

    "contains_duplicate": [
        TestCase("has duplicate", (([1,2,3,1],),), True),
        TestCase("no duplicate", (([1,2,3,4],),), False),
        TestCase("multiple dups", (([1,1,1,3,3,4,3,2,4,2],),), True),
    ],

    "isomorphic_strings": [
        TestCase("egg add", (("egg", "add"),), True),
        TestCase("foo bar", (("foo", "bar"),), False),
        TestCase("paper title", (("paper", "title"),), True),
    ],

    "word_pattern": [
        TestCase("match", (("abba", "dog cat cat dog"),), True),
        TestCase("no match", (("abba", "dog cat cat fish"),), False),
        TestCase("extra pattern", (("aaaa", "dog cat cat dog"),), False),
    ],

    "happy_number": [
        TestCase("19 is happy", ((19,),), True),
        TestCase("2 is not happy", ((2,),), False),
        TestCase("1 is happy", ((1,),), True),
    ],

    "first_unique_character": [
        TestCase("leetcode", (("leetcode",),), 0),
        TestCase("loveleetcode", (("loveleetcode",),), 2),
        TestCase("aabb", (("aabb",),), -1),
    ],

    "intersection_of_two_arrays": [
        TestCase("example 1", (([1,2,2,1], [2,2]),), [2], set_compare),
        TestCase("example 2", (([4,9,5], [9,4,9,8,4]),), [4,9], set_compare),
    ],

    "longest_consecutive_sequence": [
        TestCase("example 1", (([100,4,200,1,3,2],),), 4),
        TestCase("example 2", (([0,3,7,2,5,8,4,6,0,1],),), 9),
        TestCase("empty", (([],),), 0),
    ],

    "subarray_sum_equals_k": [
        TestCase("example 1", (([1,1,1], 2),), 2),
        TestCase("example 2", (([1,2,3], 3),), 2),
        TestCase("negative", (([1,-1,0], 0),), 3),
    ],

    # -------------------------------------------------------------------------
    # 05_merge_intervals
    # -------------------------------------------------------------------------
    "merge_intervals": [
        TestCase("overlapping", (([[1,3],[2,6],[8,10],[15,18]],),), [[1,6],[8,10],[15,18]]),
        TestCase("touching", (([[1,4],[4,5]],),), [[1,5]]),
        TestCase("single", (([[1,4]],),), [[1,4]]),
    ],

    "insert_interval": [
        TestCase("middle insert", (([[1,3],[6,9]], [2,5]),), [[1,5],[6,9]]),
        TestCase("merge multiple", (([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),), [[1,2],[3,10],[12,16]]),
    ],

    "intervals_intersection": [
        TestCase("example", (([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]),), [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]),
    ],

    "meeting_rooms": [
        TestCase("overlapping", (([[0,30],[5,10],[15,20]],),), False),
        TestCase("no overlap", (([[7,10],[2,4]],),), True),
    ],

    "meeting_rooms_ii": [
        TestCase("example 1", (([[0,30],[5,10],[15,20]],),), 2),
        TestCase("example 2", (([[7,10],[2,4]],),), 1),
    ],

    # -------------------------------------------------------------------------
    # 06_cyclic_sort
    # -------------------------------------------------------------------------
    "cyclic_sort": [
        TestCase("unsorted", (([3,1,5,4,2],),), [1,2,3,4,5]),
        TestCase("reverse", (([5,4,3,2,1],),), [1,2,3,4,5]),
        TestCase("sorted", (([1,2,3,4,5],),), [1,2,3,4,5]),
    ],

    "find_missing_number": [
        TestCase("missing 2", (([4,0,3,1],),), 2),
        TestCase("missing 8", (([0,1,2,3,4,5,6,7,9],),), 8),
        TestCase("missing 0", (([1,2,3],),), 0),
    ],

    "find_all_missing_numbers": [
        TestCase("example 1", (([4,3,2,7,8,2,3,1],),), [5,6]),
        TestCase("example 2", (([1,1],),), [2]),
    ],

    "find_duplicate": [
        TestCase("example 1", (([1,3,4,2,2],),), 2),
        TestCase("example 2", (([3,1,3,4,2],),), 3),
    ],

    "find_all_duplicates": [
        TestCase("example", (([4,3,2,7,8,2,3,1],),), [2,3], set_compare),
        TestCase("no dups", (([1,2,3],),), []),
    ],

    # -------------------------------------------------------------------------
    # 08_tree_bfs_dfs (examples - these need TreeNode support)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # 11_modified_binary_search
    # -------------------------------------------------------------------------
    "binary_search": [
        TestCase("found", (([-1,0,3,5,9,12], 9),), 4),
        TestCase("not found", (([-1,0,3,5,9,12], 2),), -1),
        TestCase("first element", (([1,2,3,4,5], 1),), 0),
        TestCase("last element", (([1,2,3,4,5], 5),), 4),
    ],

    "order_agnostic_search": [
        TestCase("ascending found", (([1,2,3,4,5,6,7], 5),), 4),
        TestCase("descending found", (([10,6,4], 10),), 0),
        TestCase("not found", (([1,2,3,4], 0),), -1),
    ],

    "ceiling_of_number": [
        TestCase("exact match", (([4,6,10], 6),), 1),
        TestCase("ceiling", (([1,3,8,10,15], 12),), 4),
        TestCase("smaller than all", (([4,6,10], 1),), 0),
    ],

    "floor_of_number": [
        TestCase("exact match", (([4,6,10], 6),), 1),
        TestCase("floor", (([1,3,8,10,15], 12),), 3),
        TestCase("larger than all", (([1,3,8,10,15], 20),), 4),
    ],

    "next_letter": [
        TestCase("example 1", ((["c","f","j"], "a"),), "c"),
        TestCase("example 2", ((["c","f","j"], "c"),), "f"),
        TestCase("wrap around", ((["c","f","j"], "k"),), "c"),
    ],

    "number_range": [
        TestCase("found", (([5,7,7,8,8,10], 8),), [3, 4]),
        TestCase("not found", (([5,7,7,8,8,10], 6),), [-1, -1]),
        TestCase("single", (([1], 1),), [0, 0]),
    ],

    "search_in_rotated_array": [
        TestCase("found left", (([4,5,6,7,0,1,2], 0),), 4),
        TestCase("found right", (([4,5,6,7,0,1,2], 5),), 1),
        TestCase("not found", (([4,5,6,7,0,1,2], 3),), -1),
    ],

    "rotation_count": [
        TestCase("rotated", (([10,15,1,3,8],),), 2),
        TestCase("not rotated", (([1,2,3,4,5],),), 0),
        TestCase("fully rotated", (([4,5,7,9,10,-1,2],),), 5),
    ],

    # -------------------------------------------------------------------------
    # 12_top_k_elements
    # -------------------------------------------------------------------------
    "top_k_frequent": [
        TestCase("example 1", (([1,1,1,2,2,3], 2),), [1,2], set_compare),
        TestCase("single", (([1], 1),), [1]),
    ],

    "kth_largest_element": [
        TestCase("example 1", (([3,2,1,5,6,4], 2),), 5),
        TestCase("example 2", (([3,2,3,1,2,4,5,5,6], 4),), 4),
    ],

    "k_closest_points": [
        TestCase("example 1", (([[1,3],[-2,2]], 1),), [[-2,2]]),
        TestCase("example 2", (([[3,3],[5,-1],[-2,4]], 2),), [[3,3],[-2,4]], set_compare),
    ],

    # -------------------------------------------------------------------------
    # 14_graph_patterns
    # -------------------------------------------------------------------------
    "number_of_islands": [
        TestCase("example 1", (([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],),), 1),
        TestCase("example 2", (([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]],),), 3),
    ],

    "course_schedule": [
        TestCase("possible", ((2, [[1,0]]),), True),
        TestCase("impossible", ((2, [[1,0],[0,1]]),), False),
    ],

    "course_schedule_ii": [
        TestCase("example 1", ((2, [[1,0]]),), [0,1]),
        TestCase("example 2", ((4, [[1,0],[2,0],[3,1],[3,2]]),), [0,1,2,3]),  # or [0,2,1,3]
    ],

    # -------------------------------------------------------------------------
    # 17_monotonic_stack_queue
    # -------------------------------------------------------------------------
    "next_greater_element": [
        TestCase("example 1", (([4,1,2], [1,3,4,2]),), [-1,3,-1]),
        TestCase("example 2", (([2,4], [1,2,3,4]),), [3,-1]),
    ],

    "daily_temperatures": [
        TestCase("example 1", (([73,74,75,71,69,72,76,73],),), [1,1,4,2,1,1,0,0]),
        TestCase("decreasing", (([30,29,28,27],),), [0,0,0,0]),
    ],

    "largest_rectangle_histogram": [
        TestCase("example 1", (([2,1,5,6,2,3],),), 10),
        TestCase("example 2", (([2,4],),), 4),
    ],

    "remove_k_digits": [
        TestCase("example 1", (("1432219", 3),), "1219"),
        TestCase("example 2", (("10200", 1),), "200"),
        TestCase("example 3", (("10", 2),), "0"),
    ],
}


# =============================================================================
# TEST RUNNER
# =============================================================================

def _run_test(func: Callable, test: TestCase) -> TestResult:
    """Run a single test case."""
    try:
        start = time.time()
        # Unpack args - test.args is a tuple of arguments
        actual = func(*test.args[0])
        elapsed = time.time() - start

        # Check result
        if test.comparator:
            passed = test.comparator(actual, test.expected)
        else:
            passed = actual == test.expected

        # Check performance constraint
        if passed and test.max_time and elapsed > test.max_time:
            return TestResult(
                name=test.name,
                passed=False,
                error_msg=f"Too slow: {elapsed:.2f}s (max: {test.max_time}s)",
                actual=actual,
                expected=test.expected,
                elapsed=elapsed
            )

        if passed:
            return TestResult(name=test.name, passed=True, elapsed=elapsed)
        else:
            return TestResult(
                name=test.name,
                passed=False,
                error_msg="Wrong answer",
                actual=actual,
                expected=test.expected,
                elapsed=elapsed
            )
    except Exception as e:
        return TestResult(
            name=test.name,
            passed=False,
            error_msg=f"{type(e).__name__}: {str(e)}"
        )


def _display_html(html: str) -> None:
    """Display HTML in notebook or print for terminal."""
    if HAS_IPYTHON:
        display(HTML(html))
    else:
        # Strip HTML tags for terminal output
        import re
        text = re.sub(r'<[^>]+>', '', html)
        text = text.replace('&#x2705;', '[PASS]')
        text = text.replace('&#x274C;', '[FAIL]')
        text = text.replace('&#x1F4A1;', '[TIP]')
        text = text.replace('&#x1F680;', '[PERF]')
        text = text.replace('&nbsp;', ' ')
        print(text)


def _display_results(func_name: str, results: List[TestResult], performance: bool) -> None:
    """Format and display test results in notebook-friendly format."""
    passed_count = sum(1 for r in results if r.passed)
    total = len(results)
    all_passed = passed_count == total

    if total == 0:
        html = f"""
        <div style="padding: 15px; background: #fff3cd; border-left: 4px solid #ffc107;
                    margin: 10px 0; border-radius: 4px;">
            <div style="font-size: 18px; margin-bottom: 8px;">
                &#x26A0; <strong style="color: #856404;">No tests found</strong>
            </div>
            <div style="color: #856404;">
                No test cases defined for function <code>{func_name}</code>.
            </div>
        </div>
        """
        _display_html(html)
        return

    if all_passed:
        perf_msg = ""
        if performance:
            perf_msg = """<div style='margin-top: 8px; color: #155724;'>
                &#x1F680; Performance tests passed!</div>"""

        html = f"""
        <div style="padding: 15px; background: #d4edda; border-left: 4px solid #28a745;
                    margin: 10px 0; border-radius: 4px;">
            <div style="font-size: 18px; margin-bottom: 8px;">
                &#x2705; <strong style="color: #28a745;">All tests passed!</strong>
            </div>
            <div style="color: #155724;">
                <code>{func_name}</code>: {passed_count}/{total} tests passed
            </div>
            {perf_msg}
        </div>
        """
    else:
        # Find first failing test for details
        failed = [r for r in results if not r.passed]
        first_fail = failed[0]

        error_details = f"Test: {first_fail.name}\n"
        if first_fail.error_msg:
            error_details += f"Error: {first_fail.error_msg}\n"
        if first_fail.actual is not None:
            error_details += f"Got:      {repr(first_fail.actual)}\n"
        if first_fail.expected is not None:
            error_details += f"Expected: {repr(first_fail.expected)}"

        # Escape HTML characters
        error_details = error_details.replace('&', '&amp;')
        error_details = error_details.replace('<', '&lt;')
        error_details = error_details.replace('>', '&gt;')

        html = f"""
        <div style="padding: 15px; background: #f8d7da; border-left: 4px solid #dc3545;
                    margin: 10px 0; border-radius: 4px;">
            <div style="font-size: 18px; margin-bottom: 8px;">
                &#x274C; <strong style="color: #dc3545;">Tests failed</strong>
            </div>
            <div style="color: #721c24;">
                <code>{func_name}</code>: {passed_count}/{total} tests passed
            </div>
            <div style="margin-top: 10px; padding: 10px; background: #fff; border-radius: 4px;
                        font-family: monospace; font-size: 13px; white-space: pre-wrap;
                        color: #333; max-height: 300px; overflow-y: auto;">
{error_details}
            </div>
            <div style="margin-top: 10px; color: #721c24; font-size: 13px;">
                &#x1F4A1; Tip: Use <code>hint("{func_name}")</code> for guidance
            </div>
        </div>
        """

    _display_html(html)


def check(function_or_name: Union[Callable, str], *,
          verbose: bool = False,
          performance: bool = False) -> bool:
    """
    Run tests for a given function and display results in the notebook.

    Args:
        function_or_name: Either a function object or string function name
        verbose: Show detailed test output for each test
        performance: Run performance tests (if available)

    Returns:
        True if all tests passed, False otherwise

    Usage:
        check(two_sum)
        check("two_sum")
        check(two_sum, performance=True)
        check(two_sum, verbose=True)
    """
    # Handle both function objects and string names
    if callable(function_or_name):
        func_name = function_or_name.__name__
        func_obj = function_or_name
    else:
        func_name = str(function_or_name)
        func_obj = None

    # Get function from registry if not provided directly
    if func_obj is None:
        from . import _function_registry
        func_obj = _function_registry.get(func_name)
        if func_obj is None:
            html = f"""
            <div style="padding: 10px; background: #fee; border-left: 4px solid #c00; margin: 10px 0;">
                <strong style="color: #c00;">Error:</strong> Function '{func_name}' not found.
                Make sure to pass the function directly: <code>check({func_name})</code>
            </div>
            """
            _display_html(html)
            return False
    else:
        # Register the function for future use
        from . import _function_registry
        _function_registry.register(func_name, func_obj)

    # Get test cases
    if func_name not in TEST_CASES:
        html = f"""
        <div style="padding: 10px; background: #fee; border-left: 4px solid #c00; margin: 10px 0;">
            <strong style="color: #c00;">Error:</strong> No tests found for function '{func_name}'
        </div>
        """
        _display_html(html)
        return False

    all_tests = TEST_CASES[func_name]

    # Filter tests based on performance flag
    if performance:
        tests = [t for t in all_tests if t.is_performance]
    else:
        tests = [t for t in all_tests if not t.is_performance]

    # Run tests
    results = []
    for test in tests:
        result = _run_test(func_obj, test)
        results.append(result)

        if verbose:
            status = "✓" if result.passed else "✗"
            print(f"  {status} {test.name}", end="")
            if result.elapsed:
                print(f" ({result.elapsed*1000:.1f}ms)")
            else:
                print()
            if not result.passed and result.error_msg:
                print(f"    Error: {result.error_msg}")

    # Display results
    _display_results(func_name, results, performance)

    return all(r.passed for r in results)


def check_all(category: Optional[str] = None, *, performance: bool = False) -> dict:
    """
    Run tests for all functions, optionally filtered by category.

    Args:
        category: Function name prefix to filter (e.g., "two_sum")
        performance: Include performance tests

    Returns:
        Dict mapping function names to pass/fail status
    """
    results = {}

    for func_name in TEST_CASES:
        if category and category not in func_name:
            continue

        # Try to get function from registry
        from . import _function_registry
        func_obj = _function_registry.get(func_name)

        if func_obj is None:
            results[func_name] = None  # Not implemented
            continue

        all_tests = TEST_CASES[func_name]
        if performance:
            tests = [t for t in all_tests if t.is_performance]
        else:
            tests = [t for t in all_tests if not t.is_performance]

        test_results = [_run_test(func_obj, t) for t in tests]
        results[func_name] = all(r.passed for r in test_results)

    return results
