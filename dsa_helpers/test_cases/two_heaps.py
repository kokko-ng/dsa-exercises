"""Test cases for Two Heaps problems (Category 09)."""

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
    ],
    "sliding_window_median": [
        TestCase("basic", (([1, 3, -1, -3, 5, 3, 6, 7], 3),), [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]),
        TestCase("k=1", (([1, 2, 3], 1),), [1.0, 2.0, 3.0]),
        TestCase("k=len", (([1, 2, 3], 3),), [2.0]),
        TestCase("even k", (([1, 2, 3, 4], 2),), [1.5, 2.5, 3.5]),
    ],
    "maximize_capital": [
        TestCase("basic", ((2, 0, [1, 2, 3], [0, 1, 1]),), 4),
        TestCase("all affordable", ((3, 0, [1, 2, 3], [0, 0, 0]),), 6),
        TestCase("none affordable", ((2, 0, [1, 2], [1, 1]),), 0),
        TestCase("single project", ((1, 1, [1], [0]),), 2),
    ],
    "next_interval": [
        TestCase("basic", (([[1, 2], [2, 3], [0, 1], [3, 4]],),), [1, 3, 0, -1]),
        TestCase("no next", (([[1, 4], [2, 3], [3, 4]],),), [-1, 2, -1]),
        TestCase("single", (([[1, 2]],),), [-1]),
        TestCase("all same", (([[1, 2], [1, 2], [1, 2]],),), [-1, -1, -1]),
    ],
    "kth_smallest_in_sorted_matrix": [
        TestCase("basic", (([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),), 13),
        TestCase("first", (([[1, 2], [1, 3]], 1),), 1),
        TestCase("last", (([[1, 2], [3, 4]], 4),), 4),
        TestCase("single", (([[1]], 1),), 1),
    ],
    "merge_k_sorted_arrays": [
        TestCase("basic", (([[1, 4, 5], [1, 3, 4], [2, 6]],),), [1, 1, 2, 3, 4, 4, 5, 6]),
        TestCase("single array", (([[1, 2, 3]],),), [1, 2, 3]),
        TestCase("empty arrays", (([[], [1], []],),), [1]),
        TestCase("all empty", (([[], []],),), []),
    ],
    "smallest_range_k_lists": [
        TestCase("basic", (([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],),), [20, 24]),
        TestCase("single lists", (([[1, 2, 3], [1, 2, 3], [1, 2, 3]],),), [1, 1]),
        TestCase("two lists", (([[1, 5], [2, 4]],),), [1, 2]),
    ],
    "reorganize_string": [
        TestCase("possible", (("aab",),), "aba"),
        TestCase("impossible", (("aaab",),), ""),
        TestCase("single", (("a",),), "a"),
        TestCase("two chars", (("aabb",),), "abab"),
    ],
}
