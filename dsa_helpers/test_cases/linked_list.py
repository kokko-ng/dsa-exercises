"""Test cases for Linked List Reversal problems (Category 07)."""

from . import TestCase

LINKED_LIST_TESTS: dict[str, list[TestCase]] = {
    "reverse_linked_list": [
        TestCase("simple", (([1, 2, 3, 4, 5],),), [5, 4, 3, 2, 1]),
        TestCase("two nodes", (([1, 2],),), [2, 1]),
        TestCase("single node", (([1],),), [1]),
        TestCase("empty", (([],),), []),
        TestCase("three nodes", (([1, 2, 3],),), [3, 2, 1]),
        TestCase("negative values", (([-1, -2, 0, 3],),), [3, 0, -2, -1]),
        TestCase("duplicates", (([1, 1, 2, 2],),), [2, 2, 1, 1]),
    ],
    "reverse_linked_list_ii": [
        TestCase("middle", (([1, 2, 3, 4, 5], 2, 4),), [1, 4, 3, 2, 5]),
        TestCase("whole list", (([1, 2, 3], 1, 3),), [3, 2, 1]),
        TestCase("two elements", (([1, 2, 3, 4, 5], 3, 4),), [1, 2, 4, 3, 5]),
        TestCase("single element", (([5], 1, 1),), [5]),
        TestCase("first two", (([1, 2, 3], 1, 2),), [2, 1, 3]),
        TestCase("left equals right", (([1, 2, 3, 4, 5], 3, 3),), [1, 2, 3, 4, 5]),
        TestCase("negative values", (([-5, -4, -3, -2, -1], 2, 4),), [-5, -2, -3, -4, -1]),
    ],
    "reverse_k_group": [
        TestCase("k=2", (([1, 2, 3, 4, 5], 2),), [2, 1, 4, 3, 5]),
        TestCase("k=3", (([1, 2, 3, 4, 5], 3),), [3, 2, 1, 4, 5]),
        TestCase("k=1", (([1, 2, 3], 1),), [1, 2, 3]),
        TestCase("k=len", (([1, 2, 3], 3),), [3, 2, 1]),
        TestCase("single", (([1], 1),), [1]),
        TestCase("negative values", (([-3, -2, -1, 0, 1, 2], 2),), [-2, -3, 0, -1, 2, 1]),
        TestCase("remainder nodes", (([1, 2, 3, 4, 5, 6, 7], 3),), [3, 2, 1, 6, 5, 4, 7]),
        TestCase("duplicates", (([1, 1, 2, 2, 3, 3], 2),), [1, 1, 2, 2, 3, 3]),
    ],
    "reverse_alternating_k": [
        TestCase("k=2", (([1, 2, 3, 4, 5, 6, 7, 8], 2),), [2, 1, 3, 4, 6, 5, 7, 8]),
        TestCase("k=3", (([1, 2, 3, 4, 5, 6], 3),), [3, 2, 1, 4, 5, 6]),
        TestCase("short list", (([1, 2], 2),), [2, 1]),
        TestCase("k=1", (([1, 2, 3], 1),), [1, 2, 3]),
        TestCase("single node", (([1], 1),), [1]),
        TestCase("negative values", (([-4, -3, -2, -1], 2),), [-3, -4, -2, -1]),
        TestCase(
            "nine elements k=3", (([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),), [3, 2, 1, 4, 5, 6, 9, 8, 7]
        ),
    ],
    "rotate_list": [
        TestCase("rotate by 2", (([1, 2, 3, 4, 5], 2),), [4, 5, 1, 2, 3]),
        TestCase("rotate by 4", (([0, 1, 2], 4),), [2, 0, 1]),
        TestCase("single node", (([1], 1),), [1]),
        TestCase("k=0", (([1, 2, 3], 0),), [1, 2, 3]),
        TestCase("k > len", (([1, 2], 3),), [2, 1]),
        TestCase("empty", (([], 0),), []),
        TestCase("k equals len", (([1, 2, 3], 3),), [1, 2, 3]),
        TestCase("large k", (([1, 2, 3, 4], 10),), [3, 4, 1, 2]),
        TestCase("negative values", (([-3, -2, -1], 1),), [-1, -3, -2]),
    ],
    "swap_pairs": [
        TestCase("even length", (([1, 2, 3, 4],),), [2, 1, 4, 3]),
        TestCase("odd length", (([1, 2, 3],),), [2, 1, 3]),
        TestCase("single", (([1],),), [1]),
        TestCase("empty", (([],),), []),
        TestCase("two nodes", (([1, 2],),), [2, 1]),
        TestCase("six nodes", (([1, 2, 3, 4, 5, 6],),), [2, 1, 4, 3, 6, 5]),
        TestCase("negative values", (([-2, -1, 0, 1],),), [-1, -2, 1, 0]),
    ],
    "reverse_between": [
        TestCase("middle", (([1, 2, 3, 4, 5], 2, 4),), [1, 4, 3, 2, 5]),
        TestCase("from start", (([1, 2, 3, 4], 1, 3),), [3, 2, 1, 4]),
        TestCase("to end", (([1, 2, 3, 4], 2, 4),), [1, 4, 3, 2]),
        TestCase("single", (([1], 1, 1),), [1]),
        TestCase("full reverse", (([1, 2, 3, 4, 5], 1, 5),), [5, 4, 3, 2, 1]),
        TestCase("two nodes reverse both", (([1, 2], 1, 2),), [2, 1]),
        TestCase("negative values", (([-3, -2, -1, 0], 2, 3),), [-3, -1, -2, 0]),
    ],
    "odd_even_linked_list": [
        TestCase("mixed", (([1, 2, 3, 4, 5],),), [1, 3, 5, 2, 4]),
        TestCase("even length", (([2, 1, 3, 5, 6, 4, 7],),), [2, 3, 6, 7, 1, 5, 4]),
        TestCase("two nodes", (([1, 2],),), [1, 2]),
        TestCase("single", (([1],),), [1]),
        TestCase("empty", (([],),), []),
        TestCase("three nodes", (([1, 2, 3],),), [1, 3, 2]),
        TestCase("negative values", (([-2, -1, 0, 1, 2],),), [-2, 0, 2, -1, 1]),
    ],
    "split_linked_list": [
        TestCase("split 5 into 3", (([1, 2, 3, 4, 5], 3),), [[1, 2], [3, 4], [5]]),
        TestCase("split 3 into 5", (([1, 2, 3], 5),), [[1], [2], [3], [], []]),
        TestCase("even split", (([1, 2, 3, 4], 2),), [[1, 2], [3, 4]]),
        TestCase("single", (([1], 1),), [[1]]),
        TestCase("empty list", (([], 3),), [[], [], []]),
        TestCase("k=1", (([1, 2, 3, 4, 5], 1),), [[1, 2, 3, 4, 5]]),
        TestCase(
            "10 into 3",
            (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),),
            [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]],
        ),
        TestCase("negative values", (([-3, -2, -1, 0], 2),), [[-3, -2], [-1, 0]]),
        TestCase("single into multiple", (([5], 3),), [[5], [], []]),
    ],
    "flatten_multilevel_list": [
        TestCase(
            "with child",
            (({"list": [1, 2, 3, 4, 5, 6], "child_at": 2, "child": [7, 8, 9]},),),
            [1, 2, 3, 7, 8, 9, 4, 5, 6],
        ),
        TestCase("no child", (({"list": [1, 2, 3], "child_at": -1, "child": []},),), [1, 2, 3]),
        TestCase("single", (({"list": [1], "child_at": -1, "child": []},),), [1]),
        TestCase("empty", (({"list": [], "child_at": -1, "child": []},),), []),
        TestCase(
            "child at start",
            (({"list": [1, 2, 3], "child_at": 0, "child": [4, 5]},),),
            [1, 4, 5, 2, 3],
        ),
        TestCase(
            "nested child",
            (
                (
                    {
                        "list": [1, 2, 3],
                        "child_at": 0,
                        "child": [4, 5],
                        "nested_child_at": 0,
                        "nested_child": [6, 7],
                    },
                ),
            ),
            [1, 4, 6, 7, 5, 2, 3],
        ),
        TestCase(
            "child at end",
            (({"list": [1, 2, 3], "child_at": 2, "child": [4, 5]},),),
            [1, 2, 3, 4, 5],
        ),
    ],
}
