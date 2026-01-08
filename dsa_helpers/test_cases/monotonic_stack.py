"""Test cases for Monotonic Stack/Queue problems (Category 17)."""

from . import TestCase

MONOTONIC_STACK_TESTS: dict[str, list[TestCase]] = {
    "next_greater_element": [
        TestCase("example 1", (([4, 1, 2], [1, 3, 4, 2]),), [-1, 3, -1]),
        TestCase("example 2", (([2, 4], [1, 2, 3, 4]),), [3, -1]),
        TestCase("no greater", (([3, 2, 1], [3, 2, 1]),), [-1, -1, -1]),
        TestCase("all greater", (([1, 2, 3], [1, 2, 3, 4]),), [2, 3, 4]),
        TestCase("single element", (([1], [1, 2]),), [2]),
        TestCase("reversed", (([4, 3, 2, 1], [1, 2, 3, 4]),), [-1, 4, 3, 2]),
        TestCase("same arrays", (([1, 2, 3], [1, 2, 3]),), [2, 3, -1]),
        TestCase("nums1 equals nums2 single", (([5], [5]),), [-1]),
    ],
    "next_greater_element_ii": [
        TestCase("example 1", (([1, 2, 1],),), [2, -1, 2]),
        TestCase("example 2", (([1, 2, 3, 4, 3],),), [2, 3, 4, -1, 4]),
        TestCase("all same", (([5, 5, 5],),), [-1, -1, -1]),
        TestCase("single element", (([5],),), [-1]),
        TestCase("two elements", (([1, 2],),), [2, -1]),
        TestCase("decreasing", (([5, 4, 3, 2, 1],),), [-1, 5, 5, 5, 5]),
        TestCase("increasing", (([1, 2, 3, 4, 5],),), [2, 3, 4, 5, -1]),
        TestCase("peak in middle", (([1, 5, 3, 2, 4],),), [5, -1, 4, 4, 5]),
        TestCase("negative numbers", (([-2, -1, -3],),), [-1, -1, -2]),
        TestCase("mixed positive negative", (([-1, 2, -1],),), [2, -1, 2]),
        TestCase("large values", (([1000000000, 999999999],),), [-1, 1000000000]),
    ],
    "daily_temperatures": [
        TestCase("example 1", (([73, 74, 75, 71, 69, 72, 76, 73],),), [1, 1, 4, 2, 1, 1, 0, 0]),
        TestCase("decreasing", (([30, 29, 28, 27],),), [0, 0, 0, 0]),
        TestCase("increasing", (([30, 31, 32, 33],),), [1, 1, 1, 0]),
        TestCase("single", (([50],),), [0]),
        TestCase("all same", (([70, 70, 70],),), [0, 0, 0]),
        TestCase("one warmer", (([70, 70, 75],),), [2, 1, 0]),
        TestCase("zigzag", (([70, 80, 70, 80, 70],),), [1, 0, 1, 0, 0]),
        TestCase("valley", (([80, 70, 60, 70, 80],),), [0, 3, 1, 1, 0]),
        TestCase("two elements same", (([30, 30],),), [0, 0]),
    ],
    "largest_rectangle_histogram": [
        TestCase("example 1", (([2, 1, 5, 6, 2, 3],),), 10),
        TestCase("example 2", (([2, 4],),), 4),
        TestCase("single bar", (([5],),), 5),
        TestCase("increasing", (([1, 2, 3, 4, 5],),), 9),
        TestCase("decreasing", (([5, 4, 3, 2, 1],),), 9),
        TestCase("all same", (([3, 3, 3, 3],),), 12),
        TestCase("valley", (([5, 1, 5],),), 5),
        TestCase("peak", (([1, 5, 1],),), 5),
        TestCase("two equal", (([2, 2],),), 4),
        TestCase("empty", (([],),), 0),
    ],
    "remove_k_digits": [
        TestCase("example 1", (("1432219", 3),), "1219"),
        TestCase("example 2", (("10200", 1),), "200"),
        TestCase("example 3", (("10", 2),), "0"),
        TestCase("remove all", (("12345", 5),), "0"),
        TestCase("leading zeros", (("100200", 1),), "200"),
        TestCase("descending", (("54321", 2),), "321"),
        TestCase("ascending", (("12345", 2),), "123"),
        TestCase("single digit", (("9", 1),), "0"),
        TestCase("remove middle", (("10001", 1),), "1"),
        TestCase("all same", (("1111", 2),), "11"),
    ],
    "stock_span": [
        TestCase("example", (([100, 80, 60, 70, 60, 75, 85],),), [1, 1, 1, 2, 1, 4, 6]),
        TestCase("increasing", (([10, 20, 30, 40, 50],),), [1, 2, 3, 4, 5]),
        TestCase("decreasing", (([50, 40, 30, 20, 10],),), [1, 1, 1, 1, 1]),
        TestCase("all same", (([30, 30, 30, 30],),), [1, 2, 3, 4]),
        TestCase("single", (([100],),), [1]),
        TestCase("two increasing", (([10, 20],),), [1, 2]),
        TestCase("two decreasing", (([20, 10],),), [1, 1]),
        TestCase("valley", (([50, 30, 10, 30, 50],),), [1, 1, 1, 3, 5]),
    ],
    "sum_of_subarray_minimums": [
        TestCase("example 1", (([3, 1, 2, 4],),), 17),
        TestCase("example 2", (([11, 81, 94, 43, 3],),), 444),
        TestCase("single", (([5],),), 5),
        TestCase("two elements", (([3, 1],),), 5),  # [3]=3, [1]=1, [3,1]=1 -> 5
        TestCase("all same", (([2, 2, 2],),), 12),  # 2+2+2+2+2+2 = 12
        TestCase("increasing", (([1, 2, 3],),), 10),  # 1+2+3+1+2+1 = 10
        TestCase("decreasing", (([3, 2, 1],),), 10),  # 3+2+1+2+1+1 = 10
        TestCase("larger example", (([1, 2, 3, 4, 5],),), 35),
        TestCase(
            "with duplicates", (([1, 2, 1],),), 7
        ),  # [1]=1, [2]=2, [1]=1, [1,2]=1, [2,1]=1, [1,2,1]=1 -> 7
        TestCase("two same elements", (([1, 1],),), 3),  # [1]=1, [1]=1, [1,1]=1 -> 3
    ],
    "shortest_unsorted_subarray": [
        TestCase("example 1", (([2, 6, 4, 8, 10, 9, 15],),), 5),
        TestCase("sorted", (([1, 2, 3, 4],),), 0),
        TestCase("reverse", (([4, 3, 2, 1],),), 4),
        TestCase("single", (([1],),), 0),
        TestCase("two sorted", (([1, 2],),), 0),
        TestCase("two unsorted", (([2, 1],),), 2),
        TestCase("unsorted at start", (([3, 2, 1, 4, 5],),), 3),
        TestCase("unsorted at end", (([1, 2, 3, 5, 4],),), 2),
        TestCase("all same", (([5, 5, 5, 5],),), 0),
        TestCase("one out of place", (([1, 3, 2, 4, 5],),), 2),
        TestCase("negative numbers", (([-1, -2, -3],),), 3),
        TestCase("negative sorted", (([-3, -2, -1],),), 0),
        TestCase("duplicates unsorted", (([1, 3, 2, 2, 2],),), 4),
        TestCase("duplicates at boundary", (([1, 2, 2, 2, 1],),), 5),
    ],
    "maximal_rectangle": [
        TestCase(
            "example 1",
            (
                (
                    [
                        ["1", "0", "1", "0", "0"],
                        ["1", "0", "1", "1", "1"],
                        ["1", "1", "1", "1", "1"],
                        ["1", "0", "0", "1", "0"],
                    ],
                ),
            ),
            6,
        ),
        TestCase("empty", (([],),), 0),
        TestCase("single 1", (([["1"]],),), 1),
        TestCase("single 0", (([["0"]],),), 0),
        TestCase("row of 1s", (([["1", "1", "1"]],),), 3),
        TestCase("column of 1s", (([["1"], ["1"], ["1"]],),), 3),
        TestCase("all 1s", (([["1", "1"], ["1", "1"]],),), 4),
        TestCase("all 0s", (([["0", "0"], ["0", "0"]],),), 0),
    ],
    "StockSpanner": [
        TestCase(
            "example 1",
            (
                (
                    (),
                    ["next", "next", "next", "next", "next", "next", "next"],
                    [(100,), (80,), (60,), (70,), (60,), (75,), (85,)],
                ),
            ),
            [1, 1, 1, 2, 1, 4, 6],
            is_class_test=True,
        ),
        TestCase(
            "increasing",
            (((), ["next", "next", "next", "next", "next"], [(10,), (20,), (30,), (40,), (50,)]),),
            [1, 2, 3, 4, 5],
            is_class_test=True,
        ),
        TestCase(
            "decreasing",
            (((), ["next", "next", "next", "next", "next"], [(50,), (40,), (30,), (20,), (10,)]),),
            [1, 1, 1, 1, 1],
            is_class_test=True,
        ),
        TestCase(
            "all same",
            (((), ["next", "next", "next", "next"], [(30,), (30,), (30,), (30,)]),),
            [1, 2, 3, 4],
            is_class_test=True,
        ),
    ],
}
