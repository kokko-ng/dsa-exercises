"""Test cases for Backtracking problems (Category 16)."""

from . import TestCase, nested_set_compare

BACKTRACKING_TESTS: dict[str, list[TestCase]] = {
    "combination_sum": [
        TestCase("basic", (([2, 3, 6, 7], 7),), [[2, 2, 3], [7]], nested_set_compare),
        TestCase(
            "multiple", (([2, 3, 5], 8),), [[2, 2, 2, 2], [2, 3, 3], [3, 5]], nested_set_compare
        ),
        TestCase("no solution", (([2], 1),), []),
        TestCase("single", (([1], 2),), [[1, 1]], nested_set_compare),
        TestCase("single candidate exact", (([7], 7),), [[7]], nested_set_compare),
        TestCase("large target", (([2, 3], 9),), [[2, 2, 2, 3], [3, 3, 3]], nested_set_compare),
    ],
    "combination_sum_ii": [
        TestCase(
            "with dups",
            (([10, 1, 2, 7, 6, 1, 5], 8),),
            [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
            nested_set_compare,
        ),
        TestCase("basic", (([2, 5, 2, 1, 2], 5),), [[1, 2, 2], [5]], nested_set_compare),
        TestCase("no solution", (([2, 4], 1),), []),
        TestCase("single element match", (([5], 5),), [[5]], nested_set_compare),
        TestCase("all same elements", (([1, 1, 1, 1], 2),), [[1, 1]], nested_set_compare),
    ],
    "combination_sum_iii": [
        TestCase("k=3 n=7", ((3, 7),), [[1, 2, 4]], nested_set_compare),
        TestCase("k=3 n=9", ((3, 9),), [[1, 2, 6], [1, 3, 5], [2, 3, 4]], nested_set_compare),
        TestCase("no solution", ((4, 1),), []),
        TestCase("k=2 n=3", ((2, 3),), [[1, 2]], nested_set_compare),
        TestCase("k=2 n=17", ((2, 17),), [[8, 9]], nested_set_compare),
        TestCase("k=9 n=45", ((9, 45),), [[1, 2, 3, 4, 5, 6, 7, 8, 9]], nested_set_compare),
    ],
    "letter_combinations_phone": [
        TestCase(
            "basic",
            (("23",),),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
            nested_set_compare,
        ),
        TestCase("empty", (("",),), []),
        TestCase("single", (("2",),), ["a", "b", "c"], nested_set_compare),
        TestCase("four letters", (("7",),), ["p", "q", "r", "s"], nested_set_compare),
        TestCase(
            "three digits",
            (("234",),),
            [
                "adg",
                "adh",
                "adi",
                "aeg",
                "aeh",
                "aei",
                "afg",
                "afh",
                "afi",
                "bdg",
                "bdh",
                "bdi",
                "beg",
                "beh",
                "bei",
                "bfg",
                "bfh",
                "bfi",
                "cdg",
                "cdh",
                "cdi",
                "ceg",
                "ceh",
                "cei",
                "cfg",
                "cfh",
                "cfi",
            ],
            nested_set_compare,
        ),
    ],
    "palindrome_partitioning": [
        TestCase("basic", (("aab",),), [["a", "a", "b"], ["aa", "b"]], nested_set_compare),
        TestCase("single", (("a",),), [["a"]]),
        TestCase("palindrome", (("aba",),), [["a", "b", "a"], ["aba"]], nested_set_compare),
        TestCase(
            "all same",
            (("aaa",),),
            [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]],
            nested_set_compare,
        ),
        TestCase("no palindrome partition", (("ab",),), [["a", "b"]], nested_set_compare),
    ],
    "n_queens": [
        TestCase(
            "n=4",
            ((4,),),
            [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
            nested_set_compare,
        ),
        TestCase("n=1", ((1,),), [["Q"]]),
        TestCase("n=2 no solution", ((2,),), []),
        TestCase("n=3 no solution", ((3,),), []),
        TestCase(
            "n=5 has solutions", ((5,),), 10, lambda result, expected: len(result) == expected
        ),
    ],
    "sudoku_solver": [
        TestCase(
            "basic",
            (
                (
                    [
                        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", "6", "."],
                        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", "6", ".", ".", ".", ".", "2", "8", "."],
                        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                    ],
                ),
            ),
            [
                ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
            ],
            check_modified_arg=0,
        ),
    ],
    "word_search": [
        TestCase(
            "exists",
            (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),),
            True,
        ),
        TestCase(
            "not exists",
            (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),),
            False,
        ),
        TestCase("single", (([["A"]], "A"),), True),
        TestCase("single not found", (([["A"]], "B"),), False),
        TestCase("word too long", (([["A", "B"], ["C", "D"]], "ABCDE"),), False),
        TestCase("snake path", (([["A", "B", "C"], ["F", "E", "D"]], "ABCDEF"),), True),
    ],
    "word_search_ii": [
        TestCase(
            "basic",
            (
                (
                    [
                        ["o", "a", "a", "n"],
                        ["e", "t", "a", "e"],
                        ["i", "h", "k", "r"],
                        ["i", "f", "l", "v"],
                    ],
                    ["oath", "pea", "eat", "rain"],
                ),
            ),
            ["eat", "oath"],
            nested_set_compare,
        ),
        TestCase("single", (([["a"]], ["a"]),), ["a"]),
        TestCase("not found", (([["a", "b"]], ["c"]),), []),
        TestCase("empty words list", (([["a", "b"], ["c", "d"]], []),), []),
        TestCase(
            "overlapping words",
            (([["a", "b"], ["c", "d"]], ["ab", "abc", "abcd"]),),
            ["ab"],
            nested_set_compare,
        ),
    ],
    "generate_parentheses": [
        TestCase(
            "n=3", ((3,),), ["((()))", "(()())", "(())()", "()(())", "()()()"], nested_set_compare
        ),
        TestCase("n=1", ((1,),), ["()"]),
        TestCase("n=2", ((2,),), ["(())", "()()"], nested_set_compare),
        TestCase(
            "n=4",
            ((4,),),
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ],
            nested_set_compare,
        ),
    ],
    "restore_ip_addresses": [
        TestCase(
            "basic", (("25525511135",),), ["255.255.11.135", "255.255.111.35"], nested_set_compare
        ),
        TestCase("zeros", (("0000",),), ["0.0.0.0"]),
        TestCase("invalid", (("1111111111111",),), []),
        TestCase("too short", (("123",),), []),
        TestCase("single zeros", (("010010",),), ["0.10.0.10", "0.100.1.0"], nested_set_compare),
        TestCase("min length", (("1111",),), ["1.1.1.1"]),
    ],
    "expression_add_operators": [
        TestCase("basic", (("123", 6),), ["1+2+3", "1*2*3"], nested_set_compare),
        TestCase("with minus", (("232", 8),), ["2*3+2", "2+3*2"], nested_set_compare),
        TestCase("zeros", (("105", 5),), ["1*0+5", "10-5"], nested_set_compare),
        TestCase("single digit", (("5", 5),), ["5"], nested_set_compare),
        TestCase("no solution", (("123", 100),), []),
        TestCase("leading zeros", (("00", 0),), ["0+0", "0-0", "0*0"], nested_set_compare),
    ],
}
