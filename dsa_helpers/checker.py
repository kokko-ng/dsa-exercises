"""
Test checker for DSA exercises.

Provides the check() function that runs pytest tests for user implementations
and displays formatted results in Jupyter notebooks.
"""

import subprocess
import sys
import re
import os
from pathlib import Path
from typing import Callable, Union, Optional

try:
    from IPython.display import display, HTML
    HAS_IPYTHON = True
except ImportError:
    HAS_IPYTHON = False


# Cache for function -> test file mapping
_FUNCTION_TEST_MAP: Optional[dict] = None


def _get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent


def _load_function_map() -> dict:
    """Lazily load mapping of function names to test file paths."""
    global _FUNCTION_TEST_MAP
    if _FUNCTION_TEST_MAP is not None:
        return _FUNCTION_TEST_MAP

    _FUNCTION_TEST_MAP = {}
    tests_dir = _get_project_root() / "tests"

    for test_file in tests_dir.rglob("test_*.py"):
        # Extract function name from test file (e.g., test_p01_two_sum.py -> two_sum)
        match = re.match(r"test_p\d+_(.+)\.py", test_file.name)
        if match:
            func_name = match.group(1)
            _FUNCTION_TEST_MAP[func_name] = str(test_file)

    return _FUNCTION_TEST_MAP


def _display_html(html: str) -> None:
    """Display HTML in notebook or print for terminal."""
    if HAS_IPYTHON:
        display(HTML(html))
    else:
        # Strip HTML tags for terminal output
        text = re.sub(r'<[^>]+>', '', html)
        text = text.replace('&#x2705;', '[PASS]')
        text = text.replace('&#x274C;', '[FAIL]')
        text = text.replace('&#x1F4A1;', '[TIP]')
        text = text.replace('&#x1F680;', '[PERF]')
        text = text.replace('&nbsp;', ' ')
        print(text)


def _extract_failure_info(output: str) -> str:
    """Extract relevant failure information from pytest output."""
    lines = output.split('\n')
    relevant_lines = []
    capture = False

    for line in lines:
        # Start capturing on assertion errors or FAILED lines
        if 'AssertionError' in line or 'assert ' in line or 'FAILED' in line:
            capture = True
        if capture:
            clean_line = line.rstrip()
            if clean_line and not clean_line.startswith('='):
                # Escape HTML characters
                clean_line = clean_line.replace('&', '&amp;')
                clean_line = clean_line.replace('<', '&lt;')
                clean_line = clean_line.replace('>', '&gt;')
                relevant_lines.append(clean_line)
        if 'short test summary' in line.lower():
            break

    return '\n'.join(relevant_lines[:15])  # Limit output


def _display_results(func_name: str, result: subprocess.CompletedProcess,
                     verbose: bool, performance: bool) -> None:
    """Format and display test results in notebook-friendly format."""

    passed = result.returncode == 0
    output = result.stdout + result.stderr

    # Count tests from output
    passed_count = len(re.findall(r"PASSED", output))
    failed_count = len(re.findall(r"FAILED", output))
    total = passed_count + failed_count

    if total == 0:
        # No tests ran - check for errors
        html = f"""
        <div style="padding: 15px; background: #fff3cd; border-left: 4px solid #ffc107;
                    margin: 10px 0; border-radius: 4px;">
            <div style="font-size: 18px; margin-bottom: 8px;">
                &#x26A0; <strong style="color: #856404;">No tests found or error occurred</strong>
            </div>
            <div style="color: #856404;">
                Make sure your function <code>{func_name}</code> is correctly defined.
            </div>
            <pre style="margin-top: 10px; padding: 10px; background: #fff; border-radius: 4px;
                        font-size: 12px; overflow-x: auto; color: #333;">{output[:500]}</pre>
        </div>
        """
        _display_html(html)
        return

    if passed:
        # Success display
        perf_msg = ""
        if performance:
            perf_msg = """<div style='margin-top: 8px; color: #155724;'>
                &#x1F680; Performance tests passed!</div>"""

        html = f"""
        <div style="padding: 15px; background: #d4edda; border-left: 4px solid #28a745;
                    margin: 10px 0; border-radius: 4px;">
            <div style="font-size: 18px; margin-bottom: 8px;">
                &#x2705; <strong style="color: #28a745;">All tests passed!</strong>
            </div>
            <div style="color: #155724;">
                <code>{func_name}</code>: {passed_count}/{total} tests passed
            </div>
            {perf_msg}
        </div>
        """
    else:
        # Failure display
        failure_info = _extract_failure_info(output)

        html = f"""
        <div style="padding: 15px; background: #f8d7da; border-left: 4px solid #dc3545;
                    margin: 10px 0; border-radius: 4px;">
            <div style="font-size: 18px; margin-bottom: 8px;">
                &#x274C; <strong style="color: #dc3545;">Tests failed</strong>
            </div>
            <div style="color: #721c24;">
                <code>{func_name}</code>: {passed_count}/{total} tests passed
            </div>
            <div style="margin-top: 10px; padding: 10px; background: #fff; border-radius: 4px;
                        font-family: monospace; font-size: 13px; white-space: pre-wrap;
                        color: #333; max-height: 300px; overflow-y: auto;">
{failure_info}
            </div>
            <div style="margin-top: 10px; color: #721c24; font-size: 13px;">
                &#x1F4A1; Tip: Use <code>hint("{func_name}")</code> for guidance
            </div>
        </div>
        """

    _display_html(html)

    if verbose:
        print("\n--- Full Test Output ---")
        print(output)


