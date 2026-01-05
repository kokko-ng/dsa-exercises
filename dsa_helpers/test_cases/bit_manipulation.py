"""Test cases for Bit Manipulation problems (Category 18)."""

from . import TestCase, sorted_compare

BIT_MANIPULATION_TESTS = {
    "single_number": [
        TestCase("basic", (([2, 2, 1],),), 1),
        TestCase("larger", (([4, 1, 2, 1, 2],),), 4),
        TestCase("single", (([1],),), 1),
        TestCase("negative", (([-1, -1, 2],),), 2),
    ],

    "single_number_ii": [
        TestCase("basic", (([2, 2, 3, 2],),), 3),
        TestCase("larger", (([0, 1, 0, 1, 0, 1, 99],),), 99),
        TestCase("single", (([5],),), 5),
        TestCase("negative", (([-2, -2, -2, 3],),), 3),
    ],

    "single_number_iii": [
        TestCase("basic", (([1, 2, 1, 3, 2, 5],),), [3, 5], sorted_compare),
        TestCase("simple", (([1, 2],),), [1, 2], sorted_compare),
        TestCase("negative", (([-1, 0],),), [-1, 0], sorted_compare),
    ],

    "counting_bits": [
        TestCase("n=2", ((2,),), [0, 1, 1]),
        TestCase("n=5", ((5,),), [0, 1, 1, 2, 1, 2]),
        TestCase("n=0", ((0,),), [0]),
        TestCase("n=1", ((1,),), [0, 1]),
    ],

    "reverse_bits": [
        TestCase("basic", ((43261596,),), 964176192),
        TestCase("all ones", ((4294967293,),), 3221225471),
        TestCase("zero", ((0,),), 0),
    ],

    "power_of_two": [
        TestCase("is power", ((1,),), True),
        TestCase("is power 16", ((16,),), True),
        TestCase("not power", ((3,),), False),
        TestCase("zero", ((0,),), False),
        TestCase("negative", ((-2,),), False),
    ],

    "bitwise_and_range": [
        TestCase("basic", ((5, 7),), 4),
        TestCase("same", ((5, 5),), 5),
        TestCase("zero result", ((0, 1),), 0),
        TestCase("larger range", ((1, 2147483647),), 0),
    ],

    "missing_number": [
        TestCase("basic", (([3, 0, 1],),), 2),
        TestCase("first missing", (([1, 2],),), 0),
        TestCase("last missing", (([0, 1],),), 2),
        TestCase("single", (([0],),), 1),
        TestCase("larger", (([9, 6, 4, 2, 3, 5, 7, 0, 1],),), 8),
    ],

    "sum_of_two_integers": [
        TestCase("positive", ((1, 2),), 3),
        TestCase("negative", ((-1, 1),), 0),
        TestCase("both negative", ((-1, -1),), -2),
        TestCase("zero", ((0, 5),), 5),
        TestCase("larger", ((100, 200),), 300),
    ],
}
