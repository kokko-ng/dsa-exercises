"""
Pytest configuration and shared fixtures for DSA exercises.

This module provides:
- Common fixtures for data structures
- Utility functions for converting between formats
- Shared test helpers
"""

import pytest
import sys
from pathlib import Path
from typing import Optional, List

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import data structures
from dsa_helpers.data_structures import (
    TreeNode, ListNode, DoublyListNode, GraphNode, Interval
)

# Import function registry
from dsa_helpers._function_registry import get as get_function


# =============================================================================
# Linked List Utilities
# =============================================================================

def list_to_linked_list(values: List[int]) -> Optional[ListNode]:
    """Convert Python list to linked list."""
    return ListNode.from_list(values)


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Convert linked list to Python list."""
    if head is None:
        return []
    return head.to_list()


def create_linked_list_with_cycle(values: List[int], pos: int) -> Optional[ListNode]:
    """
    Create a linked list with a cycle.

    Args:
        values: List values
        pos: Position where tail connects to (0-indexed), -1 for no cycle

    Returns:
        Head of the linked list
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = head if pos == 0 else None

    for i, val in enumerate(values[1:], 1):
        current.next = ListNode(val)
        current = current.next
        if i == pos:
            cycle_node = current

    if pos >= 0 and cycle_node:
        current.next = cycle_node

    return head


# =============================================================================
# Tree Utilities
# =============================================================================

def list_to_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Convert level-order list to binary tree."""
    return TreeNode.from_list(values)


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Convert binary tree to level-order list."""
    if root is None:
        return []
    return root.to_list()


def trees_equal(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
    """Check if two trees are equal."""
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return t1 == t2


def tree_paths(root: Optional[TreeNode]) -> List[List[int]]:
    """Get all root-to-leaf paths as lists."""
    if root is None:
        return []

    paths = []

    def dfs(node: TreeNode, path: List[int]):
        path.append(node.val)
        if not node.left and not node.right:
            paths.append(path.copy())
        else:
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
        path.pop()

    dfs(root, [])
    return paths


# =============================================================================
# Graph Utilities
# =============================================================================

def adjacency_list_to_graph(adj_list: List[List[int]]) -> Optional[GraphNode]:
    """Convert adjacency list to graph."""
    return GraphNode.from_adjacency_list(adj_list)


def graph_to_adjacency_list(node: Optional[GraphNode]) -> List[List[int]]:
    """Convert graph to adjacency list using BFS."""
    if node is None:
        return []

    visited = {}
    queue = [node]
    visited[node.val] = node

    while queue:
        current = queue.pop(0)
        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = neighbor
                queue.append(neighbor)

    max_val = max(visited.keys()) if visited else 0
    result = [[] for _ in range(max_val)]

    for val, n in visited.items():
        if val <= len(result):
            result[val - 1] = [neighbor.val for neighbor in n.neighbors]

    return result


# =============================================================================
# Interval Utilities
# =============================================================================

def lists_to_intervals(intervals: List[List[int]]) -> List[Interval]:
    """Convert list of lists to list of Intervals."""
    return Interval.from_list(intervals)


def intervals_to_lists(intervals: List[Interval]) -> List[List[int]]:
    """Convert list of Intervals to list of lists."""
    return Interval.to_list(intervals)


# =============================================================================
# Sample Data Fixtures
# =============================================================================

@pytest.fixture
def sample_linked_list():
    """Sample linked list: 1 -> 2 -> 3 -> 4 -> 5"""
    return ListNode.from_list([1, 2, 3, 4, 5])


@pytest.fixture
def sample_tree():
    """
    Sample binary tree:
           1
          / \
         2   3
        / \
       4   5
    """
    return TreeNode.from_list([1, 2, 3, 4, 5])


@pytest.fixture
def sample_bst():
    """
    Sample BST:
           4
          / \
         2   6
        / \ / \
       1  3 5  7
    """
    return TreeNode.from_list([4, 2, 6, 1, 3, 5, 7])


@pytest.fixture
def empty_tree():
    """Empty tree (None)."""
    return None


@pytest.fixture
def single_node_tree():
    """Single node tree."""
    return TreeNode(1)


@pytest.fixture
def sample_intervals():
    """Sample intervals: [[1,3], [2,6], [8,10], [15,18]]"""
    return [[1, 3], [2, 6], [8, 10], [15, 18]]


# =============================================================================
# Make utilities available globally
# =============================================================================

# Attach utilities to pytest namespace for easy access in tests
pytest.list_to_linked_list = list_to_linked_list
pytest.linked_list_to_list = linked_list_to_list
pytest.create_linked_list_with_cycle = create_linked_list_with_cycle
pytest.list_to_tree = list_to_tree
pytest.tree_to_list = tree_to_list
pytest.trees_equal = trees_equal
pytest.tree_paths = tree_paths
pytest.adjacency_list_to_graph = adjacency_list_to_graph
pytest.graph_to_adjacency_list = graph_to_adjacency_list
pytest.lists_to_intervals = lists_to_intervals
pytest.intervals_to_lists = intervals_to_lists

# Re-export data structures for tests
pytest.ListNode = ListNode
pytest.TreeNode = TreeNode
pytest.DoublyListNode = DoublyListNode
pytest.GraphNode = GraphNode
pytest.Interval = Interval
pytest.get_function = get_function
