"""Data structure helpers for DSA exercises.

Provides common data structures used across algorithm problems:
- ListNode: Singly linked list
- DoublyListNode: Doubly linked list
- TreeNode: Binary tree
- GraphNode: Graph adjacency list
- TrieNode: Prefix tree
- UnionFind: Disjoint set union
- Interval: Interval representation
"""

from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        """String representation showing the list."""
        values = []
        node: Optional[ListNode] = self
        seen = set()
        while node and id(node) not in seen:
            values.append(str(node.val))
            seen.add(id(node))
            node = node.next
        if node:
            values.append(f"... (cycle to {node.val})")
        return " -> ".join(values)

    def __eq__(self, other: object) -> bool:
        """Compare two linked lists by value (cycle-safe).

        Note: For cycle detection problems, use 'is' to check object identity,
        not '==' which compares list contents.
        """
        if not isinstance(other, ListNode):
            return False
        # For identity check (same object), return True
        if self is other:
            return True
        # For value comparison, traverse with cycle detection
        a: Optional[ListNode] = self
        b: Optional[ListNode] = other
        seen_a: set[int] = set()
        seen_b: set[int] = set()
        while a and b:
            if a.val != b.val:
                return False
            if id(a) in seen_a or id(b) in seen_b:
                # Cycle detected, compare by remaining structure
                # If both have cycles at this point, consider them equal
                return id(a) in seen_a and id(b) in seen_b
            seen_a.add(id(a))
            seen_b.add(id(b))
            a, b = a.next, b.next
        return a is None and b is None

    @classmethod
    def from_list(cls, values: list[int]) -> Optional["ListNode"]:
        """Create linked list from Python list."""
        if not values:
            return None
        head = cls(values[0])
        current = head
        for val in values[1:]:
            current.next = cls(val)
            current = current.next
        return head

    def to_list(self) -> list[int]:
        """Convert linked list to Python list."""
        result = []
        node: Optional[ListNode] = self
        seen = set()
        while node and id(node) not in seen:
            result.append(node.val)
            seen.add(id(node))
            node = node.next
        return result


