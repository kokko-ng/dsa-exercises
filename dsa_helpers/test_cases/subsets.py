"""Test cases for Subsets & Permutations problems (Category 10)."""

from . import TestCase, nested_set_compare, sorted_compare

SUBSETS_TESTS = {
    "subsets": [
        TestCase(
            "basic",
            (([1, 2, 3],),),
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
            nested_set_compare,
        ),
        TestCase("single", (([0],),), [[], [0]], nested_set_compare),
        TestCase("empty", (([],),), [[]], nested_set_compare),
        TestCase("two elements", (([1, 2],),), [[], [1], [2], [1, 2]], nested_set_compare),
    ],
    "subsets_with_duplicates": [
        TestCase(
            "with dups",
            (([1, 2, 2],),),
            [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]],
            nested_set_compare,
        ),
        TestCase("all same", (([1, 1],),), [[], [1], [1, 1]], nested_set_compare),
        TestCase("no dups", (([1, 2],),), [[], [1], [2], [1, 2]], nested_set_compare),
    ],
    "permutations": [
        TestCase(
            "basic",
            (([1, 2, 3],),),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            nested_set_compare,
        ),
        TestCase("single", (([1],),), [[1]], nested_set_compare),
        TestCase("two elements", (([1, 2],),), [[1, 2], [2, 1]], nested_set_compare),
    ],
    "permutations_with_duplicates": [
        TestCase(
            "with dups", (([1, 1, 2],),), [[1, 1, 2], [1, 2, 1], [2, 1, 1]], nested_set_compare
        ),
        TestCase("all same", (([1, 1],),), [[1, 1]], nested_set_compare),
        TestCase("no dups", (([1, 2],),), [[1, 2], [2, 1]], nested_set_compare),
    ],
    "string_permutations_by_changing_case": [
        TestCase("letters", (("a1b2",),), ["a1b2", "a1B2", "A1b2", "A1B2"], nested_set_compare),
        TestCase(
            "all letters",
            (("abc",),),
            ["abc", "abC", "aBc", "aBC", "Abc", "AbC", "ABc", "ABC"],
            nested_set_compare,
        ),
        TestCase("all numbers", (("123",),), ["123"]),
        TestCase("single letter", (("a",),), ["a", "A"], nested_set_compare),
    ],
    "balanced_parentheses": [
        TestCase(
            "n=3", ((3,),), ["((()))", "(()())", "(())()", "()(())", "()()()"], nested_set_compare
        ),
        TestCase("n=1", ((1,),), ["()"]),
        TestCase("n=2", ((2,),), ["(())", "()()"], nested_set_compare),
    ],
    "unique_generalized_abbreviations": [
        TestCase(
            "word",
            (("word",),),
            [
                "word",
                "1ord",
                "w1rd",
                "wo1d",
                "wor1",
                "2rd",
                "w2d",
                "wo2",
                "1o1d",
                "1or1",
                "w1r1",
                "3d",
                "w3",
                "1o2",
                "2r1",
                "4",
            ],
            nested_set_compare,
        ),
        TestCase("single", (("a",),), ["a", "1"], nested_set_compare),
    ],
    "evaluate_expression": [
        TestCase("simple", (("2-1-1",),), [0, 2], sorted_compare),
        TestCase("multiply", (("2*3-4*5",),), [-34, -14, -10, -10, 10], sorted_compare),
        TestCase("single", (("5",),), [5]),
    ],
    "structurally_unique_bst": [
        TestCase("n=3", ((3,),), 5, lambda actual, expected: len(actual) == expected),
        TestCase("n=1", ((1,),), 1, lambda actual, expected: len(actual) == expected),
        TestCase("n=4", ((4,),), 14, lambda actual, expected: len(actual) == expected),
    ],
    "count_unique_bst": [
        TestCase("n=3", ((3,),), 5),
        TestCase("n=1", ((1,),), 1),
        TestCase("n=5", ((5,),), 42),
        TestCase("n=4", ((4,),), 14),
    ],
}