def check(function_or_name: Union[Callable, str], *,
          verbose: bool = False,
          performance: bool = False) -> bool:
    """
    Run tests for a given function and display results in the notebook.

    Args:
        function_or_name: Either a function object or string function name
        verbose: Show detailed test output
        performance: Run performance tests (if available)

    Returns:
        True if all tests passed, False otherwise

    Usage:
        check(two_sum)
        check("two_sum")
        check(two_sum, performance=True)
        check(two_sum, verbose=True)
    """
    # Handle both function objects and string names
    if callable(function_or_name):
        func_name = function_or_name.__name__
        func_obj = function_or_name
    else:
        func_name = str(function_or_name)
        func_obj = None

    # Register the function if provided as object
    if func_obj is not None:
        from . import _function_registry
        _function_registry.register(func_name, func_obj)

    # Find test file
    func_map = _load_function_map()

    if func_name not in func_map:
        html = f"""
        <div style="padding: 10px; background: #fee; border-left: 4px solid #c00; margin: 10px 0;">
            <strong style="color: #c00;">Error:</strong> No tests found for function '{func_name}'
        </div>
        """
        _display_html(html)
        return False

    test_file = func_map[func_name]
    project_root = _get_project_root()

    # Build pytest command
    cmd = [
        sys.executable, "-m", "pytest",
        test_file,
        "-v" if verbose else "-q",
        "--tb=short",
        "--no-header",
        "-x",  # Stop on first failure for faster feedback
    ]

    if performance:
        cmd.extend(["-m", "performance"])
    else:
        cmd.extend(["-m", "not performance"])

    # Run pytest as subprocess
    env = os.environ.copy()
    env['PYTHONPATH'] = str(project_root) + os.pathsep + env.get('PYTHONPATH', '')

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(project_root),
        env=env
    )

    # Parse and format output
    _display_results(func_name, result, verbose, performance)

    return result.returncode == 0


def check_all(category: Optional[str] = None, *, performance: bool = False) -> dict:
    """
    Run tests for all functions, optionally filtered by category.

    Args:
        category: Category name to filter (e.g., "01_array_string")
        performance: Include performance tests

    Returns:
        Dict mapping function names to pass/fail status
    """
    func_map = _load_function_map()
    results = {}

    for func_name, test_file in func_map.items():
        if category and category not in test_file:
            continue

        # Simple pass/fail check without display
        project_root = _get_project_root()
        cmd = [
            sys.executable, "-m", "pytest",
            test_file,
            "-q",
            "--tb=no",
        ]

        if not performance:
            cmd.extend(["-m", "not performance"])

        env = os.environ.copy()
        env['PYTHONPATH'] = str(project_root) + os.pathsep + env.get('PYTHONPATH', '')

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(project_root),
            env=env
        )

        results[func_name] = result.returncode == 0

    return results
