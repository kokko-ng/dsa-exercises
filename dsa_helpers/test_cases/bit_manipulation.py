"""Test cases for Bit Manipulation problems (Category 18)."""

from . import TestCase, sorted_compare

BIT_MANIPULATION_TESTS: dict[str, list[TestCase]] = {
    "single_number": [
        TestCase("basic", (([2, 2, 1],),), 1),
        TestCase("larger", (([4, 1, 2, 1, 2],),), 4),
        TestCase("single", (([1],),), 1),
        TestCase("negative", (([-1, -1, 2],),), 2),
        TestCase("zero is single", (([0, 1, 1],),), 0),
        TestCase("large numbers", (([1000000, 1000000, 999999],),), 999999),
        TestCase("negative single", (([-5, 3, 3],),), -5),
    ],
    "single_number_ii": [
        TestCase("basic", (([2, 2, 3, 2],),), 3),
        TestCase("larger", (([0, 1, 0, 1, 0, 1, 99],),), 99),
        TestCase("single", (([5],),), 5),
        TestCase("negative", (([-2, -2, -2, 3],),), 3),
        TestCase("zero is single", (([1, 1, 1, 0],),), 0),
        TestCase("negative single", (([1, 1, 1, -1],),), -1),
        TestCase("all negatives", (([-2, -2, -2, -5],),), -5),
    ],
    "single_number_iii": [
        TestCase("basic", (([1, 2, 1, 3, 2, 5],),), [3, 5], sorted_compare),
        TestCase("simple", (([1, 2],),), [1, 2], sorted_compare),
        TestCase("negative", (([-1, 0],),), [-1, 0], sorted_compare),
        TestCase("with zero", (([0, 1, 2, 2],),), [0, 1], sorted_compare),
        TestCase("large gap", (([1, 100, 1, 200, 100, 200, 5, 999],),), [5, 999], sorted_compare),
        TestCase("both negative", (([-3, -5, 1, 1],),), [-5, -3], sorted_compare),
        TestCase("zero and negative", (([0, -1, 2, 2],),), [-1, 0], sorted_compare),
    ],
    "counting_bits": [
        TestCase("n=2", ((2,),), [0, 1, 1]),
        TestCase("n=5", ((5,),), [0, 1, 1, 2, 1, 2]),
        TestCase("n=0", ((0,),), [0]),
        TestCase("n=1", ((1,),), [0, 1]),
        TestCase("n=8", ((8,),), [0, 1, 1, 2, 1, 2, 2, 3, 1]),
        TestCase("n=15", ((15,),), [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]),
    ],
    "reverse_bits": [
        TestCase("basic", ((43261596,),), 964176192),
        TestCase("all ones", ((4294967293,),), 3221225471),
        TestCase("zero", ((0,),), 0),
        TestCase("power of 2", ((1,),), 2147483648),  # 1 reversed is 10000...0 (MSB set)
        TestCase("all 32 ones", ((4294967295,),), 4294967295),  # All 1s stays all 1s
        TestCase("alternating bits", ((2863311530,),), 1431655765),  # 0xAAAAAAAA -> 0x55555555
    ],
    "power_of_two": [
        TestCase("is power", ((1,),), True),
        TestCase("is power 16", ((16,),), True),
        TestCase("not power", ((3,),), False),
        TestCase("zero", ((0,),), False),
        TestCase("negative", ((-2,),), False),
        TestCase("large power", ((1073741824,),), True),  # 2^30
        TestCase("large not power", ((1073741825,),), False),  # 2^30 + 1
        TestCase("power of 2 is 2", ((2,),), True),
        TestCase("negative power of 2", ((-16,),), False),
    ],
    "bitwise_and_range": [
        TestCase("basic", ((5, 7),), 4),
        TestCase("same", ((5, 5),), 5),
        TestCase("zero result", ((0, 1),), 0),
        TestCase("larger range", ((1, 2147483647),), 0),
        TestCase("both zero", ((0, 0),), 0),
        TestCase("consecutive", ((12, 13),), 12),
        TestCase("power of 2 range", ((8, 15),), 8),
    ],
    "missing_number": [
        TestCase("basic", (([3, 0, 1],),), 2),
        TestCase("first missing", (([1, 2],),), 0),
        TestCase("last missing", (([0, 1],),), 2),
        TestCase("single", (([0],),), 1),
        TestCase("larger", (([9, 6, 4, 2, 3, 5, 7, 0, 1],),), 8),
        TestCase("single zero missing", (([1],),), 0),
        TestCase("middle missing", (([0, 1, 3],),), 2),
    ],
    "sum_of_two_integers": [
        TestCase("positive", ((1, 2),), 3),
        TestCase("negative", ((-1, 1),), 0),
        TestCase("both negative", ((-1, -1),), -2),
        TestCase("zero", ((0, 5),), 5),
        TestCase("larger", ((100, 200),), 300),
        TestCase("both zero", ((0, 0),), 0),
        TestCase("negative and positive", ((-5, 10),), 5),
        TestCase("boundary positive", ((999, 1),), 1000),
        TestCase("negative larger magnitude", ((-10, 3),), -7),
    ],
    "number_of_1_bits": [
        TestCase("basic", ((11,),), 3),
        TestCase("power of 2", ((128,),), 1),
        TestCase("all ones", ((15,),), 4),
        TestCase("zero", ((0,),), 0),
        TestCase("large", ((2147483645,),), 30),
        TestCase("one", ((1,),), 1),
        TestCase("255", ((255,),), 8),  # 8 bits all set
    ],
}
