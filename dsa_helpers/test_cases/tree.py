"""Test cases for Tree BFS & DFS problems (Category 08)."""

from . import TestCase

TREE_TESTS = {
    "level_order_traversal": [
        TestCase("complete tree", (([3, 9, 20, None, None, 15, 7],),), [[3], [9, 20], [15, 7]]),
        TestCase("single node", (([1],),), [[1]]),
        TestCase("empty", (([],),), []),
        TestCase("left skewed", (([1, 2, None, 3],),), [[1], [2], [3]]),
        TestCase("right skewed", (([1, None, 2, None, 3],),), [[1], [2], [3]]),
    ],

    "reverse_level_order": [
        TestCase("complete tree", (([3, 9, 20, None, None, 15, 7],),), [[15, 7], [9, 20], [3]]),
        TestCase("single node", (([1],),), [[1]]),
        TestCase("empty", (([],),), []),
    ],

    "zigzag_level_order": [
        TestCase("complete tree", (([3, 9, 20, None, None, 15, 7],),), [[3], [20, 9], [15, 7]]),
        TestCase("single node", (([1],),), [[1]]),
        TestCase("empty", (([],),), []),
        TestCase("two levels", (([1, 2, 3],),), [[1], [3, 2]]),
    ],

    "average_of_levels": [
        TestCase("complete tree", (([3, 9, 20, None, None, 15, 7],),), [3.0, 14.5, 11.0]),
        TestCase("single node", (([1],),), [1.0]),
        TestCase("two levels", (([3, 9, 20],),), [3.0, 14.5]),
    ],

    "minimum_depth": [
        TestCase("balanced", (([3, 9, 20, None, None, 15, 7],),), 2),
        TestCase("left skewed", (([2, None, 3, None, 4, None, 5, None, 6],),), 5),
        TestCase("single node", (([1],),), 1),
        TestCase("empty", (([],),), 0),
    ],

    "maximum_depth": [
        TestCase("balanced", (([3, 9, 20, None, None, 15, 7],),), 3),
        TestCase("single node", (([1],),), 1),
        TestCase("empty", (([],),), 0),
        TestCase("left skewed", (([1, 2, None, 3],),), 3),
    ],

    "level_order_successor": [
        TestCase("in same level", (([3, 9, 20, None, None, 15, 7], 9),), 20),
        TestCase("next level", (([3, 9, 20, None, None, 15, 7], 20),), 15),
        TestCase("last node", (([3, 9, 20, None, None, 15, 7], 7),), None),
        TestCase("root", (([1, 2, 3], 1),), 2),
    ],

    "connect_level_order_siblings": [
        TestCase("complete tree", (([1, 2, 3, 4, 5, 6, 7],),), [[1, None], [2, 3, None], [4, 5, 6, 7, None]]),
        TestCase("single node", (([1],),), [[1, None]]),
    ],

    "path_sum": [
        TestCase("has path", (([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22),), True),
        TestCase("no path", (([1, 2, 3], 5),), False),
        TestCase("single node true", (([1], 1),), True),
        TestCase("single node false", (([1], 2),), False),
        TestCase("empty", (([], 0),), False),
    ],

    "all_paths_for_sum": [
        TestCase("two paths", (([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22),), [[5, 4, 11, 2], [5, 8, 4, 5]]),
        TestCase("single path", (([1, 2, 3], 4),), [[1, 3]]),
        TestCase("no path", (([1, 2, 3], 10),), []),
    ],

    "sum_of_path_numbers": [
        TestCase("simple", (([1, 2, 3],),), 25),
        TestCase("single", (([1],),), 1),
        TestCase("larger", (([4, 9, 0, 5, 1],),), 1026),
    ],

    "path_with_given_sequence": [
        TestCase("exists", (([1, 7, 9, None, None, 2, 9], [1, 9, 9]),), True),
        TestCase("not exists", (([1, 0, 1, 1, 0, 0, 1], [1, 1, 0]),), False),
        TestCase("single", (([1], [1]),), True),
    ],

    "count_paths_for_sum": [
        TestCase("multiple paths", (([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8),), 3),
        TestCase("simple", (([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22),), 3),
        TestCase("single node", (([1], 1),), 1),
    ],

    "tree_diameter": [
        TestCase("balanced", (([1, 2, 3, 4, 5],),), 3),
        TestCase("skewed", (([1, 2, None, 3, None, 4],),), 3),
        TestCase("single", (([1],),), 0),
        TestCase("empty", (([],),), 0),
    ],

    "path_with_maximum_sum": [
        TestCase("mixed", (([-10, 9, 20, None, None, 15, 7],),), 42),
        TestCase("negative", (([-3],),), -3),
        TestCase("simple", (([1, 2, 3],),), 6),
        TestCase("single path", (([2, -1],),), 2),
    ],
}
