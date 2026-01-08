"""Test cases for Two Heaps problems (Category 09)."""

from ..comparators import reorganize_string_compare
from . import TestCase

TWO_HEAPS_TESTS: dict[str, list[TestCase]] = {
    "find_median_from_stream": [
        TestCase(
            "basic",
            (
                (
                    {
                        "ops": ["add_num", "add_num", "find_median", "add_num", "find_median"],
                        "vals": [1, 2, None, 3, None],
                    },
                ),
            ),
            [None, None, 1.5, None, 2.0],
            is_class_test=True,
        ),
        TestCase(
            "single",
            (({"ops": ["add_num", "find_median"], "vals": [5, None]},),),
            [None, 5.0],
            is_class_test=True,
        ),
        TestCase(
            "sorted input",
            (
                (
                    {
                        "ops": ["add_num", "add_num", "add_num", "find_median"],
                        "vals": [1, 2, 3, None],
                    },
                ),
            ),
            [None, None, None, 2.0],
            is_class_test=True,
        ),
        TestCase(
            "negative numbers",
            (
                (
                    {
                        "ops": ["add_num", "add_num", "find_median", "add_num", "find_median"],
                        "vals": [-1, -5, None, -3, None],
                    },
                ),
            ),
            [None, None, -3.0, None, -3.0],
            is_class_test=True,
        ),
        TestCase(
            "duplicates",
            (
                (
                    {
                        "ops": ["add_num", "add_num", "add_num", "find_median"],
                        "vals": [5, 5, 5, None],
                    },
                ),
            ),
            [None, None, None, 5.0],
            is_class_test=True,
        ),
    ],
    "sliding_window_median": [
        TestCase("basic", (([1, 3, -1, -3, 5, 3, 6, 7], 3),), [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]),
        TestCase("k=1", (([1, 2, 3], 1),), [1.0, 2.0, 3.0]),
        TestCase("k=len", (([1, 2, 3], 3),), [2.0]),
        TestCase("even k", (([1, 2, 3, 4], 2),), [1.5, 2.5, 3.5]),
        TestCase("single element", (([5], 1),), [5.0]),
        TestCase("duplicates", (([1, 1, 1, 1], 2),), [1.0, 1.0, 1.0]),
        TestCase("negative numbers", (([-1, -2, -3, -4], 2),), [-1.5, -2.5, -3.5]),
    ],
    "maximize_capital": [
        TestCase("basic", ((2, 0, [1, 2, 3], [0, 1, 1]),), 4),
        TestCase("all affordable", ((3, 0, [1, 2, 3], [0, 0, 0]),), 6),
        TestCase("none affordable", ((2, 0, [1, 2], [1, 1]),), 0),
        TestCase("single project", ((1, 1, [1], [0]),), 2),
        TestCase("more projects than k", ((1, 0, [1, 2, 3], [0, 0, 0]),), 3),
        TestCase("high initial capital", ((2, 100, [1, 2, 3], [0, 1, 2]),), 105),
        TestCase("k is zero", ((0, 5, [1, 2, 3], [0, 0, 0]),), 5),
        TestCase("empty projects", ((2, 10, [], []),), 10),
        TestCase("gradual unlock", ((3, 0, [1, 2, 3], [0, 1, 3]),), 6),
    ],
    "next_interval": [
        TestCase("basic", (([[1, 2], [2, 3], [0, 1], [3, 4]],),), [1, 3, 0, -1]),
        TestCase("no next", (([[1, 4], [2, 3], [3, 4]],),), [-1, 2, -1]),
        TestCase("single", (([[1, 2]],),), [-1]),
        TestCase("all same", (([[1, 2], [1, 2], [1, 2]],),), [-1, -1, -1]),
        TestCase("consecutive", (([[1, 2], [2, 3], [3, 4]],),), [1, 2, -1]),
        TestCase("self reference", (([[1, 1], [2, 2]],),), [0, 1]),
    ],
    "kth_smallest_in_sorted_matrix": [
        TestCase("basic", (([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),), 13),
        TestCase("first", (([[1, 2], [1, 3]], 1),), 1),
        TestCase("last", (([[1, 2], [3, 4]], 4),), 4),
        TestCase("single", (([[1]], 1),), 1),
        TestCase("negative values", (([[-5, -4], [-3, -2]], 2),), -4),
        TestCase("duplicates", (([[1, 1], [1, 2]], 3),), 1),
        TestCase("middle element", (([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5),), 5),
        TestCase("k at boundary", (([[1, 10], [2, 11]], 2),), 2),
    ],
    "merge_k_sorted_arrays": [
        TestCase("basic", (([[1, 4, 5], [1, 3, 4], [2, 6]],),), [1, 1, 2, 3, 4, 4, 5, 6]),
        TestCase("single array", (([[1, 2, 3]],),), [1, 2, 3]),
        TestCase("empty arrays", (([[], [1], []],),), [1]),
        TestCase("all empty", (([[], []],),), []),
        TestCase("negative values", (([[-3, -1, 0], [-2, 1, 2]],),), [-3, -2, -1, 0, 1, 2]),
        TestCase("single element arrays", (([[1], [2], [3]],),), [1, 2, 3]),
    ],
    "smallest_range_k_lists": [
        TestCase("basic", (([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],),), [20, 24]),
        TestCase("single lists", (([[1, 2, 3], [1, 2, 3], [1, 2, 3]],),), [1, 1]),
        TestCase("two lists", (([[1, 5], [2, 4]],),), [1, 2]),
        TestCase("single element lists", (([[1], [2], [3]],),), [1, 3]),
        TestCase("negative values", (([[-5, -1, 0], [-3, 2, 4], [-2, 1, 3]],),), [-2, 0]),
        TestCase("overlapping ranges", (([[1, 5, 8], [4, 12], [7, 8, 10]],),), [4, 7]),
        TestCase("single list", (([[1, 2, 3]],),), [1, 1]),
    ],
    "reorganize_string": [
        TestCase("possible", (("aab",),), "aba", reorganize_string_compare),
        TestCase("impossible", (("aaab",),), "", reorganize_string_compare),
        TestCase("single", (("a",),), "a", reorganize_string_compare),
        TestCase("two chars", (("aabb",),), "abab", reorganize_string_compare),
        TestCase("three chars", (("aabc",),), "abac", reorganize_string_compare),
        TestCase("all same", (("aaa",),), "", reorganize_string_compare),
        TestCase("many chars balanced", (("aabbccdd",),), "abcdabcd", reorganize_string_compare),
        TestCase("two same", (("aa",),), "", reorganize_string_compare),
        TestCase("long string", (("aaabbbccc",),), "abcabcabc", reorganize_string_compare),
    ],
}
