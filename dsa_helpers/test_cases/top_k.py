"""Test cases for Top K Elements problems (Category 12)."""

from . import TestCase, set_compare, unordered_list_compare

TOP_K_TESTS = {
    "top_k_frequent": [
        TestCase("example 1", (([1, 1, 1, 2, 2, 3], 2),), [1, 2], set_compare),
        TestCase("single", (([1], 1),), [1]),
        TestCase("all same frequency", (([1, 2, 3], 2),), None, None),  # Multiple valid answers
        TestCase("negative numbers", (([-1, -1, -2, -2, -2], 1),), [-2]),
        TestCase("k equals unique", (([1, 1, 2, 2, 3, 3], 3),), [1, 2, 3], set_compare),
        TestCase("one dominant", (([1, 1, 1, 1, 2, 3, 4], 1),), [1]),
        TestCase("all unique", (([1, 2, 3, 4, 5], 3),), None, None),  # Multiple valid
        TestCase("two groups", (([1, 1, 1, 2, 2, 2, 3], 2),), [1, 2], set_compare),
    ],

    "kth_largest_element": [
        TestCase("example 1", (([3, 2, 1, 5, 6, 4], 2),), 5),
        TestCase("example 2", (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),), 4),
        TestCase("single element", (([1], 1),), 1),
        TestCase("all same", (([2, 2, 2, 2], 2),), 2),
        TestCase("with negatives", (([-1, -2, -3, -4], 2),), -2),
        TestCase("k equals length", (([5, 3, 1, 4, 2], 5),), 1),
        TestCase("sorted ascending", (([1, 2, 3, 4, 5], 3),), 3),
        TestCase("sorted descending", (([5, 4, 3, 2, 1], 3),), 3),
        TestCase("with duplicates", (([1, 2, 2, 3, 3, 3], 2),), 3),
    ],

    "k_closest_points": [
        TestCase("example 1", (([[1, 3], [-2, 2]], 1),), [[-2, 2]]),
        TestCase("example 2", (([[3, 3], [5, -1], [-2, 4]], 2),), [[3, 3], [-2, 4]], unordered_list_compare),
        TestCase("origin", (([[0, 0], [1, 1]], 1),), [[0, 0]]),
        TestCase("same distance", (([[1, 0], [0, 1]], 2),), [[1, 0], [0, 1]], unordered_list_compare),
        TestCase("single point", (([[5, 5]], 1),), [[5, 5]]),
        TestCase("negative coords", (([[-1, -1], [-2, -2], [1, 1]], 2),), [[-1, -1], [1, 1]], unordered_list_compare),
        TestCase("all same distance", (([[1, 0], [0, 1], [-1, 0], [0, -1]], 2),), None, None),  # Multiple valid
        TestCase("on axes", (([[3, 0], [0, 4], [0, 0]], 2),), [[0, 0], [3, 0]], unordered_list_compare),
    ],

    "sort_characters_by_frequency": [
        TestCase("tree", (("tree",),), None, None),  # "eert" or "eetr"
        TestCase("cccaaa", (("cccaaa",),), None, None),  # "cccaaa" or "aaaccc"
        TestCase("Aabb", (("Aabb",),), None, None),  # "bbAa" or "bbaA"
        TestCase("single char", (("a",),), "a"),
        TestCase("all same", (("aaaa",),), "aaaa"),
        TestCase("all unique", (("abc",),), None, None),  # Any order valid
        TestCase("numbers", (("112233",),), None, None),  # Multiple valid
    ],

    "find_k_closest_elements": [
        TestCase("example 1", (([1, 2, 3, 4, 5], 4, 3),), [1, 2, 3, 4]),
        TestCase("example 2", (([1, 2, 3, 4, 5], 4, -1),), [1, 2, 3, 4]),
        TestCase("x larger than all", (([1, 2, 3, 4, 5], 4, 10),), [2, 3, 4, 5]),
        TestCase("x in middle", (([1, 2, 3, 4, 5], 3, 3),), [2, 3, 4]),
        TestCase("k equals array", (([1, 2, 3], 3, 2),), [1, 2, 3]),
        TestCase("single element", (([5], 1, 5),), [5]),
        TestCase("x is element", (([1, 3, 5, 7, 9], 3, 5),), [3, 5, 7]),
        TestCase("between elements", (([1, 2, 4, 5], 2, 3),), [2, 4]),
    ],

    "connect_ropes": [
        TestCase("example 1", (([1, 3, 11, 5],),), 33),
        TestCase("example 2", (([3, 4, 5, 6],),), 36),
        TestCase("single rope", (([5],),), 0),
        TestCase("two ropes", (([1, 2],),), 3),
        TestCase("all same", (([4, 4, 4, 4],),), 40),
        TestCase("sorted", (([1, 2, 3, 4, 5],),), 33),
    ],

    "maximum_distinct_elements": [
        TestCase("example 1", (([7, 3, 5, 8, 5, 3, 3], 2),), 3),
        TestCase("example 2", (([3, 5, 12, 11, 12], 3),), 2),
        TestCase("no removal", (([1, 2, 3, 4], 0),), 4),
        TestCase("all same", (([5, 5, 5, 5], 3),), 1),
        TestCase("all unique", (([1, 2, 3, 4, 5], 2),), 3),
    ],

    "sum_of_elements": [
        TestCase("example 1", (([1, 3, 12, 5, 15, 11], 3, 6),), 23),
        TestCase("example 2", (([3, 5, 8, 7], 1, 4),), 12),
        TestCase("adjacent k", (([1, 2, 3, 4, 5], 2, 3),), 0),  # No elements between 2nd and 3rd smallest
    ],

    "frequency_sort": [
        TestCase("example 1", (([1, 1, 2, 2, 2, 3],),), [2, 2, 2, 1, 1, 3]),  # or [3, 1, 1, 2, 2, 2]
        TestCase("all same", (([5, 5, 5],),), [5, 5, 5]),
        TestCase("all unique", (([1, 2, 3],),), None, None),  # Any order valid
    ],

    "kth_largest_in_stream": [
        # Requires special class-based testing
    ],
}
