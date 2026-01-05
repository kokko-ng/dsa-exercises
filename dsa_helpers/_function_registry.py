"""
Function registry for storing user implementations from notebooks.

This module provides a mechanism to register functions defined in Jupyter notebooks
so they can be accessed by the inline test runner.
"""

import inspect
import json
import os
import tempfile
from typing import Any, Callable, Optional

# Registry file location
_REGISTRY_FILE = os.path.join(tempfile.gettempdir(), "dsa_func_registry.json")


def _load_registry() -> dict:
    """Load the function registry from disk."""
    try:
        if os.path.exists(_REGISTRY_FILE):
            with open(_REGISTRY_FILE) as f:
                return json.load(f)
    except (OSError, json.JSONDecodeError):
        pass
    return {}


def _save_registry(registry: dict) -> None:
    """Save the function registry to disk."""
    try:
        with open(_REGISTRY_FILE, 'w') as f:
            json.dump(registry, f)
    except OSError:
        pass


def register(name: str, func: Callable) -> None:
    """
    Register a function for testing.

    Args:
        name: The function name (used as key)
        func: The function object to register
    """
    registry = _load_registry()

    # Store function source code
    try:
        source = inspect.getsource(func)
    except (OSError, TypeError):
        # If we can't get source, try to reconstruct from bytecode
        # This is a fallback for functions defined in notebooks
        source = None

    registry[name] = {
        'source': source,
        'name': name,
    }

    _save_registry(registry)


def get(name: str) -> Optional[Callable]:
    """
    Retrieve a registered function by name.

    Args:
        name: The function name to retrieve

    Returns:
        The function object, or None if not found
    """
    registry = _load_registry()

    if name not in registry:
        return None

    func_info = registry[name]
    source = func_info.get('source')

    if source is None:
        return None

    # Reconstruct function from source
    # Create a namespace with common imports
    local_ns: dict = {}
    global_ns = {
        '__builtins__': __builtins__,
        'Optional': Optional,
        'List': list,
        'Dict': dict,
        'Any': Any,
    }

    # Add data structures to namespace
    try:
        from .data_structures import (
            DoublyListNode,
            GraphNode,
            Interval,
            ListNode,
            TreeNode,
            Trie,
            TrieNode,
            UnionFind,
        )
        global_ns.update({
            'ListNode': ListNode,
            'TreeNode': TreeNode,
            'DoublyListNode': DoublyListNode,
            'GraphNode': GraphNode,
            'TrieNode': TrieNode,
            'Trie': Trie,
            'UnionFind': UnionFind,
            'Interval': Interval,
        })
    except ImportError:
        pass

    try:
        exec(source, global_ns, local_ns)
        return local_ns.get(func_info['name'])
    except Exception:
        return None


def clear(name: Optional[str] = None) -> None:
    """
    Clear registered function(s).

    Args:
        name: Function name to clear, or None to clear all
    """
    if name is None:
        # Clear entire registry
        try:
            if os.path.exists(_REGISTRY_FILE):
                os.remove(_REGISTRY_FILE)
        except OSError:
            pass
    else:
        registry = _load_registry()
        if name in registry:
            del registry[name]
            _save_registry(registry)


def list_registered() -> list:
    """List all registered function names."""
    registry = _load_registry()
    return list(registry.keys())
