"""Test cases for Top K Elements problems (Category 12)."""

from . import TestCase, frequency_sort_compare, set_compare, unordered_list_compare

TOP_K_TESTS: dict[str, list[TestCase]] = {
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
        TestCase(
            "example 2",
            (([[3, 3], [5, -1], [-2, 4]], 2),),
            [[3, 3], [-2, 4]],
            unordered_list_compare,
        ),
        TestCase("origin", (([[0, 0], [1, 1]], 1),), [[0, 0]]),
        TestCase(
            "same distance", (([[1, 0], [0, 1]], 2),), [[1, 0], [0, 1]], unordered_list_compare
        ),
        TestCase("single point", (([[5, 5]], 1),), [[5, 5]]),
        TestCase(
            "negative coords",
            (([[-1, -1], [-2, -2], [1, 1]], 2),),
            [[-1, -1], [1, 1]],
            unordered_list_compare,
        ),
        TestCase(
            "all same distance", (([[1, 0], [0, 1], [-1, 0], [0, -1]], 2),), None, None
        ),  # Multiple valid
        TestCase(
            "on axes", (([[3, 0], [0, 4], [0, 0]], 2),), [[0, 0], [3, 0]], unordered_list_compare
        ),
    ],
    "sort_by_frequency": [
        TestCase("tree", (("tree",),), "tree", frequency_sort_compare),
        TestCase("cccaaa", (("cccaaa",),), "cccaaa", frequency_sort_compare),
        TestCase("Aabb", (("Aabb",),), "Aabb", frequency_sort_compare),
        TestCase("single char", (("a",),), "a"),
        TestCase("all same", (("aaaa",),), "aaaa"),
        TestCase("all unique", (("abc",),), "abc", frequency_sort_compare),
        TestCase("numbers", (("112233",),), "112233", frequency_sort_compare),
        TestCase("mixed case", (("AaBbCc",),), "AaBbCc", frequency_sort_compare),
    ],
    "closest_numbers": [
        TestCase("example 1", (([1, 2, 3, 4, 5], 4, 3),), [1, 2, 3, 4]),
        TestCase("example 2", (([1, 2, 3, 4, 5], 4, -1),), [1, 2, 3, 4]),
        TestCase("x larger than all", (([1, 2, 3, 4, 5], 4, 10),), [2, 3, 4, 5]),
        TestCase("x in middle", (([1, 2, 3, 4, 5], 3, 3),), [2, 3, 4]),
        TestCase("k equals array", (([1, 2, 3], 3, 2),), [1, 2, 3]),
        TestCase("single element", (([5], 1, 5),), [5]),
        TestCase("x is element", (([1, 3, 5, 7, 9], 3, 5),), [3, 5, 7]),
        TestCase("between elements", (([1, 2, 4, 5], 2, 3),), [2, 4]),
        TestCase("with negatives", (([-3, -1, 0, 2, 4], 3, 0),), [-1, 0, 2]),
    ],
    "connect_ropes": [
        TestCase("example 1", (([1, 3, 11, 5],),), 33),
        TestCase("example 2", (([3, 4, 5, 6],),), 36),
        TestCase("single rope", (([5],),), 0),
        TestCase("two ropes", (([1, 2],),), 3),
        TestCase("all same", (([4, 4, 4, 4],),), 32),
        TestCase("sorted", (([1, 2, 3, 4, 5],),), 33),
        TestCase("descending", (([5, 4, 3, 2, 1],),), 33),
        TestCase("three ropes", (([2, 3, 4],),), 14),  # 2+3=5 (cost 5), 5+4=9 (cost 9), total 14
        TestCase("empty", (([],),), 0),
        TestCase("large ropes", (([100, 200, 300],),), 900),
    ],
    "maximum_distinct_elements": [
        TestCase("example 1", (([7, 3, 5, 8, 5, 3, 3], 2),), 3),
        TestCase("example 2", (([3, 5, 12, 11, 12], 3),), 2),
        TestCase("no removal", (([1, 2, 3, 4], 0),), 4),
        TestCase("all same", (([5, 5, 5, 5], 3),), 1),
        TestCase("all unique", (([1, 2, 3, 4, 5], 2),), 3),
        TestCase("remove all", (([1, 2, 3], 3),), 0),
        TestCase("single element", (([5], 0),), 1),
        TestCase("k larger than duplicates", (([1, 1, 2, 2, 3], 4),), 1),
    ],
    "sum_of_elements": [
        TestCase("example 1", (([1, 3, 12, 5, 15, 11], 3, 6),), 23),
        TestCase("example 2", (([3, 5, 8, 7], 1, 4),), 12),
        TestCase(
            "adjacent k", (([1, 2, 3, 4, 5], 2, 3),), 0
        ),  # No elements between 2nd and 3rd smallest
        TestCase("with negatives", (([-5, -2, 0, 3, 7], 2, 5),), 1),  # Sum of -2, 0, 3
        TestCase("larger range", (([1, 2, 3, 4, 5, 6, 7, 8], 2, 7),), 18),  # 3+4+5+6
        TestCase("k1=1 k2=2", (([10, 20, 30], 1, 2),), 0),  # Nothing between 1st and 2nd
        TestCase("all same", (([5, 5, 5, 5], 1, 4),), 10),  # 5+5 between
        TestCase("duplicates", (([1, 1, 2, 2, 3, 3], 2, 5),), 4),  # 2+2 between
    ],
    "kth_largest_in_stream": [
        TestCase("example 1", ((3, [4, 5, 8, 2], [3, 5, 10, 9, 4]),), [4, 5, 5, 8, 8]),
        TestCase("k=1", ((1, [1, 2], [3, 4, 5]),), [3, 4, 5]),
        TestCase("single initial", ((1, [5], [1, 2, 3, 4]),), [5, 5, 5, 5]),
        TestCase("k equals size", ((3, [1, 2, 3], [4, 5]),), [2, 3]),
        TestCase("all same", ((2, [5, 5], [5, 5]),), [5, 5]),
        TestCase("with negatives", ((2, [-3, -1, 0], [1, 2]),), [0, 1]),
    ],
    "top_k_frequent_words": [
        TestCase("basic", ((["i", "love", "leetcode", "i", "love", "coding"], 2),), ["i", "love"]),
        TestCase(
            "tie by alpha",
            ((["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),),
            ["the", "is", "sunny", "day"],
        ),
        TestCase("single word", ((["hello"], 1),), ["hello"]),
        TestCase("all same freq", ((["a", "b", "c"], 2),), ["a", "b"]),
        TestCase("k equals unique", ((["apple", "banana", "apple"], 2),), ["apple", "banana"]),
        TestCase("k=1 multiple same freq", ((["a", "b", "c", "a", "b", "c"], 1),), ["a"]),
        TestCase("all duplicates", ((["word", "word", "word"], 1),), ["word"]),
    ],
}
