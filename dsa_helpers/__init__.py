"""
DSA Helpers - Utilities for DSA exercises.

This package provides helper functions and data structures for
algorithm practice exercises.

Usage:
    from dsa_helpers import check, hint
    from dsa_helpers.data_structures import TreeNode, ListNode

Functions:
    check(func): Run tests for a function and display results
    hint(name): Display progressive hints for a problem
    list_problems(): List all available problems
    show_problems(): Display problems in formatted table

Data Structures:
    ListNode: Singly linked list node
    DoublyListNode: Doubly linked list node
    TreeNode: Binary tree node
    GraphNode: Graph adjacency list node
    TrieNode: Trie/prefix tree node
    Trie: Complete trie implementation
    UnionFind: Disjoint set union
    Interval: Interval representation
"""

from .checker import check, check_all
from .hints import hint, list_problems, show_problems, reset_all_hints, reload_hints
from .data_structures import (
    ListNode,
    DoublyListNode,
    TreeNode,
    GraphNode,
    TrieNode,
    Trie,
    UnionFind,
    Interval,
)

__all__ = [
    # Functions
    'check',
    'check_all',
    'hint',
    'list_problems',
    'show_problems',
    'reset_all_hints',
    'reload_hints',
    # Data structures
    'ListNode',
    'DoublyListNode',
    'TreeNode',
    'GraphNode',
    'TrieNode',
    'Trie',
    'UnionFind',
    'Interval',
]

__version__ = '0.1.0'
