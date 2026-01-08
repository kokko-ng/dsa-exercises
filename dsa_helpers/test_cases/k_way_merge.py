"""Test cases for K-Way Merge problems (Category 13)."""

from . import TestCase

K_WAY_MERGE_TESTS: dict[str, list[TestCase]] = {
    "merge_k_sorted_lists": [
        TestCase("basic", (([[1, 4, 5], [1, 3, 4], [2, 6]],),), [1, 1, 2, 3, 4, 4, 5, 6]),
        TestCase("single list", (([[1, 2, 3]],),), [1, 2, 3]),
        TestCase("empty lists", (([[], [1], []],),), [1]),
        TestCase("all empty", (([],),), []),
        TestCase("single elements", (([[1], [0]],),), [0, 1]),
        TestCase("with negative numbers", (([[-5, -2, 0], [-3, 1, 4]],),), [-5, -3, -2, 0, 1, 4]),
        TestCase("list of empty lists", (([[]],),), []),
    ],
    "kth_smallest_in_m_sorted": [
        TestCase("basic", (([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5),), 4),
        TestCase("first", (([[1, 2], [3, 4]], 1),), 1),
        TestCase("last", (([[1, 2], [3, 4]], 4),), 4),
        TestCase("single list", (([[1, 2, 3, 4, 5]], 3),), 3),
        TestCase("with duplicates", (([[1, 1, 2], [1, 2, 3]], 3),), 1),
        TestCase("negative numbers", (([[-5, -3, 0], [-4, -2, 1]], 2),), -4),
    ],
    "smallest_number_range": [
        TestCase("basic", (([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],),), [20, 24]),
        TestCase("single element lists", (([[1], [2], [3]],),), [1, 3]),
        TestCase("overlapping", (([[1, 5, 8], [4, 12], [7, 8, 10]],),), [4, 7]),
        TestCase("same elements", (([[1, 2, 3], [1, 2, 3], [1, 2, 3]],),), [1, 1]),
        TestCase("negative range", (([[-5, -3, 0], [-4, -2, 1], [-6, -1, 2]],),), [-3, -1]),
    ],
    "kth_smallest_in_matrix": [
        TestCase("basic", (([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),), 13),
        TestCase("first", (([[1, 2], [1, 3]], 1),), 1),
        TestCase("single", (([[5]], 1),), 5),
        TestCase("2x2", (([[1, 2], [3, 4]], 3),), 3),
        TestCase("negative numbers", (([[-5]], 1),), -5),
        TestCase("last element", (([[1, 2], [3, 4]], 4),), 4),
        TestCase("with duplicates", (([[1, 2, 2], [2, 3, 3], [3, 3, 4]], 7),), 3),
    ],
    "find_k_pairs_smallest_sums": [
        TestCase("basic", (([1, 7, 11], [2, 4, 6], 3),), [[1, 2], [1, 4], [1, 6]]),
        TestCase("same elements", (([1, 1, 2], [1, 2, 3], 2),), [[1, 1], [1, 1]]),
        TestCase("k=1", (([1, 2], [3], 1),), [[1, 3]]),
        TestCase("negative numbers", (([-2, -1, 0], [-3, 1, 2], 2),), [[-2, -3], [-1, -3]]),
        TestCase("k larger than pairs", (([1], [2], 5),), [[1, 2]]),
        TestCase("single element arrays", (([1], [1], 1),), [[1, 1]]),
    ],
    "merge_k_sorted_arrays": [
        TestCase("basic", (([[1, 4, 5], [1, 3, 4], [2, 6]],),), [1, 1, 2, 3, 4, 4, 5, 6]),
        TestCase("single", (([[1, 2, 3]],),), [1, 2, 3]),
        TestCase("with empties", (([[], [1, 2], []],),), [1, 2]),
        TestCase("negative numbers", (([[-3, -1, 0], [-2, 1]],),), [-3, -2, -1, 0, 1]),
        TestCase("all empty", (([[], []],),), []),
    ],
    "kth_smallest_in_row_col_sorted": [
        TestCase("basic", (([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),), 13),
        TestCase("corner", (([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9),), 9),
        TestCase("first", (([[1]], 1),), 1),
        TestCase("single row", (([[1, 2, 3, 4, 5]], 3),), 3),
        TestCase("single column", (([[1], [2], [3], [4]], 2),), 2),
        TestCase("rectangular", (([[1, 2, 3], [4, 5, 6]], 5),), 5),
        TestCase("negative numbers", (([[-10, -5, 0], [-3, 2, 5], [1, 4, 8]], 4),), -3),
        TestCase("with duplicates", (([[1, 2, 2], [2, 3, 3], [3, 4, 5]], 5),), 3),
    ],
    "median_of_sorted_arrays": [
        TestCase("basic", (([1, 3], [2]),), 2.0),
        TestCase("even total", (([1, 2], [3, 4]),), 2.5),
        TestCase("one empty", (([], [1]),), 1.0),
        TestCase("one element each", (([1], [2]),), 1.5),
        TestCase("larger", (([1, 2, 3], [4, 5, 6]),), 3.5),
        TestCase("negative numbers", (([-3, -1, 0], [-2, 1, 2]),), -0.5),
        TestCase("both empty with one", (([], [2]),), 2.0),
        TestCase("different sizes", (([1, 2], [3, 4, 5, 6]),), 3.5),
    ],
}
