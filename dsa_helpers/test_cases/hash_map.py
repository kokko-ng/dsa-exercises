"""Test cases for Hash Map problems (Category 02)."""

from . import TestCase, nested_set_compare, set_compare

HASH_MAP_TESTS = {
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
        TestCase("single word per group", ((["abc", "def", "ghi", "jkl"],),),
                 [["abc"], ["def"], ["ghi"], ["jkl"]], nested_set_compare),
        TestCase("performance", ((["abc", "bca", "cab"] * 1000 + ["xyz", "zyx"] * 500,),), None, None, is_performance=True, max_time=1.0),
    ],

    "two_sum_ii": [
        TestCase("example 1", (([2, 7, 11, 15], 9),), [1, 2]),
        TestCase("example 2", (([2, 3, 4], 6),), [1, 3]),
        TestCase("example 3", (([-1, 0], -1),), [1, 2]),
        TestCase("at ends", (([1, 2, 3, 4, 5], 6),), [1, 5]),
        TestCase("duplicates", (([1, 2, 2, 3], 4),), [1, 4]),
        TestCase("negative sum", (([-5, -3, -1, 0, 2], -8),), [1, 2]),
        TestCase("large gap", (([1, 2, 3, 50, 100], 103),), [3, 5]),
        TestCase("adjacent", (([1, 2, 3, 4, 5], 3),), [1, 2]),
    ],

    "contains_duplicate": [
        TestCase("has duplicate", (([1, 2, 3, 1],),), True),
        TestCase("no duplicate", (([1, 2, 3, 4],),), False),
        TestCase("multiple dups", (([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],),), True),
        TestCase("empty", (([],),), False),
        TestCase("single element", (([1],),), False),
        TestCase("two same", (([1, 1],),), True),
        TestCase("two different", (([1, 2],),), False),
        TestCase("negative numbers", (([-1, -2, -3, -1],),), True),
        TestCase("large array no dup", ((list(range(10000)),),), False),
    ],

    "isomorphic_strings": [
        TestCase("egg add", (("egg", "add"),), True),
        TestCase("foo bar", (("foo", "bar"),), False),
        TestCase("paper title", (("paper", "title"),), True),
        TestCase("single char", (("a", "b"),), True),
        TestCase("empty", (("", ""),), True),
        TestCase("badc baba", (("badc", "baba"),), False),
        TestCase("abab cdcd", (("abab", "cdcd"),), True),
        TestCase("same strings", (("abc", "abc"),), True),
        TestCase("ab aa", (("ab", "aa"),), False),
    ],

    "word_pattern": [
        TestCase("match", (("abba", "dog cat cat dog"),), True),
        TestCase("no match", (("abba", "dog cat cat fish"),), False),
        TestCase("extra pattern", (("aaaa", "dog cat cat dog"),), False),
        TestCase("single", (("a", "dog"),), True),
        TestCase("abba abba", (("abba", "dog dog dog dog"),), False),
        TestCase("different lengths", (("abc", "b c"),), False),
        TestCase("same word", (("ab", "dog dog"),), False),
        TestCase("long pattern", (("abcabc", "one two three one two three"),), True),
    ],

    "happy_number": [
        TestCase("19 is happy", ((19,),), True),
        TestCase("2 is not happy", ((2,),), False),
        TestCase("1 is happy", ((1,),), True),
        TestCase("7 is happy", ((7,),), True),
        TestCase("4 is not happy", ((4,),), False),
        TestCase("100 is happy", ((100,),), True),
        TestCase("10 is happy", ((10,),), True),
        TestCase("13 is happy", ((13,),), True),
        TestCase("20 is not happy", ((20,),), False),
    ],

    "first_unique_character": [
        TestCase("leetcode", (("leetcode",),), 0),
        TestCase("loveleetcode", (("loveleetcode",),), 2),
        TestCase("aabb", (("aabb",),), -1),
        TestCase("single", (("z",),), 0),
        TestCase("all same", (("aaa",),), -1),
        TestCase("unique at end", (("aabbccd",),), 6),
        TestCase("unique in middle", (("aabcbba",),), 3),
        TestCase("first unique", (("abc",),), 0),
        TestCase("empty", (("",),), -1),
    ],

    "intersection_of_two_arrays": [
        TestCase("example 1", (([1, 2, 2, 1], [2, 2]),), [2], set_compare),
        TestCase("example 2", (([4, 9, 5], [9, 4, 9, 8, 4]),), [4, 9], set_compare),
        TestCase("no intersection", (([1, 2], [3, 4]),), [], set_compare),
        TestCase("same arrays", (([1, 2, 3], [1, 2, 3]),), [1, 2, 3], set_compare),
        TestCase("empty first", (([], [1, 2]),), [], set_compare),
        TestCase("empty second", (([1, 2], []),), [], set_compare),
        TestCase("complete overlap", (([1, 1, 1], [1]),), [1], set_compare),
        TestCase("negative numbers", (([-1, -2, -3], [-2, -3, -4]),), [-2, -3], set_compare),
    ],

    "longest_consecutive_sequence": [
        TestCase("example 1", (([100, 4, 200, 1, 3, 2],),), 4),
        TestCase("example 2", (([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],),), 9),
        TestCase("empty", (([],),), 0),
        TestCase("single element", (([5],),), 1),
        TestCase("no sequence", (([10, 20, 30],),), 1),
        TestCase("with duplicates", (([1, 2, 2, 3],),), 3),
        TestCase("negative numbers", (([-2, -1, 0, 1],),), 4),
        TestCase("scattered", (([1, 100, 2, 200, 3, 300],),), 3),
        TestCase("all same", (([5, 5, 5, 5],),), 1),
    ],

    "subarray_sum_equals_k": [
        TestCase("example 1", (([1, 1, 1], 2),), 2),
        TestCase("example 2", (([1, 2, 3], 3),), 2),
        TestCase("negative", (([1, -1, 0], 0),), 3),
        TestCase("single match", (([1], 1),), 1),
        TestCase("no match", (([1, 2, 3], 7),), 0),
        TestCase("all zeros", (([0, 0, 0], 0),), 6),
        TestCase("negative numbers", (([-1, -1, 1], 0),), 1),
        TestCase("large k", (([1, 2, 3, 4, 5], 15),), 1),
        TestCase("cumulative", (([3, 4, 7, 2, -3, 1, 4, 2], 7),), 4),
    ],

    "four_sum_ii": [
        TestCase("example 1", (([1, 2], [-2, -1], [-1, 2], [0, 2]),), 2),
        TestCase("all zeros", (([0], [0], [0], [0]),), 1),
        TestCase("example 2", (([0, 1, -1], [-1, 1, 0], [0, 0, 1], [-1, 1, 1]),), 17),
        TestCase("no solution", (([1], [1], [1], [1]),), 0),
        TestCase("single elements", (([1], [-1], [0], [0]),), 1),
        TestCase("negative only", (([-1, -1], [-1], [1, 1], [1]),), 4),
    ],

    "lru_cache": [
        # LRU cache requires special handling - leaving placeholder
    ],
}
