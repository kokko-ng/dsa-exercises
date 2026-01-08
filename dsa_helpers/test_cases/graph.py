"""Test cases for Graph problems (Category 14)."""

from . import TestCase, set_compare, topological_order_compare, unordered_list_compare

GRAPH_TESTS: dict[str, list[TestCase]] = {
    "number_of_islands": [
        TestCase(
            "single island",
            (
                (
                    [
                        ["1", "1", "1", "1", "0"],
                        ["1", "1", "0", "1", "0"],
                        ["1", "1", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"],
                    ],
                ),
            ),
            1,
        ),
        TestCase(
            "three islands",
            (
                (
                    [
                        ["1", "1", "0", "0", "0"],
                        ["1", "1", "0", "0", "0"],
                        ["0", "0", "1", "0", "0"],
                        ["0", "0", "0", "1", "1"],
                    ],
                ),
            ),
            3,
        ),
        TestCase("no islands", (([["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]],),), 0),
        TestCase("all land", (([["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]],),), 1),
        TestCase("single cell land", (([["1"]],),), 1),
        TestCase("single cell water", (([["0"]],),), 0),
        TestCase("diagonal not connected", (([["1", "0"], ["0", "1"]],),), 2),
        TestCase("checkerboard", (([["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]],),), 5),
        TestCase("horizontal strip", (([["1", "1", "1", "1", "1"]],),), 1),
        TestCase("vertical strip", (([["1"], ["1"], ["1"], ["1"]],),), 1),
    ],
    "course_schedule": [
        TestCase("possible", ((2, [[1, 0]]),), True),
        TestCase("impossible", ((2, [[1, 0], [0, 1]]),), False),
        TestCase("no prereqs", ((3, []),), True),
        TestCase("chain", ((4, [[1, 0], [2, 1], [3, 2]]),), True),
        TestCase("complex cycle", ((3, [[0, 1], [1, 2], [2, 0]]),), False),
        TestCase("self loop", ((1, [[0, 0]]),), False),
        TestCase("multiple chains", ((5, [[1, 0], [2, 0], [3, 1], [4, 2]]),), True),
        TestCase("diamond", ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]),), True),
        TestCase("single course", ((1, []),), True),
    ],
    "course_schedule_ii": [
        TestCase("example 1", ((2, [[1, 0]]),), [0, 1]),
        TestCase(
            "example 2",
            ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]),),
            [0, 1, 2, 3],
            topological_order_compare,
        ),
        TestCase("no prereqs", ((3, []),), [0, 1, 2], set_compare),
        TestCase("cycle", ((2, [[1, 0], [0, 1]]),), []),
        TestCase("single", ((1, []),), [0]),
        TestCase("chain", ((4, [[1, 0], [2, 1], [3, 2]]),), [0, 1, 2, 3]),
        TestCase(
            "complex valid",
            ((6, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3]]),),
            [0, 1, 2, 3, 4, 5],
            topological_order_compare,
        ),
    ],
    "clone_graph": [
        # Test cases use adjacency list format: [[neighbors of node 1], [neighbors of node 2], ...]
        # The checker will convert these to Node objects and verify deep copy
        TestCase(
            "basic four nodes",
            (([[2, 4], [1, 3], [2, 4], [1, 3]],),),
            [[2, 4], [1, 3], [2, 4], [1, 3]],
        ),
        TestCase(
            "single node no neighbors",
            (
                (
                    [
                        [],
                    ],
                ),
            ),
            [[]],
        ),
        TestCase("two connected nodes", (([[2], [1]],),), [[2], [1]]),
        TestCase("empty graph", ((None,),), None),
        TestCase("triangle", (([[2, 3], [1, 3], [1, 2]],),), [[2, 3], [1, 3], [1, 2]]),
        TestCase("star graph", (([[2, 3, 4], [1], [1], [1]],),), [[2, 3, 4], [1], [1], [1]]),
    ],
    "pacific_atlantic_water": [
        TestCase(
            "example",
            (
                (
                    [
                        [1, 2, 2, 3, 5],
                        [3, 2, 3, 4, 4],
                        [2, 4, 5, 3, 1],
                        [6, 7, 1, 4, 5],
                        [5, 1, 1, 2, 4],
                    ],
                ),
            ),
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
            unordered_list_compare,
        ),
        TestCase("single cell", (([[1]],),), [[0, 0]], unordered_list_compare),
        TestCase("row", (([[1, 2, 3]],),), [[0, 0], [0, 1], [0, 2]], unordered_list_compare),
        TestCase("column", (([[1], [2], [3]],),), [[0, 0], [1, 0], [2, 0]], unordered_list_compare),
        TestCase(
            "all same",
            (([[5, 5], [5, 5]],),),
            [[0, 0], [0, 1], [1, 0], [1, 1]],
            unordered_list_compare,
        ),
        TestCase(
            "descending",
            (([[3, 2, 1], [2, 1, 0], [1, 0, 0]],),),
            [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0]],
            unordered_list_compare,
        ),
    ],
    "word_ladder": [
        TestCase("example 1", (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),), 5),
        TestCase("no path", (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),), 0),
        TestCase("short path", (("hot", "dog", ["hot", "dot", "dog"]),), 3),
        TestCase(
            "longer path", (("go", "sq", ["si", "go", "se", "cm", "so", "ph", "os", "sq"]),), 3
        ),
        TestCase("single char", (("a", "c", ["a", "b", "c"]),), 2),
        TestCase("direct transform", (("ab", "ac", ["ac"]),), 2),
        TestCase("begin not in list", (("hit", "hot", ["hot"]),), 2),
    ],
    "network_delay_time": [
        TestCase("example 1", (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2),), 2),
        TestCase("example 2", (([[1, 2, 1]], 2, 1),), 1),
        TestCase("unreachable", (([[1, 2, 1]], 2, 2),), -1),
        TestCase("single node", (([], 1, 1),), 0),
        TestCase("multiple paths", (([[1, 2, 1], [1, 3, 2], [2, 3, 1]], 3, 1),), 2),
        TestCase("cycle", (([[1, 2, 1], [2, 3, 1], [3, 1, 1]], 3, 1),), 2),
    ],
    "cheapest_flights": [
        TestCase(
            "example 1",
            ((4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1),),
            700,
        ),
        TestCase("example 2", ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1),), 200),
        TestCase("no stops", ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0),), 500),
        TestCase("unreachable", ((3, [[0, 1, 100]], 0, 2, 1),), -1),
        TestCase("direct flight", ((2, [[0, 1, 100]], 0, 1, 0),), 100),
        TestCase("k larger than needed", ((3, [[0, 1, 100], [1, 2, 100]], 0, 2, 5),), 200),
        TestCase("no flights", ((3, [], 0, 2, 1),), -1),
    ],
    "minimum_height_trees": [
        TestCase("example 1", ((4, [[1, 0], [1, 2], [1, 3]]),), [1]),
        TestCase(
            "example 2", ((6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]),), [3, 4], set_compare
        ),
        TestCase("single node", ((1, []),), [0]),
        TestCase("two nodes", ((2, [[0, 1]]),), [0, 1], set_compare),
        TestCase("line", ((5, [[0, 1], [1, 2], [2, 3], [3, 4]]),), [2]),
    ],
    "redundant_connection": [
        TestCase("example 1", (([[1, 2], [1, 3], [2, 3]],),), [2, 3]),
        TestCase("example 2", (([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],),), [1, 4]),
        TestCase("triangle", (([[1, 2], [2, 3], [1, 3]],),), [1, 3]),
        TestCase("last edge", (([[1, 2], [1, 3], [1, 4], [3, 4]],),), [3, 4]),
        TestCase("line with cycle", (([[1, 2], [2, 3], [3, 1]],),), [3, 1]),
    ],
    "alien_dictionary": [
        TestCase("basic", ((["wrt", "wrf", "er", "ett", "rftt"],),), "wertf"),
        TestCase("simple", ((["z", "x"],),), "zx"),
        TestCase("invalid", ((["z", "x", "z"],),), ""),
        TestCase("single word", ((["abc"],),), "abc", set_compare),
        TestCase("invalid prefix", ((["abc", "ab"],),), ""),
        TestCase("two chars", ((["ab", "ba"],),), "ab"),
    ],
    "all_paths_from_source": [
        TestCase(
            "example 1",
            (([[1, 2], [3], [3], []],),),
            [[0, 1, 3], [0, 2, 3]],
            unordered_list_compare,
        ),
        TestCase(
            "example 2",
            (([[4, 3, 1], [3, 2, 4], [3], [4], []],),),
            [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
            unordered_list_compare,
        ),
        TestCase("single path", (([[1], [2], []],),), [[0, 1, 2]]),
        TestCase("direct", (([[1], []],),), [[0, 1]]),
        TestCase("minimal two node", (([[1], []],),), [[0, 1]]),
        TestCase(
            "multiple branches",
            (([[1, 2, 3], [], [], []],),),
            [[0, 1], [0, 2], [0, 3]],
            unordered_list_compare,
        ),
    ],
    "critical_connections": [
        TestCase(
            "basic", ((4, [[0, 1], [1, 2], [2, 0], [1, 3]]),), [[1, 3]], unordered_list_compare
        ),
        TestCase("no bridges", ((3, [[0, 1], [1, 2], [2, 0]]),), []),
        TestCase("single edge", ((2, [[0, 1]]),), [[0, 1]], unordered_list_compare),
        TestCase(
            "multiple bridges",
            ((5, [[0, 1], [1, 2], [2, 3], [3, 4]]),),
            [[0, 1], [1, 2], [2, 3], [3, 4]],
            unordered_list_compare,
        ),
    ],
    "reconstruct_itinerary": [
        TestCase(
            "basic",
            (([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],),),
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
        ),
        TestCase(
            "multiple paths",
            (([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],),),
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        ),
        TestCase("single", (([["JFK", "A"]],),), ["JFK", "A"]),
    ],
    "word_ladder_ii": [
        TestCase(
            "basic",
            (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),),
            [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
            unordered_list_compare,
        ),
        TestCase("no path", (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),), []),
        TestCase("short path", (("hot", "dog", ["hot", "dot", "dog"]),), [["hot", "dot", "dog"]]),
    ],
}