class DoublyListNode:
    """Doubly linked list node."""

    def __init__(
        self,
        val: int = 0,
        prev: Optional["DoublyListNode"] = None,
        next: Optional["DoublyListNode"] = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        """String representation showing the list."""
        values = []
        node: Optional[DoublyListNode] = self
        seen = set()
        while node and id(node) not in seen:
            values.append(str(node.val))
            seen.add(id(node))
            node = node.next
        return " <-> ".join(values)

    @classmethod
    def from_list(cls, values: list[int]) -> Optional["DoublyListNode"]:
        """Create doubly linked list from Python list."""
        if not values:
            return None
        head = cls(values[0])
        current = head
        for val in values[1:]:
            new_node = cls(val, prev=current)
            current.next = new_node
            current = new_node
        return head

    def to_list(self) -> list[int]:
        """Convert doubly linked list to Python list."""
        result = []
        node: Optional[DoublyListNode] = self
        seen = set()
        while node and id(node) not in seen:
            result.append(node.val)
            seen.add(id(node))
            node = node.next
        return result


class TreeNode:
    """Binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
        next: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next  # Used for level-order sibling connection problems

    def __repr__(self) -> str:
        """Simple string representation."""
        return f"TreeNode({self.val})"

    def __eq__(self, other: object) -> bool:
        """Compare two trees."""
        if other is None:
            return False
        if not isinstance(other, TreeNode):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

    @classmethod
    def from_list(cls, values: list[Optional[int]]) -> Optional["TreeNode"]:
        """Create tree from level-order list (LeetCode format).

        Example: [1, 2, 3, None, 4] creates:
                1
               / \
              2   3
               \
                4
        """
        if not values or values[0] is None:
            return None
        assert values[0] is not None  # for type checker
        root = cls(values[0])
        queue: list[TreeNode] = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            # Left child
            if i < len(values) and values[i] is not None:
                left_val = values[i]
                assert left_val is not None  # for type checker
                node.left = cls(left_val)
                queue.append(node.left)
            i += 1
            # Right child
            if i < len(values) and values[i] is not None:
                right_val = values[i]
                assert right_val is not None  # for type checker
                node.right = cls(right_val)
                queue.append(node.right)
            i += 1
        return root

    def to_list(self) -> list[Optional[int]]:
        """Convert tree to level-order list."""
        result: list[Optional[int]] = []
        queue: list[Optional[TreeNode]] = [self]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing Nones
        while result and result[-1] is None:
            result.pop()
        return result

    def pretty_print(self, level: int = 0, prefix: str = "Root: ") -> None:
        """Print tree in a readable format."""
        print(" " * (level * 4) + prefix + str(self.val))
        if self.left:
            self.left.pretty_print(level + 1, "L--- ")
        if self.right:
            self.right.pretty_print(level + 1, "R--- ")


class GraphNode:
    """Graph node for adjacency list representation."""

    def __init__(self, val: int = 0, neighbors: Optional[list["GraphNode"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        """String representation showing node and neighbors."""
        neighbor_vals = [n.val for n in self.neighbors]
        return f"GraphNode({self.val}, neighbors={neighbor_vals})"

    @classmethod
    def from_adjacency_list(cls, adj_list: list[list[int]]) -> Optional["GraphNode"]:
        """Create graph from adjacency list.

        adj_list[i] contains neighbors of node i (1-indexed in typical problems).
        Returns the node with value 1.
        """
        if not adj_list:
            return None

        # Create all nodes
        nodes: dict[int, GraphNode] = {}
        for i in range(len(adj_list)):
            nodes[i + 1] = cls(i + 1)

        # Connect neighbors
        for i, neighbors in enumerate(adj_list):
            nodes[i + 1].neighbors = [nodes[n] for n in neighbors if n in nodes]

        return nodes.get(1)


class TrieNode:
    """Trie (prefix tree) node."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False
        self.word: Optional[str] = None

    def __repr__(self) -> str:
        """String representation showing children keys and end status."""
        return f"TrieNode(children={list(self.children.keys())}, is_end={self.is_end})"


class Trie:
    """Complete Trie implementation for reference."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.word = word

    def search(self, word: str) -> bool:
        """Check if word exists in trie."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Check if any word starts with prefix."""
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        """Find node for given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of components

    def find(self, x: int) -> int:
        """Find with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union by rank. Returns True if union was performed."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same component."""
        return self.find(x) == self.find(y)

    def get_count(self) -> int:
        """Return number of disjoint components."""
        return self.count


class Interval:
    """Interval representation for interval problems."""

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        """String representation in [start, end] format."""
        return f"[{self.start}, {self.end}]"

    def __eq__(self, other: object) -> bool:
        """Compare interval with another Interval, list, or tuple."""
        if isinstance(other, Interval):
            return self.start == other.start and self.end == other.end
        if isinstance(other, (list, tuple)) and len(other) == 2:
            return bool(self.start == other[0] and self.end == other[1])
        return False

    def __lt__(self, other: "Interval") -> bool:
        """For sorting by start time."""
        return self.start < other.start

    def overlaps(self, other: "Interval") -> bool:
        """Check if this interval overlaps with another."""
        return self.start <= other.end and other.start <= self.end

    def merge(self, other: "Interval") -> "Interval":
        """Merge two overlapping intervals."""
        return Interval(min(self.start, other.start), max(self.end, other.end))

    @classmethod
    def from_list(cls, intervals: list[list[int]]) -> list["Interval"]:
        """Convert list of lists to list of Intervals."""
        return [cls(i[0], i[1]) for i in intervals]

    @staticmethod
    def to_list(intervals: list["Interval"]) -> list[list[int]]:
        """Convert list of Intervals to list of lists."""
        return [[i.start, i.end] for i in intervals]
