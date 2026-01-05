# DSA Algorithm Exercises

A comprehensive collection of 203 algorithm problems organized by pattern, with Jupyter notebooks, hidden tests, and progressive hints.

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## Usage

### In Jupyter Notebook

```python
# Import helpers
from dsa_helpers import check, hint
from dsa_helpers.data_structures import ListNode, TreeNode

# Write your solution
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

# Check your solution
check(two_sum)

# Get hints if stuck (call multiple times for more hints)
hint("two_sum")
```

### Helper Functions

| Function | Description |
|----------|-------------|
| `check(func)` | Run tests for your solution |
| `check(func, verbose=True)` | Show detailed test output |
| `check(func, performance=True)` | Run performance tests |
| `hint("problem")` | Get progressive hints (3 levels) |
| `hint("problem", reset=True)` | Reset hints and start over |
| `show_problems()` | List all available problems |

### Data Structures

```python
from dsa_helpers.data_structures import (
    ListNode,        # Singly linked list
    DoublyListNode,  # Doubly linked list
    TreeNode,        # Binary tree
    GraphNode,       # Graph node
    TrieNode,        # Trie node
    UnionFind,       # Disjoint set
    Interval,        # Interval [start, end]
)

# Create from list
head = ListNode.from_list([1, 2, 3, 4, 5])
root = TreeNode.from_list([1, 2, 3, None, 4])

# Convert back
values = head.to_list()  # [1, 2, 3, 4, 5]
```

## Categories

| # | Category | Problems |
|---|----------|----------|
| 01 | Array & String Manipulation | 15 |
| 02 | Hash Map Patterns | 12 |
| 03 | Two Pointers & Sliding Window | 15 |
| 04 | Fast & Slow Pointers | 8 |
| 05 | Merge Intervals | 10 |
| 06 | Cyclic Sort | 8 |
| 07 | Linked List In-Place Reversal | 10 |
| 08 | Tree BFS & DFS | 15 |
| 09 | Two Heaps | 8 |
| 10 | Subsets & Permutations | 10 |
| 11 | Modified Binary Search | 12 |
| 12 | Top K Elements | 10 |
| 13 | K-Way Merge | 8 |
| 14 | Graph Patterns | 15 |
| 15 | Dynamic Programming | 25 |
| 16 | Backtracking | 12 |
| 17 | Monotonic Stack/Queue | 10 |
| 18 | Bit Manipulation | 10 |
| | **Total** | **203** |

## Project Structure

```
dsa-exercises/
├── notebooks/          # Jupyter notebooks (one per category)
├── hints/              # Progressive hints in YAML
├── dsa_helpers/        # Helper package
│   ├── checker.py      # check() function with inline tests
│   ├── test_cases.py   # Test case definitions
│   ├── comparators.py  # Result comparison functions
│   ├── hints.py        # hint() function
│   └── data_structures.py
└── README.md
```

## Recommended Order

1. Start with **01_array_string** - foundational patterns
2. Continue with **02_hash_map** and **03_two_pointers** - core techniques
3. Work through remaining categories in order
4. Categories are ordered by increasing conceptual complexity
5. Problems within each category progress from easier to harder

## Tips

- Read the problem description carefully before coding
- Consider edge cases (empty input, single element, duplicates)
- Use `hint()` when stuck - hints are designed to guide without spoiling
- Run performance tests to ensure optimal solutions
- Review the summary section at the end of each notebook
