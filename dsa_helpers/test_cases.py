"""
Test case definitions for all DSA exercises.

Each function has a list of TestCase objects with:
- name: Test description
- args: Tuple of arguments to pass to the function
- expected: Expected return value
- comparator: Optional comparison function (default: equality)
- is_performance: Whether this is a performance test
- max_time: Maximum allowed execution time in seconds
"""

from dataclasses import dataclass
from typing import Any, Callable, Optional, List

from .comparators import (
    sorted_compare,
    set_compare,
    nested_set_compare,
    unordered_list_compare,
    topological_order_compare,
)


@dataclass
class TestCase:
    """A single test case."""
    name: str
    args: tuple
    expected: Any
    comparator: Optional[Callable[[Any, Any], bool]] = None
    is_performance: bool = False
    max_time: Optional[float] = None


# =============================================================================
# TEST CASES REGISTRY
# =============================================================================

TEST_CASES: dict[str, List[TestCase]] = {
    # =========================================================================
    # 01_array_string
    # =========================================================================
    "two_sum": [
        TestCase("simple case", (([2, 7, 11, 15], 9),), [0, 1], sorted_compare),
        TestCase("middle elements", (([3, 2, 4], 6),), [1, 2], sorted_compare),
        TestCase("duplicate values", (([3, 3], 6),), [0, 1], sorted_compare),
        TestCase("negative numbers", (([-1, -2, -3, -4, -5], -8),), [2, 4], sorted_compare),
        TestCase("mixed signs", (([-3, 4, 3, 90], 0),), [0, 2], sorted_compare),
        TestCase("zeros", (([0, 4, 3, 0], 0),), [0, 3], sorted_compare),
        TestCase("large numbers", (([1000000000, 2, 1000000000], 2000000000),), [0, 2], sorted_compare),
        TestCase("target at end", (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19),), [8, 9], sorted_compare),
        TestCase("negative target", (([5, -10, 3, -6], -16),), [1, 3], sorted_compare),
        TestCase("performance", ((list(range(100000)), 199997),), [99998, 99999], sorted_compare, is_performance=True, max_time=1.0),
    ],

    "valid_anagram": [
        TestCase("simple anagram", (("anagram", "nagaram"),), True),
        TestCase("not anagram", (("rat", "car"),), False),
        TestCase("same string", (("abc", "abc"),), True),
        TestCase("different lengths", (("ab", "abc"),), False),
        TestCase("empty strings", (("", ""),), True),
        TestCase("single char same", (("a", "a"),), True),
        TestCase("single char diff", (("a", "b"),), False),
        TestCase("repeated chars", (("aabb", "abab"),), True),
        TestCase("same letters diff count", (("aab", "abb"),), False),
        TestCase("long anagram", (("abcdefghijklmnopqrstuvwxyz" * 10, "zyxwvutsrqponmlkjihgfedcba" * 10),), True),
        TestCase("performance", (("abcdefghij" * 5000, "jihgfedcba" * 5000),), True, is_performance=True, max_time=1.0),
    ],

    "valid_palindrome": [
        TestCase("classic palindrome", (("A man, a plan, a canal: Panama",),), True),
        TestCase("not palindrome", (("race a car",),), False),
        TestCase("simple palindrome", (("aba",),), True),
        TestCase("even palindrome", (("abba",),), True),
        TestCase("empty after filter", ((" ",),), True),
        TestCase("single char", (("a",),), True),
        TestCase("only numbers", (("12321",),), True),
        TestCase("mixed case", (("Aa",),), True),
        TestCase("special chars only", ((",.!?",),), True),
        TestCase("numbers and letters", (("0P",),), False),
    ],

    "reverse_string": [
        TestCase("simple", ((["h", "e", "l", "l", "o"],),), ["o", "l", "l", "e", "h"]),
        TestCase("even length", ((["H", "a", "n", "n", "a", "h"],),), ["h", "a", "n", "n", "a", "H"]),
        TestCase("single char", ((["a"],),), ["a"]),
        TestCase("two chars", ((["a", "b"],),), ["b", "a"]),
        TestCase("empty", (([],),), []),
        TestCase("palindrome", ((["r", "a", "c", "e", "c", "a", "r"],),), ["r", "a", "c", "e", "c", "a", "r"]),
    ],

    "longest_common_prefix": [
        TestCase("common prefix", ((["flower", "flow", "flight"],),), "fl"),
        TestCase("no common prefix", ((["dog", "racecar", "car"],),), ""),
        TestCase("all same", ((["test", "test", "test"],),), "test"),
        TestCase("empty list", (([],),), ""),
        TestCase("single word", ((["alone"],),), "alone"),
        TestCase("empty string in list", ((["", "b", "c"],),), ""),
        TestCase("all empty", ((["", "", ""],),), ""),
        TestCase("single char prefix", ((["ab", "a"],),), "a"),
    ],

    "remove_duplicates": [
        TestCase("with duplicates", (([1, 1, 2],),), 2),
        TestCase("more duplicates", (([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],),), 5),
        TestCase("no duplicates", (([1, 2, 3],),), 3),
        TestCase("all same", (([1, 1, 1, 1],),), 1),
        TestCase("empty", (([],),), 0),
        TestCase("single element", (([1],),), 1),
        TestCase("two same", (([2, 2],),), 1),
        TestCase("two different", (([1, 2],),), 2),
    ],

    "rotate_array": [
        TestCase("rotate by 3", (([1, 2, 3, 4, 5, 6, 7], 3),), [5, 6, 7, 1, 2, 3, 4]),
        TestCase("rotate by 2", (([-1, -100, 3, 99], 2),), [3, 99, -1, -100]),
        TestCase("rotate by length", (([1, 2, 3], 3),), [1, 2, 3]),
        TestCase("rotate single", (([1], 1),), [1]),
        TestCase("rotate by zero", (([1, 2, 3], 0),), [1, 2, 3]),
        TestCase("rotate more than length", (([1, 2, 3], 4),), [3, 1, 2]),
        TestCase("rotate by 1", (([1, 2, 3, 4], 1),), [4, 1, 2, 3]),
    ],

    "move_zeroes": [
        TestCase("mixed", (([0, 1, 0, 3, 12],),), [1, 3, 12, 0, 0]),
        TestCase("single zero", (([0],),), [0]),
        TestCase("no zeros", (([1, 2, 3],),), [1, 2, 3]),
        TestCase("all zeros", (([0, 0, 0],),), [0, 0, 0]),
        TestCase("zeros at end", (([1, 2, 0, 0],),), [1, 2, 0, 0]),
        TestCase("zeros at start", (([0, 0, 1, 2],),), [1, 2, 0, 0]),
        TestCase("alternating", (([0, 1, 0, 2, 0, 3],),), [1, 2, 3, 0, 0, 0]),
        TestCase("empty", (([],),), []),
    ],

    "plus_one": [
        TestCase("simple", (([1, 2, 3],),), [1, 2, 4]),
        TestCase("carry", (([9],),), [1, 0]),
        TestCase("multiple carry", (([9, 9, 9],),), [1, 0, 0, 0]),
        TestCase("no carry", (([1, 2, 9],),), [1, 3, 0]),
        TestCase("single digit", (([0],),), [1]),
        TestCase("middle carry", (([1, 9, 9],),), [2, 0, 0]),
        TestCase("large number", (([9, 8, 7, 6, 5, 4, 3, 2, 1, 0],),), [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]),
    ],

    "merge_sorted_arrays": [
        TestCase("simple merge", (([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),), [1, 2, 2, 3, 5, 6]),
        TestCase("empty second", (([1], 1, [], 0),), [1]),
        TestCase("empty first", (([0], 0, [1], 1),), [1]),
        TestCase("all from second", (([0, 0, 0], 0, [1, 2, 3], 3),), [1, 2, 3]),
        TestCase("interleaved", (([1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3),), [1, 2, 3, 4, 5, 6]),
    ],

    "product_except_self": [
        TestCase("simple", (([1, 2, 3, 4],),), [24, 12, 8, 6]),
        TestCase("with zero", (([-1, 1, 0, -3, 3],),), [0, 0, 9, 0, 0]),
        TestCase("two elements", (([1, 2],),), [2, 1]),
        TestCase("with negative", (([-1, -2, -3],),), [6, 3, 2]),
        TestCase("two zeros", (([0, 0, 1],),), [0, 0, 0]),
        TestCase("all ones", (([1, 1, 1, 1],),), [1, 1, 1, 1]),
    ],

    "container_with_most_water": [
        TestCase("example 1", (([1, 8, 6, 2, 5, 4, 8, 3, 7],),), 49),
        TestCase("example 2", (([1, 1],),), 1),
        TestCase("decreasing", (([4, 3, 2, 1, 4],),), 16),
        TestCase("increasing", (([1, 2, 3, 4, 5],),), 6),
        TestCase("peak in middle", (([1, 2, 4, 3],),), 4),
        TestCase("same height", (([5, 5, 5, 5],),), 15),
    ],

    "trapping_rain_water": [
        TestCase("example 1", (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],),), 6),
        TestCase("example 2", (([4, 2, 0, 3, 2, 5],),), 9),
        TestCase("no water", (([1, 2, 3],),), 0),
        TestCase("descending", (([5, 4, 3, 2, 1],),), 0),
        TestCase("single bar", (([5],),), 0),
        TestCase("two bars", (([1, 2],),), 0),
        TestCase("valley", (([3, 0, 3],),), 3),
        TestCase("empty", (([],),), 0),
    ],

    "longest_substring_without_repeating": [
        TestCase("abcabcbb", (("abcabcbb",),), 3),
        TestCase("bbbbb", (("bbbbb",),), 1),
        TestCase("pwwkew", (("pwwkew",),), 3),
        TestCase("empty", (("",),), 0),
        TestCase("single char", (("a",),), 1),
        TestCase("all unique", (("abcdef",),), 6),
        TestCase("two chars alternating", (("abababab",),), 2),
        TestCase("space in string", (("hello world",),), 6),
    ],

    "minimum_window_substring": [
        TestCase("example 1", (("ADOBECODEBANC", "ABC"),), "BANC"),
        TestCase("example 2", (("a", "a"),), "a"),
        TestCase("no window", (("a", "aa"),), ""),
        TestCase("exact match", (("abc", "abc"),), "abc"),
        TestCase("t larger", (("a", "b"),), ""),
        TestCase("duplicate chars in t", (("aa", "aa"),), "aa"),
    ],

    # =========================================================================
    # 02_hash_map
    # =========================================================================
    "group_anagrams": [
        TestCase("example", ((["eat", "tea", "tan", "ate", "nat", "bat"],),),
                 [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]], nested_set_compare),
        TestCase("empty string", (([""]),), [[""]], nested_set_compare),
        TestCase("single char", ((["a"],),), [["a"]], nested_set_compare),
        TestCase("no anagrams", ((["abc", "def", "ghi"],),), [["abc"], ["def"], ["ghi"]], nested_set_compare),
        TestCase("all anagrams", ((["abc", "bca", "cab", "acb"],),), [["abc", "acb", "bca", "cab"]], nested_set_compare),
        TestCase("multiple empty", ((["", ""],),), [["", ""]], nested_set_compare),
        TestCase("same letters diff counts", ((["aab", "aba", "baa", "ab"],),),
                 [["aab", "aba", "baa"], ["ab"]], nested_set_compare),
        TestCase("performance", ((["abc", "bca", "cab"] * 1000 + ["xyz", "zyx"] * 500,),), None, None, is_performance=True, max_time=1.0),
    ],

    "two_sum_ii": [
        TestCase("example 1", (([2, 7, 11, 15], 9),), [1, 2]),
        TestCase("example 2", (([2, 3, 4], 6),), [1, 3]),
        TestCase("example 3", (([-1, 0], -1),), [1, 2]),
        TestCase("at ends", (([1, 2, 3, 4, 5], 6),), [1, 5]),
        TestCase("duplicates", (([1, 1, 1, 1], 2),), [1, 2]),
        TestCase("negative sum", (([-5, -3, -1, 0, 2], -8),), [1, 2]),
    ],

    "contains_duplicate": [
        TestCase("has duplicate", (([1, 2, 3, 1],),), True),
        TestCase("no duplicate", (([1, 2, 3, 4],),), False),
        TestCase("multiple dups", (([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],),), True),
        TestCase("empty", (([],),), False),
        TestCase("single element", (([1],),), False),
        TestCase("two same", (([1, 1],),), True),
        TestCase("two different", (([1, 2],),), False),
    ],

    "isomorphic_strings": [
        TestCase("egg add", (("egg", "add"),), True),
        TestCase("foo bar", (("foo", "bar"),), False),
        TestCase("paper title", (("paper", "title"),), True),
        TestCase("single char", (("a", "b"),), True),
        TestCase("empty", (("", ""),), True),
        TestCase("badc baba", (("badc", "baba"),), False),
        TestCase("abab cdcd", (("abab", "cdcd"),), True),
    ],

    "word_pattern": [
        TestCase("match", (("abba", "dog cat cat dog"),), True),
        TestCase("no match", (("abba", "dog cat cat fish"),), False),
        TestCase("extra pattern", (("aaaa", "dog cat cat dog"),), False),
        TestCase("single", (("a", "dog"),), True),
        TestCase("abba abba", (("abba", "dog dog dog dog"),), False),
        TestCase("different lengths", (("abc", "b c"),), False),
    ],

    "happy_number": [
        TestCase("19 is happy", ((19,),), True),
        TestCase("2 is not happy", ((2,),), False),
        TestCase("1 is happy", ((1,),), True),
        TestCase("7 is happy", ((7,),), True),
        TestCase("4 is not happy", ((4,),), False),
        TestCase("100 is happy", ((100,),), True),
    ],

    "first_unique_character": [
        TestCase("leetcode", (("leetcode",),), 0),
        TestCase("loveleetcode", (("loveleetcode",),), 2),
        TestCase("aabb", (("aabb",),), -1),
        TestCase("single", (("z",),), 0),
        TestCase("all same", (("aaa",),), -1),
        TestCase("unique at end", (("aabbccd",),), 6),
    ],

    "intersection_of_two_arrays": [
        TestCase("example 1", (([1, 2, 2, 1], [2, 2]),), [2], set_compare),
        TestCase("example 2", (([4, 9, 5], [9, 4, 9, 8, 4]),), [4, 9], set_compare),
        TestCase("no intersection", (([1, 2], [3, 4]),), [], set_compare),
        TestCase("same arrays", (([1, 2, 3], [1, 2, 3]),), [1, 2, 3], set_compare),
        TestCase("empty first", (([], [1, 2]),), [], set_compare),
        TestCase("empty second", (([1, 2], []),), [], set_compare),
    ],

    "longest_consecutive_sequence": [
        TestCase("example 1", (([100, 4, 200, 1, 3, 2],),), 4),
        TestCase("example 2", (([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],),), 9),
        TestCase("empty", (([],),), 0),
        TestCase("single element", (([5],),), 1),
        TestCase("no sequence", (([10, 20, 30],),), 1),
        TestCase("with duplicates", (([1, 2, 2, 3],),), 3),
        TestCase("negative numbers", (([-2, -1, 0, 1],),), 4),
    ],

    "subarray_sum_equals_k": [
        TestCase("example 1", (([1, 1, 1], 2),), 2),
        TestCase("example 2", (([1, 2, 3], 3),), 2),
        TestCase("negative", (([1, -1, 0], 0),), 3),
        TestCase("single match", (([1], 1),), 1),
        TestCase("no match", (([1, 2, 3], 7),), 0),
        TestCase("all zeros", (([0, 0, 0], 0),), 6),
        TestCase("negative numbers", (([-1, -1, 1], 0),), 1),
    ],

    "four_sum_ii": [
        TestCase("example 1", (([1, 2], [-2, -1], [-1, 2], [0, 2]),), 2),
        TestCase("all zeros", (([0], [0], [0], [0]),), 1),
        TestCase("example 2", (([0, 1, -1], [-1, 1, 0], [0, 0, 1], [-1, 1, 1]),), 17),
    ],

    # =========================================================================
    # 05_merge_intervals
    # =========================================================================
    "merge_intervals": [
        TestCase("overlapping", (([[1, 3], [2, 6], [8, 10], [15, 18]],),), [[1, 6], [8, 10], [15, 18]]),
        TestCase("touching", (([[1, 4], [4, 5]],),), [[1, 5]]),
        TestCase("single", (([[1, 4]],),), [[1, 4]]),
        TestCase("no overlap", (([[1, 2], [3, 4], [5, 6]],),), [[1, 2], [3, 4], [5, 6]]),
        TestCase("all overlap", (([[1, 10], [2, 6], [3, 5], [7, 9]],),), [[1, 10]]),
        TestCase("unsorted input", (([[3, 5], [1, 4]],),), [[1, 5]]),
        TestCase("nested intervals", (([[1, 10], [2, 3], [4, 5], [6, 7]],),), [[1, 10]]),
        TestCase("identical intervals", (([[1, 3], [1, 3], [1, 3]],),), [[1, 3]]),
        TestCase("chain merge", (([[1, 2], [2, 3], [3, 4], [4, 5]],),), [[1, 5]]),
    ],

    "insert_interval": [
        TestCase("middle insert", (([[1, 3], [6, 9]], [2, 5]),), [[1, 5], [6, 9]]),
        TestCase("merge multiple", (([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),), [[1, 2], [3, 10], [12, 16]]),
        TestCase("no overlap", (([[1, 2], [5, 6]], [3, 4]),), [[1, 2], [3, 4], [5, 6]]),
        TestCase("merge all", (([[1, 3], [4, 6], [7, 9]], [2, 8]),), [[1, 9]]),
        TestCase("at start", (([[3, 5], [6, 8]], [1, 2]),), [[1, 2], [3, 5], [6, 8]]),
        TestCase("at end", (([[1, 2], [3, 4]], [5, 6]),), [[1, 2], [3, 4], [5, 6]]),
        TestCase("empty intervals", (([], [1, 3]),), [[1, 3]]),
    ],

    "intervals_intersection": [
        TestCase("example", (([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]),),
                 [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]),
        TestCase("no intersection", (([[1, 2], [5, 6]], [[3, 4], [7, 8]]),), []),
        TestCase("full overlap", (([[1, 10]], [[1, 10]]),), [[1, 10]]),
        TestCase("one empty", (([], [[1, 2]]),), []),
    ],

    "meeting_rooms": [
        TestCase("overlapping", (([[0, 30], [5, 10], [15, 20]],),), False),
        TestCase("no overlap", (([[7, 10], [2, 4]],),), True),
        TestCase("touching", (([[1, 2], [2, 3]],),), True),
        TestCase("single meeting", (([[1, 5]],),), True),
        TestCase("empty", (([],),), True),
    ],

    "meeting_rooms_ii": [
        TestCase("example 1", (([[0, 30], [5, 10], [15, 20]],),), 2),
        TestCase("example 2", (([[7, 10], [2, 4]],),), 1),
        TestCase("all overlap", (([[1, 10], [2, 9], [3, 8]],),), 3),
        TestCase("no overlap", (([[1, 2], [3, 4], [5, 6]],),), 1),
        TestCase("touching", (([[1, 2], [2, 3], [3, 4]],),), 1),
        TestCase("empty", (([],),), 0),
    ],

    "non_overlapping_intervals": [
        TestCase("example 1", (([[1, 2], [2, 3], [3, 4], [1, 3]],),), 1),
        TestCase("example 2", (([[1, 2], [1, 2], [1, 2]],),), 2),
        TestCase("no removal", (([[1, 2], [3, 4]],),), 0),
    ],

    # =========================================================================
    # 06_cyclic_sort
    # =========================================================================
    "cyclic_sort": [
        TestCase("unsorted", (([3, 1, 5, 4, 2],),), [1, 2, 3, 4, 5]),
        TestCase("reverse", (([5, 4, 3, 2, 1],),), [1, 2, 3, 4, 5]),
        TestCase("sorted", (([1, 2, 3, 4, 5],),), [1, 2, 3, 4, 5]),
        TestCase("single", (([1],),), [1]),
        TestCase("two elements", (([2, 1],),), [1, 2]),
    ],

    "find_missing_number": [
        TestCase("missing 2", (([4, 0, 3, 1],),), 2),
        TestCase("missing 8", (([0, 1, 2, 3, 4, 5, 6, 7, 9],),), 8),
        TestCase("missing 0", (([1, 2, 3],),), 0),
        TestCase("missing last", (([0, 1, 2],),), 3),
        TestCase("single missing", (([0],),), 1),
        TestCase("missing first", (([1],),), 0),
    ],

    "find_all_missing_numbers": [
        TestCase("example 1", (([4, 3, 2, 7, 8, 2, 3, 1],),), [5, 6], sorted_compare),
        TestCase("example 2", (([1, 1],),), [2]),
        TestCase("no missing", (([1, 2, 3],),), []),
        TestCase("all missing", (([2, 2, 2],),), [1, 3], sorted_compare),
    ],

    "find_duplicate": [
        TestCase("example 1", (([1, 3, 4, 2, 2],),), 2),
        TestCase("example 2", (([3, 1, 3, 4, 2],),), 3),
        TestCase("at start", (([2, 2, 2, 2, 2],),), 2),
        TestCase("two elements", (([1, 1],),), 1),
    ],

    "find_all_duplicates": [
        TestCase("example", (([4, 3, 2, 7, 8, 2, 3, 1],),), [2, 3], set_compare),
        TestCase("no dups", (([1, 2, 3],),), []),
        TestCase("all dups", (([1, 1, 2, 2],),), [1, 2], set_compare),
        TestCase("single dup", (([1, 1],),), [1]),
    ],

    "find_corrupt_pair": [
        TestCase("example 1", (([3, 1, 2, 5, 2],),), [2, 4], sorted_compare),
        TestCase("example 2", (([3, 1, 2, 3, 6, 4],),), [3, 5], sorted_compare),
    ],

    "first_missing_positive": [
        TestCase("example 1", (([1, 2, 0],),), 3),
        TestCase("example 2", (([3, 4, -1, 1],),), 2),
        TestCase("example 3", (([7, 8, 9, 11, 12],),), 1),
        TestCase("consecutive", (([1, 2, 3],),), 4),
        TestCase("single negative", (([-1],),), 1),
    ],

    # =========================================================================
    # 11_modified_binary_search
    # =========================================================================
    "binary_search": [
        TestCase("found middle", (([-1, 0, 3, 5, 9, 12], 9),), 4),
        TestCase("found first", (([-1, 0, 3, 5, 9, 12], -1),), 0),
        TestCase("found last", (([-1, 0, 3, 5, 9, 12], 12),), 5),
        TestCase("not found", (([-1, 0, 3, 5, 9, 12], 2),), -1),
        TestCase("single element found", (([5], 5),), 0),
        TestCase("single element not found", (([5], 3),), -1),
        TestCase("two elements first", (([1, 3], 1),), 0),
        TestCase("two elements second", (([1, 3], 3),), 1),
        TestCase("negative numbers", (([-10, -5, -3, -1], -5),), 1),
        TestCase("target smaller than all", (([2, 4, 6, 8], 1),), -1),
        TestCase("target larger than all", (([2, 4, 6, 8], 10),), -1),
        TestCase("performance", ((list(range(0, 2000000, 2)), 999998),), 499999, None, is_performance=True, max_time=0.1),
    ],

    "order_agnostic_search": [
        TestCase("ascending found", (([1, 2, 3, 4, 5, 6, 7], 5),), 4),
        TestCase("descending found", (([10, 6, 4], 10),), 0),
        TestCase("not found", (([1, 2, 3, 4], 0),), -1),
        TestCase("single ascending", (([5], 5),), 0),
        TestCase("descending not found", (([10, 8, 6, 4, 2], 5),), -1),
        TestCase("descending last", (([10, 8, 6, 4, 2], 2),), 4),
    ],

    "ceiling_of_number": [
        TestCase("exact match", (([4, 6, 10], 6),), 1),
        TestCase("ceiling", (([1, 3, 8, 10, 15], 12),), 4),
        TestCase("smaller than all", (([4, 6, 10], 1),), 0),
        TestCase("between elements", (([1, 3, 5, 7], 4),), 2),
        TestCase("larger than all", (([1, 2, 3], 5),), -1),
    ],

    "floor_of_number": [
        TestCase("exact match", (([4, 6, 10], 6),), 1),
        TestCase("floor", (([1, 3, 8, 10, 15], 12),), 3),
        TestCase("larger than all", (([1, 3, 8, 10, 15], 20),), 4),
        TestCase("between elements", (([1, 3, 5, 7], 4),), 1),
        TestCase("smaller than all", (([2, 3, 4], 1),), -1),
    ],

    "next_letter": [
        TestCase("example 1", ((["c", "f", "j"], "a"),), "c"),
        TestCase("example 2", ((["c", "f", "j"], "c"),), "f"),
        TestCase("wrap around", ((["c", "f", "j"], "k"),), "c"),
        TestCase("between letters", ((["c", "f", "j"], "d"),), "f"),
        TestCase("before first", ((["c", "f", "j"], "b"),), "c"),
    ],

    "number_range": [
        TestCase("found", (([5, 7, 7, 8, 8, 10], 8),), [3, 4]),
        TestCase("not found", (([5, 7, 7, 8, 8, 10], 6),), [-1, -1]),
        TestCase("single", (([1], 1),), [0, 0]),
        TestCase("all same", (([5, 5, 5, 5], 5),), [0, 3]),
        TestCase("at start", (([1, 1, 2, 3], 1),), [0, 1]),
        TestCase("at end", (([1, 2, 3, 3], 3),), [2, 3]),
    ],

    "search_in_rotated_array": [
        TestCase("found left", (([4, 5, 6, 7, 0, 1, 2], 0),), 4),
        TestCase("found right", (([4, 5, 6, 7, 0, 1, 2], 5),), 1),
        TestCase("not found", (([4, 5, 6, 7, 0, 1, 2], 3),), -1),
        TestCase("not rotated", (([1, 2, 3, 4, 5], 3),), 2),
        TestCase("single element", (([1], 1),), 0),
        TestCase("two elements", (([2, 1], 1),), 1),
    ],

    "rotation_count": [
        TestCase("rotated", (([10, 15, 1, 3, 8],),), 2),
        TestCase("not rotated", (([1, 2, 3, 4, 5],),), 0),
        TestCase("fully rotated", (([4, 5, 7, 9, 10, -1, 2],),), 5),
        TestCase("single element", (([5],),), 0),
        TestCase("two elements", (([2, 1],),), 1),
    ],

    "search_in_infinite_array": [
        TestCase("found", (([4, 6, 8, 10, 12, 14, 16, 18, 20], 16),), 6),
        TestCase("found at start", (([1, 2, 3, 4, 5], 1),), 0),
        TestCase("not found", (([1, 2, 3, 4, 5], 10),), -1),
    ],

    "minimum_difference_element": [
        TestCase("example 1", (([4, 6, 10], 7),), 6),
        TestCase("example 2", (([4, 6, 10], 4),), 4),
        TestCase("example 3", (([1, 3, 8, 10, 15], 12),), 10),
        TestCase("exact match", (([1, 5, 10], 5),), 5),
    ],

    "bitonic_array_maximum": [
        TestCase("example 1", (([1, 3, 8, 12, 4, 2],),), 12),
        TestCase("example 2", (([3, 8, 3, 1],),), 8),
        TestCase("example 3", (([1, 3, 8, 12],),), 12),
        TestCase("peak at start", (([10, 8, 6, 4],),), 10),
    ],

    # =========================================================================
    # 12_top_k_elements
    # =========================================================================
    "top_k_frequent": [
        TestCase("example 1", (([1, 1, 1, 2, 2, 3], 2),), [1, 2], set_compare),
        TestCase("single", (([1], 1),), [1]),
        TestCase("all same frequency", (([1, 2, 3], 2),), None, None),  # Multiple valid answers
        TestCase("negative numbers", (([-1, -1, -2, -2, -2], 1),), [-2]),
    ],

    "kth_largest_element": [
        TestCase("example 1", (([3, 2, 1, 5, 6, 4], 2),), 5),
        TestCase("example 2", (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),), 4),
        TestCase("single element", (([1], 1),), 1),
        TestCase("all same", (([2, 2, 2, 2], 2),), 2),
        TestCase("with negatives", (([-1, -2, -3, -4], 2),), -2),
    ],

    "k_closest_points": [
        TestCase("example 1", (([[1, 3], [-2, 2]], 1),), [[-2, 2]]),
        TestCase("example 2", (([[3, 3], [5, -1], [-2, 4]], 2),), [[3, 3], [-2, 4]], unordered_list_compare),
        TestCase("origin", (([[0, 0], [1, 1]], 1),), [[0, 0]]),
        TestCase("same distance", (([[1, 0], [0, 1]], 2),), [[1, 0], [0, 1]], unordered_list_compare),
    ],

    "sort_characters_by_frequency": [
        TestCase("tree", (("tree",),), "eert"),  # or "eetr"
        TestCase("cccaaa", (("cccaaa",),), "cccaaa"),  # or "aaaccc"
        TestCase("Aabb", (("Aabb",),), "bbAa"),  # or "bbaA"
    ],

    "find_k_closest_elements": [
        TestCase("example 1", (([1, 2, 3, 4, 5], 4, 3),), [1, 2, 3, 4]),
        TestCase("example 2", (([1, 2, 3, 4, 5], 4, -1),), [1, 2, 3, 4]),
    ],

    # =========================================================================
    # 14_graph_patterns
    # =========================================================================
    "number_of_islands": [
        TestCase("single island", (([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]],),), 1),
        TestCase("three islands", (([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]],),), 3),
        TestCase("no islands", (([["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]],),), 0),
        TestCase("all land", (([["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]],),), 1),
        TestCase("single cell land", (([["1"]],),), 1),
        TestCase("single cell water", (([["0"]],),), 0),
        TestCase("diagonal not connected", (([["1", "0"], ["0", "1"]],),), 2),
    ],

    "course_schedule": [
        TestCase("possible", ((2, [[1, 0]]),), True),
        TestCase("impossible", ((2, [[1, 0], [0, 1]]),), False),
        TestCase("no prereqs", ((3, []),), True),
        TestCase("chain", ((4, [[1, 0], [2, 1], [3, 2]]),), True),
        TestCase("complex cycle", ((3, [[0, 1], [1, 2], [2, 0]]),), False),
    ],

    "course_schedule_ii": [
        TestCase("example 1", ((2, [[1, 0]]),), [0, 1]),
        TestCase("example 2", ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]),), [0, 1, 2, 3], topological_order_compare),
        TestCase("no prereqs", ((3, []),), [0, 1, 2], set_compare),
        TestCase("cycle", ((2, [[1, 0], [0, 1]]),), []),
    ],

    "clone_graph": [
        # This requires special handling for graph nodes
    ],

    "pacific_atlantic_water": [
        TestCase("example", (([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],),),
                 [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]], unordered_list_compare),
    ],

    # =========================================================================
    # 17_monotonic_stack_queue
    # =========================================================================
    "next_greater_element": [
        TestCase("example 1", (([4, 1, 2], [1, 3, 4, 2]),), [-1, 3, -1]),
        TestCase("example 2", (([2, 4], [1, 2, 3, 4]),), [3, -1]),
        TestCase("no greater", (([3, 2, 1], [3, 2, 1]),), [-1, -1, -1]),
        TestCase("all greater", (([1, 2, 3], [1, 2, 3, 4]),), [2, 3, 4]),
    ],

    "next_greater_element_ii": [
        TestCase("example 1", (([1, 2, 1],),), [2, -1, 2]),
        TestCase("example 2", (([1, 2, 3, 4, 3],),), [2, 3, 4, -1, 4]),
        TestCase("all same", (([5, 5, 5],),), [-1, -1, -1]),
    ],

    "daily_temperatures": [
        TestCase("example 1", (([73, 74, 75, 71, 69, 72, 76, 73],),), [1, 1, 4, 2, 1, 1, 0, 0]),
        TestCase("decreasing", (([30, 29, 28, 27],),), [0, 0, 0, 0]),
        TestCase("increasing", (([30, 31, 32, 33],),), [1, 1, 1, 0]),
        TestCase("single", (([50],),), [0]),
        TestCase("all same", (([70, 70, 70],),), [0, 0, 0]),
    ],

    "largest_rectangle_histogram": [
        TestCase("example 1", (([2, 1, 5, 6, 2, 3],),), 10),
        TestCase("example 2", (([2, 4],),), 4),
        TestCase("single bar", (([5],),), 5),
        TestCase("increasing", (([1, 2, 3, 4, 5],),), 9),
        TestCase("decreasing", (([5, 4, 3, 2, 1],),), 9),
        TestCase("all same", (([3, 3, 3, 3],),), 12),
    ],

    "remove_k_digits": [
        TestCase("example 1", (("1432219", 3),), "1219"),
        TestCase("example 2", (("10200", 1),), "200"),
        TestCase("example 3", (("10", 2),), "0"),
        TestCase("remove all", (("12345", 5),), "0"),
        TestCase("leading zeros", (("100200", 1),), "200"),
    ],

    "stock_span": [
        TestCase("example", (([100, 80, 60, 70, 60, 75, 85],),), [1, 1, 1, 2, 1, 4, 6]),
    ],

    "sum_of_subarray_minimums": [
        TestCase("example 1", (([3, 1, 2, 4],),), 17),
        TestCase("example 2", (([11, 81, 94, 43, 3],),), 444),
        TestCase("single", (([5],),), 5),
    ],

    "shortest_unsorted_subarray": [
        TestCase("example 1", (([2, 6, 4, 8, 10, 9, 15],),), 5),
        TestCase("sorted", (([1, 2, 3, 4],),), 0),
        TestCase("reverse", (([4, 3, 2, 1],),), 4),
        TestCase("single", (([1],),), 0),
    ],
}
