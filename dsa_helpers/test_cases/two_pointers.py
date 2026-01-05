"""Test cases for Two Pointers & Sliding Window problems (Category 03)."""

from . import TestCase, sorted_compare, set_compare, nested_set_compare

TWO_POINTERS_TESTS = {
    "remove_element": [
        TestCase("remove 3s", (([3, 2, 2, 3], 3),), 2),
        TestCase("remove 2s", (([0, 1, 2, 2, 3, 0, 4, 2], 2),), 5),
        TestCase("empty array", (([], 1),), 0),
        TestCase("no matches", (([1, 2, 3], 4),), 3),
        TestCase("all matches", (([2, 2, 2], 2),), 0),
        TestCase("single element match", (([1], 1),), 0),
        TestCase("single element no match", (([1], 2),), 1),
        TestCase("alternating", (([1, 2, 1, 2, 1], 1),), 2),
    ],

    "squares_of_sorted_array": [
        TestCase("mixed signs", (([-4, -1, 0, 3, 10],),), [0, 1, 9, 16, 100]),
        TestCase("all negative", (([-7, -3, -1],),), [1, 9, 49]),
        TestCase("all positive", (([1, 2, 3],),), [1, 4, 9]),
        TestCase("single element", (([-5],),), [25]),
        TestCase("two elements", (([-3, 2],),), [4, 9]),
        TestCase("zeros", (([-2, 0, 2],),), [0, 4, 4]),
        TestCase("larger array", (([-5, -3, -2, -1],),), [1, 4, 9, 25]),
        TestCase("symmetric", (([-3, -1, 0, 1, 3],),), [0, 1, 1, 9, 9]),
    ],

    "three_sum": [
        TestCase("example 1", (([-1, 0, 1, 2, -1, -4],),), [[-1, -1, 2], [-1, 0, 1]], nested_set_compare),
        TestCase("no solution", (([0, 1, 1],),), [], nested_set_compare),
        TestCase("all zeros", (([0, 0, 0],),), [[0, 0, 0]], nested_set_compare),
        TestCase("two elements", (([1, -1],),), [], nested_set_compare),
        TestCase("duplicates", (([1, 1, -2],),), [[-2, 1, 1]], nested_set_compare),
        TestCase("multiple solutions", (([-2, 0, 1, 1, 2],),), [[-2, 0, 2], [-2, 1, 1]], nested_set_compare),
        TestCase("negative heavy", (([-4, -2, -1, 0, 1, 2],),), [[-2, 0, 2], [-1, 0, 1]], nested_set_compare),
        TestCase("empty", (([],),), [], nested_set_compare),
    ],

    "three_sum_closest": [
        TestCase("example 1", (([-1, 2, 1, -4], 1),), 2),
        TestCase("all zeros", (([0, 0, 0], 1),), 0),
        TestCase("exact match", (([1, 1, 1], 3),), 3),
        TestCase("negative target", (([-3, -1, 1, 2], -3),), -3),
        TestCase("large difference", (([1, 2, 3], 100),), 6),
        TestCase("negative result", (([-5, -4, -3], 0),), -12),
        TestCase("mixed", (([1, 2, 4, 8, 16], 15),), 14),
        TestCase("duplicates", (([1, 1, 1, 1], 0),), 3),
    ],

    "sort_colors": [
        TestCase("mixed", (([2, 0, 2, 1, 1, 0],),), [0, 0, 1, 1, 2, 2], check_modified_arg=0),
        TestCase("simple", (([2, 0, 1],),), [0, 1, 2], check_modified_arg=0),
        TestCase("already sorted", (([0, 1, 2],),), [0, 1, 2], check_modified_arg=0),
        TestCase("reverse sorted", (([2, 1, 0],),), [0, 1, 2], check_modified_arg=0),
        TestCase("all same 0", (([0, 0, 0],),), [0, 0, 0], check_modified_arg=0),
        TestCase("all same 1", (([1, 1, 1],),), [1, 1, 1], check_modified_arg=0),
        TestCase("all same 2", (([2, 2, 2],),), [2, 2, 2], check_modified_arg=0),
        TestCase("two colors", (([1, 0, 1, 0],),), [0, 0, 1, 1], check_modified_arg=0),
        TestCase("single element", (([1],),), [1], check_modified_arg=0),
    ],

    "backspace_string_compare": [
        TestCase("equal after backspace", (("ab#c", "ad#c"),), True),
        TestCase("both empty", (("ab##", "c#d#"),), True),
        TestCase("different", (("a#c", "b"),), False),
        TestCase("no backspace", (("abc", "abc"),), True),
        TestCase("multiple backspace", (("a###b", "b"),), True),
        TestCase("backspace at start", (("#a#b", "b"),), True),
        TestCase("empty result", (("####", ""),), True),
        TestCase("single chars", (("a", "a"),), True),
        TestCase("single char diff", (("a", "b"),), False),
        TestCase("complex", (("bxj##tw", "bxo#j##tw"),), True),
    ],

    "maximum_average_subarray": [
        TestCase("example 1", (([1, 12, -5, -6, 50, 3], 4),), 12.75),
        TestCase("single element", (([5], 1),), 5.0),
        TestCase("whole array", (([1, 2, 3], 3),), 2.0),
        TestCase("negative numbers", (([-1, -2, -3], 2),), -1.5),
        TestCase("mixed", (([4, 0, 4, 3, 3], 5),), 2.8),
        TestCase("k equals 1", (([1, 2, 3, 4, 5], 1),), 5.0),
        TestCase("all same", (([5, 5, 5, 5], 2),), 5.0),
        TestCase("large k", (([0, 1, 1, 3, 3], 4),), 2.0),
    ],

    "minimum_size_subarray_sum": [
        TestCase("example 1", ((7, [2, 3, 1, 2, 4, 3]),), 2),
        TestCase("single element enough", ((4, [1, 4, 4]),), 1),
        TestCase("no solution", ((11, [1, 1, 1, 1, 1, 1, 1, 1]),), 0),
        TestCase("whole array", ((15, [1, 2, 3, 4, 5]),), 5),
        TestCase("first element", ((5, [5, 1, 2, 3]),), 1),
        TestCase("last element", ((5, [1, 2, 3, 5]),), 1),
        TestCase("exact sum", ((6, [1, 2, 3]),), 3),
        TestCase("larger than all", ((100, [1, 2, 3, 4, 5]),), 0),
    ],

    "longest_repeating_character_replacement": [
        TestCase("example 1", (("ABAB", 2),), 4),
        TestCase("example 2", (("AABABBA", 1),), 4),
        TestCase("no replacement", (("AAAA", 0),), 4),
        TestCase("all different", (("ABCD", 3),), 4),
        TestCase("single char", (("A", 0),), 1),
        TestCase("two chars", (("AB", 1),), 2),
        TestCase("empty", (("", 2),), 0),
        TestCase("all same", (("BBBB", 2),), 4),
    ],

    "permutation_in_string": [
        TestCase("found", (("ab", "eidbaooo"),), True),
        TestCase("not found", (("ab", "eidboaoo"),), False),
        TestCase("exact match", (("abc", "abc"),), True),
        TestCase("at end", (("ab", "cdab"),), True),
        TestCase("longer s1", (("abc", "ab"),), False),
        TestCase("single char found", (("a", "a"),), True),
        TestCase("single char not found", (("a", "b"),), False),
        TestCase("repeated chars", (("aab", "cbdaaboa"),), True),
    ],

    "find_all_anagrams": [
        TestCase("example 1", (("cbaebabacd", "abc"),), [0, 6]),
        TestCase("example 2", (("abab", "ab"),), [0, 1, 2]),
        TestCase("no anagrams", (("xyz", "abc"),), []),
        TestCase("single char", (("aaaa", "a"),), [0, 1, 2, 3]),
        TestCase("whole string", (("abc", "abc"),), [0]),
        TestCase("p longer", (("ab", "abc"),), []),
        TestCase("empty s", (("", "a"),), []),
        TestCase("overlapping", (("aaa", "aa"),), [0, 1]),
    ],

    "max_consecutive_ones_iii": [
        TestCase("example 1", (([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2),), 6),
        TestCase("example 2", (([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3),), 10),
        TestCase("all ones", (([1, 1, 1], 0),), 3),
        TestCase("all zeros", (([0, 0, 0], 3),), 3),
        TestCase("k equals length", (([0, 1, 0], 3),), 3),
        TestCase("single element", (([1], 0),), 1),
        TestCase("no flips needed", (([1, 1, 1, 1], 2),), 4),
        TestCase("all need flip", (([0, 0, 0, 0], 2),), 2),
    ],

    "fruit_into_baskets": [
        TestCase("example 1", (([1, 2, 1],),), 3),
        TestCase("example 2", (([0, 1, 2, 2],),), 3),
        TestCase("example 3", (([1, 2, 3, 2, 2],),), 4),
        TestCase("single type", (([1, 1, 1, 1],),), 4),
        TestCase("two types", (([1, 2, 1, 2],),), 4),
        TestCase("three types", (([1, 2, 3],),), 2),
        TestCase("single element", (([5],),), 1),
        TestCase("alternating three", (([1, 2, 3, 1, 2, 3],),), 2),
    ],

    "longest_substring_k_distinct": [
        TestCase("example 1", (("eceba", 2),), 3),
        TestCase("example 2", (("aa", 1),), 2),
        TestCase("k zero", (("abc", 0),), 0),
        TestCase("k larger", (("abc", 5),), 3),
        TestCase("all same", (("aaaa", 1),), 4),
        TestCase("empty string", (("", 2),), 0),
        TestCase("single char", (("a", 1),), 1),
        TestCase("k equals distinct", (("abc", 3),), 3),
    ],
}
