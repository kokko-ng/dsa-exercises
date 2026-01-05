"""Test cases for Cyclic Sort problems (Category 06)."""

from . import TestCase, sorted_compare, set_compare


CYCLIC_SORT_TESTS = {
    "cyclic_sort": [
        TestCase("unsorted", (([3, 1, 5, 4, 2],),), [1, 2, 3, 4, 5]),
        TestCase("reverse", (([5, 4, 3, 2, 1],),), [1, 2, 3, 4, 5]),
        TestCase("sorted", (([1, 2, 3, 4, 5],),), [1, 2, 3, 4, 5]),
        TestCase("single", (([1],),), [1]),
        TestCase("two elements", (([2, 1],),), [1, 2]),
        TestCase("random order", (([2, 4, 1, 3],),), [1, 2, 3, 4]),
        TestCase("first last swapped", (([5, 2, 3, 4, 1],),), [1, 2, 3, 4, 5]),
        TestCase("large", ((list(range(100, 0, -1)),),), list(range(1, 101))),
    ],

    "find_missing_number": [
        TestCase("missing 2", (([4, 0, 3, 1],),), 2),
        TestCase("missing 8", (([0, 1, 2, 3, 4, 5, 6, 7, 9],),), 8),
        TestCase("missing 0", (([1, 2, 3],),), 0),
        TestCase("missing last", (([0, 1, 2],),), 3),
        TestCase("single missing", (([0],),), 1),
        TestCase("missing first", (([1],),), 0),
        TestCase("missing middle", (([0, 1, 3, 4, 5],),), 2),
        TestCase("larger array", (([0, 1, 2, 3, 4, 5, 6, 8, 9, 10],),), 7),
        TestCase("two elements", (([1, 0],),), 2),
    ],

    "find_all_missing_numbers": [
        TestCase("example 1", (([4, 3, 2, 7, 8, 2, 3, 1],),), [5, 6], sorted_compare),
        TestCase("example 2", (([1, 1],),), [2]),
        TestCase("no missing", (([1, 2, 3],),), []),
        TestCase("all missing", (([2, 2, 2],),), [1, 3], sorted_compare),
        TestCase("single element", (([1],),), []),
        TestCase("first missing", (([2, 3, 4],),), [1], sorted_compare),
        TestCase("last missing", (([1, 2, 1],),), [3]),
        TestCase("multiple dups", (([1, 1, 1, 1],),), [2, 3, 4], sorted_compare),
    ],

    "find_duplicate": [
        TestCase("example 1", (([1, 3, 4, 2, 2],),), 2),
        TestCase("example 2", (([3, 1, 3, 4, 2],),), 3),
        TestCase("at start", (([2, 2, 2, 2, 2],),), 2),
        TestCase("two elements", (([1, 1],),), 1),
        TestCase("at end", (([1, 2, 3, 4, 4],),), 4),
        TestCase("in middle", (([1, 4, 4, 2, 4],),), 4),
        TestCase("first element", (([1, 1, 2, 3, 4],),), 1),
        TestCase("larger", (([1, 2, 3, 4, 5, 5, 6, 7],),), 5),
    ],

    "find_all_duplicates": [
        TestCase("example", (([4, 3, 2, 7, 8, 2, 3, 1],),), [2, 3], set_compare),
        TestCase("no dups", (([1, 2, 3],),), []),
        TestCase("all dups", (([1, 1, 2, 2],),), [1, 2], set_compare),
        TestCase("single dup", (([1, 1],),), [1]),
        TestCase("multiple of same", (([1, 1, 1, 1],),), [1]),
        TestCase("two pairs", (([1, 2, 1, 2],),), [1, 2], set_compare),
        TestCase("scattered", (([3, 1, 2, 5, 3, 2],),), [2, 3], set_compare),
        TestCase("at boundaries", (([1, 2, 3, 4, 1, 4],),), [1, 4], set_compare),
    ],

    "find_corrupt_pair": [
        TestCase("example 1", (([3, 1, 2, 5, 2],),), [2, 4], sorted_compare),
        TestCase("example 2", (([3, 1, 2, 3, 6, 4],),), [3, 5], sorted_compare),
        TestCase("at start", (([1, 1, 3, 4, 5],),), [1, 2], sorted_compare),
        TestCase("at end", (([1, 2, 3, 4, 4],),), [4, 5], sorted_compare),
        TestCase("two elements", (([2, 2],),), [1, 2], sorted_compare),
        TestCase("adjacent", (([1, 2, 3, 3, 5],),), [3, 4], sorted_compare),
        TestCase("far apart", (([1, 2, 1, 4, 5],),), [1, 3], sorted_compare),
    ],

    "first_missing_positive": [
        TestCase("example 1", (([1, 2, 0],),), 3),
        TestCase("example 2", (([3, 4, -1, 1],),), 2),
        TestCase("example 3", (([7, 8, 9, 11, 12],),), 1),
        TestCase("consecutive", (([1, 2, 3],),), 4),
        TestCase("single negative", (([-1],),), 1),
        TestCase("single positive", (([1],),), 2),
        TestCase("with zeros", (([0, 0, 0],),), 1),
        TestCase("large gap", (([1, 1000],),), 2),
        TestCase("all negatives", (([-1, -2, -3],),), 1),
        TestCase("unsorted complete", (([3, 2, 1, 5, 4],),), 6),
    ],

    "first_k_missing_positive": [
        TestCase("example 1", (([3, -1, 4, 5, 5], 3),), [1, 2, 6]),
        TestCase("example 2", (([2, 3, 4], 3),), [1, 5, 6]),
        TestCase("example 3", (([-2, -3, 4], 2),), [1, 2]),
        TestCase("all missing", (([5, 6, 7], 3),), [1, 2, 3]),
        TestCase("none missing initially", (([1, 2, 3], 2),), [4, 5]),
        TestCase("with duplicates", (([1, 1, 1, 1], 3),), [2, 3, 4]),
    ],
}
