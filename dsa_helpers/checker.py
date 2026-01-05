"""
Test checker for DSA exercises.

Provides the check() function that runs inline tests for user implementations
and displays formatted results in Jupyter notebooks. No pytest required.
"""

import re
import time
from typing import Callable, Union, Optional, List

try:
    from IPython.display import display, HTML
    HAS_IPYTHON = True
except ImportError:
    HAS_IPYTHON = False

from .test_cases import TestCase, TEST_CASES


class TestResult:
    """Result of running a test case."""
    __slots__ = ('name', 'passed', 'error_msg', 'actual', 'expected', 'elapsed')

    def __init__(self, name: str, passed: bool, error_msg: Optional[str] = None,
                 actual=None, expected=None, elapsed: Optional[float] = None):
        self.name = name
        self.passed = passed
        self.error_msg = error_msg
        self.actual = actual
        self.expected = expected
        self.elapsed = elapsed


def _run_test(func: Callable, test: TestCase) -> TestResult:
    """Run a single test case."""
    try:
        start = time.time()
        actual = func(*test.args[0])
        elapsed = time.time() - start

        # Check result
        if test.comparator:
            passed = test.comparator(actual, test.expected)
        elif test.expected is None:
            # Skip comparison for tests with None expected (multiple valid answers)
            passed = True
        else:
            passed = actual == test.expected

        # Check performance constraint
        if passed and test.max_time and elapsed > test.max_time:
            return TestResult(
                name=test.name,
                passed=False,
                error_msg=f"Too slow: {elapsed:.2f}s (max: {test.max_time}s)",
                actual=actual,
                expected=test.expected,
                elapsed=elapsed
            )

        if passed:
            return TestResult(name=test.name, passed=True, elapsed=elapsed)
        else:
            return TestResult(
                name=test.name,
                passed=False,
                error_msg="Wrong answer",
                actual=actual,
                expected=test.expected,
                elapsed=elapsed
            )
    except Exception as e:
        return TestResult(
            name=test.name,
            passed=False,
            error_msg=f"{type(e).__name__}: {str(e)}"
        )


def _display_html(html: str) -> None:
    """Display HTML in notebook or print for terminal."""
    if HAS_IPYTHON:
        display(HTML(html))
    else:
        text = re.sub(r'<[^>]+>', '', html)
        text = text.replace('&#x2705;', '[PASS]')
        text = text.replace('&#x274C;', '[FAIL]')
        text = text.replace('&#x1F4A1;', '[TIP]')
        text = text.replace('&#x1F680;', '[PERF]')
        text = text.replace('&#x26A0;', '[WARN]')
        text = text.replace('&nbsp;', ' ')
        print(text)


def _display_results(func_name: str, results: List[TestResult], performance: bool) -> None:
    """Format and display test results in notebook-friendly format."""
    passed_count = sum(1 for r in results if r.passed)
    total = len(results)
    all_passed = passed_count == total

    if total == 0:
        html = f"""
        <div style="padding: 15px; background: #fff3cd; border-left: 4px solid #ffc107;
                    margin: 10px 0; border-radius: 4px;">
            <div style="font-size: 18px; margin-bottom: 8px;">
                &#x26A0; <strong style="color: #856404;">No tests found</strong>
            </div>
            <div style="color: #856404;">
                No test cases defined for function <code>{func_name}</code>.
            </div>
        </div>
        """
        _display_html(html)
        return

    if all_passed:
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
        failed = [r for r in results if not r.passed]
        first_fail = failed[0]

        error_details = f"Test: {first_fail.name}\n"
        if first_fail.error_msg:
            error_details += f"Error: {first_fail.error_msg}\n"
        if first_fail.actual is not None:
            error_details += f"Got:      {repr(first_fail.actual)}\n"
        if first_fail.expected is not None:
            error_details += f"Expected: {repr(first_fail.expected)}"

        error_details = error_details.replace('&', '&amp;')
        error_details = error_details.replace('<', '&lt;')
        error_details = error_details.replace('>', '&gt;')

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
{error_details}
            </div>
            <div style="margin-top: 10px; color: #721c24; font-size: 13px;">
                &#x1F4A1; Tip: Use <code>hint("{func_name}")</code> for guidance
            </div>
        </div>
        """

    _display_html(html)


def check(function_or_name: Union[Callable, str], *,
          verbose: bool = False,
          performance: bool = False) -> bool:
    """
    Run tests for a given function and display results in the notebook.

    Args:
        function_or_name: Either a function object or string function name
        verbose: Show detailed test output for each test
        performance: Run performance tests (if available)

    Returns:
        True if all tests passed, False otherwise

    Usage:
        check(two_sum)
        check("two_sum")
        check(two_sum, performance=True)
        check(two_sum, verbose=True)
    """
    if callable(function_or_name):
        func_name = function_or_name.__name__
        func_obj = function_or_name
    else:
        func_name = str(function_or_name)
        func_obj = None

    if func_obj is None:
        from . import _function_registry
        func_obj = _function_registry.get(func_name)
        if func_obj is None:
            html = f"""
            <div style="padding: 10px; background: #fee; border-left: 4px solid #c00; margin: 10px 0;">
                <strong style="color: #c00;">Error:</strong> Function '{func_name}' not found.
                Make sure to pass the function directly: <code>check({func_name})</code>
            </div>
            """
            _display_html(html)
            return False
    else:
        from . import _function_registry
        _function_registry.register(func_name, func_obj)

    if func_name not in TEST_CASES:
        html = f"""
        <div style="padding: 10px; background: #fee; border-left: 4px solid #c00; margin: 10px 0;">
            <strong style="color: #c00;">Error:</strong> No tests found for function '{func_name}'
        </div>
        """
        _display_html(html)
        return False

    all_tests = TEST_CASES[func_name]

    if performance:
        tests = [t for t in all_tests if t.is_performance]
    else:
        tests = [t for t in all_tests if not t.is_performance]

    results = []
    for test in tests:
        result = _run_test(func_obj, test)
        results.append(result)

        if verbose:
            status = "✓" if result.passed else "✗"
            print(f"  {status} {test.name}", end="")
            if result.elapsed:
                print(f" ({result.elapsed*1000:.1f}ms)")
            else:
                print()
            if not result.passed and result.error_msg:
                print(f"    Error: {result.error_msg}")

    _display_results(func_name, results, performance)

    return all(r.passed for r in results)


def check_all(category: Optional[str] = None, *, performance: bool = False) -> dict:
    """
    Run tests for all functions, optionally filtered by category.

    Args:
        category: Function name prefix to filter (e.g., "two_sum")
        performance: Include performance tests

    Returns:
        Dict mapping function names to pass/fail status
    """
    from . import _function_registry

    results = {}

    for func_name in TEST_CASES:
        if category and category not in func_name:
            continue

        func_obj = _function_registry.get(func_name)

        if func_obj is None:
            results[func_name] = None
            continue

        all_tests = TEST_CASES[func_name]
        if performance:
            tests = [t for t in all_tests if t.is_performance]
        else:
            tests = [t for t in all_tests if not t.is_performance]

        test_results = [_run_test(func_obj, t) for t in tests]
        results[func_name] = all(r.passed for r in test_results)

    return results


def list_available_functions() -> List[str]:
    """Return a list of all functions that have test cases defined."""
    return sorted(TEST_CASES.keys())
