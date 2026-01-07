"""Test cases for Merge Intervals problems (Category 05)."""

from . import TestCase

MERGE_INTERVALS_TESTS: dict[str, list[TestCase]] = {
    "merge_intervals": [
        TestCase(
            "overlapping", (([[1, 3], [2, 6], [8, 10], [15, 18]],),), [[1, 6], [8, 10], [15, 18]]
        ),
        TestCase("touching", (([[1, 4], [4, 5]],),), [[1, 5]]),
        TestCase("single", (([[1, 4]],),), [[1, 4]]),
        TestCase("no overlap", (([[1, 2], [3, 4], [5, 6]],),), [[1, 2], [3, 4], [5, 6]]),
        TestCase("all overlap", (([[1, 10], [2, 6], [3, 5], [7, 9]],),), [[1, 10]]),
        TestCase("unsorted input", (([[3, 5], [1, 4]],),), [[1, 5]]),
        TestCase("nested intervals", (([[1, 10], [2, 3], [4, 5], [6, 7]],),), [[1, 10]]),
        TestCase("identical intervals", (([[1, 3], [1, 3], [1, 3]],),), [[1, 3]]),
        TestCase("chain merge", (([[1, 2], [2, 3], [3, 4], [4, 5]],),), [[1, 5]]),
        TestCase("empty", (([],),), []),
        TestCase("large gap", (([[1, 2], [100, 200]],),), [[1, 2], [100, 200]]),
    ],
    "insert_interval": [
        TestCase("middle insert", (([[1, 3], [6, 9]], [2, 5]),), [[1, 5], [6, 9]]),
        TestCase(
            "merge multiple",
            (([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),),
            [[1, 2], [3, 10], [12, 16]],
        ),
        TestCase("no overlap", (([[1, 2], [5, 6]], [3, 4]),), [[1, 2], [3, 4], [5, 6]]),
        TestCase("merge all", (([[1, 3], [4, 6], [7, 9]], [2, 8]),), [[1, 9]]),
        TestCase("at start", (([[3, 5], [6, 8]], [1, 2]),), [[1, 2], [3, 5], [6, 8]]),
        TestCase("at end", (([[1, 2], [3, 4]], [5, 6]),), [[1, 2], [3, 4], [5, 6]]),
        TestCase("empty intervals", (([], [1, 3]),), [[1, 3]]),
        TestCase("cover first", (([[2, 3], [5, 6]], [1, 4]),), [[1, 4], [5, 6]]),
        TestCase("cover last", (([[1, 2], [3, 4]], [3, 6]),), [[1, 2], [3, 6]]),
        TestCase("contained", (([[1, 5]], [2, 3]),), [[1, 5]]),
    ],
    "intervals_intersection": [
        TestCase(
            "example",
            (([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]),),
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        ),
        TestCase("no intersection", (([[1, 2], [5, 6]], [[3, 4], [7, 8]]),), []),
        TestCase("full overlap", (([[1, 10]], [[1, 10]]),), [[1, 10]]),
        TestCase("one empty", (([], [[1, 2]]),), []),
        TestCase("nested", (([[1, 10]], [[2, 3], [5, 6]]),), [[2, 3], [5, 6]]),
        TestCase("touching", (([[1, 3], [5, 7]], [[3, 5]]),), [[3, 3], [5, 5]]),
        TestCase("partial overlap", (([[1, 5], [10, 15]], [[3, 12]]),), [[3, 5], [10, 12]]),
        TestCase("single point", (([[1, 1]], [[1, 1]]),), [[1, 1]]),
    ],
    "meeting_rooms": [
        TestCase("overlapping", (([[0, 30], [5, 10], [15, 20]],),), False),
        TestCase("no overlap", (([[7, 10], [2, 4]],),), True),
        TestCase("touching", (([[1, 2], [2, 3]],),), True),
        TestCase("single meeting", (([[1, 5]],),), True),
        TestCase("empty", (([],),), True),
        TestCase("nested", (([[1, 10], [2, 5]],),), False),
        TestCase("chain", (([[1, 2], [2, 3], [3, 4]],),), True),
        TestCase("gap", (([[1, 2], [5, 6]],),), True),
    ],
    "meeting_rooms_ii": [
        TestCase("example 1", (([[0, 30], [5, 10], [15, 20]],),), 2),
        TestCase("example 2", (([[7, 10], [2, 4]],),), 1),
        TestCase("all overlap", (([[1, 10], [2, 9], [3, 8]],),), 3),
        TestCase("no overlap", (([[1, 2], [3, 4], [5, 6]],),), 1),
        TestCase("touching", (([[1, 2], [2, 3], [3, 4]],),), 1),
        TestCase("empty", (([],),), 0),
        TestCase("same time", (([[1, 5], [1, 5], [1, 5]],),), 3),
        TestCase("cascading", (([[0, 5], [1, 6], [2, 7], [3, 8]],),), 4),
        TestCase("single", (([[1, 10]],),), 1),
    ],
    "non_overlapping_intervals": [
        TestCase("example 1", (([[1, 2], [2, 3], [3, 4], [1, 3]],),), 1),
        TestCase("example 2", (([[1, 2], [1, 2], [1, 2]],),), 2),
        TestCase("no removal", (([[1, 2], [3, 4]],),), 0),
        TestCase("all overlap", (([[1, 4], [2, 3], [3, 5]],),), 1),
        TestCase("empty", (([],),), 0),
        TestCase("single", (([[1, 2]],),), 0),
        TestCase("nested", (([[1, 10], [2, 3], [4, 5]],),), 1),
        TestCase("chain remove", (([[1, 3], [2, 4], [3, 5], [4, 6]],),), 2),
    ],
    "employee_free_time": [
        TestCase("example 1", (([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]],),), [[3, 4]]),
        TestCase(
            "example 2", (([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]],),), [[5, 6], [7, 9]]
        ),
        TestCase("no free time", (([[[1, 10]], [[1, 10]]],),), []),
        TestCase("single employee", (([[[1, 2], [5, 6]]],),), [[2, 5]]),
        TestCase("consecutive", (([[[1, 2]], [[2, 3]], [[3, 4]]],),), []),
    ],
    "car_pooling": [
        TestCase("example 1", (([[2, 1, 5], [3, 3, 7]], 4),), False),
        TestCase("example 2", (([[2, 1, 5], [3, 3, 7]], 5),), True),
        TestCase("single trip", (([[2, 1, 5]], 2),), True),
        TestCase("over capacity", (([[5, 1, 5]], 4),), False),
        TestCase("no overlap", (([[2, 1, 5], [3, 6, 8]], 4),), True),
        TestCase("same location", (([[3, 1, 5], [2, 1, 5]], 5),), True),
    ],
    "interval_list_intersections": [
        TestCase(
            "basic",
            (([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]),),
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        ),
        TestCase("no intersection", (([[1, 2]], [[3, 4]]),), []),
        TestCase("full overlap", (([[1, 5]], [[1, 5]]),), [[1, 5]]),
        TestCase("one empty", (([], [[1, 2]]),), []),
    ],
    "minimum_platforms": [
        TestCase(
            "basic", (([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]),), 3
        ),
        TestCase("no overlap", (([900, 1100], [930, 1130]),), 1),
        TestCase("all overlap", (([900, 900, 900], [1000, 1000, 1000]),), 3),
        TestCase("single train", (([900], [910]),), 1),
    ],
}
