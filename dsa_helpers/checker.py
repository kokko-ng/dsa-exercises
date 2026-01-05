"""
Test checker for DSA exercises.

Provides the check() function that runs inline tests for user implementations
and displays formatted results in Jupyter notebooks. No pytest required.
"""

import re
import time
from typing import Any, Callable, Optional, Union

try:
    from IPython import get_ipython  # type: ignore[attr-defined]
    from IPython.display import HTML, display

    # Check if we're actually in an IPython/Jupyter environment
    HAS_IPYTHON = get_ipython() is not None  # type: ignore[no-untyped-call]
except ImportError:
    HAS_IPYTHON = False

from .test_cases import TEST_CASES, TestCase


class TestResult:
    """Result of running a test case."""

    __slots__ = ("name", "passed", "error_msg", "actual", "expected", "elapsed", "args")

    def __init__(
        self,
        name: str,
        passed: bool,
        error_msg: Optional[str] = None,
        actual: Any = None,
        expected: Any = None,
        elapsed: Optional[float] = None,
        args: Any = None,
    ) -> None:
        self.name = name
        self.passed = passed
        self.error_msg = error_msg
        self.actual = actual
        self.expected = expected
        self.elapsed = elapsed
        self.args = args


def _run_test(func: Callable[..., Any], test: TestCase) -> TestResult:
    """Run a single test case."""
    test_args = test.args[0]  # Capture the input arguments
    # Make a copy for functions that modify in-place
    test_args_copy = list(test_args) if test.check_modified_arg is not None else test_args

    try:
        start = time.time()

        # Handle class-based tests
        if test.is_class_test:
            # For class tests: args[0] = (init_args, method_names, method_args)
            init_args, method_names, method_args = test_args

            # Instantiate the class
            instance = func(*init_args)

            # Execute method calls and collect results
            actual = []
            for method_name, method_arg in zip(method_names, method_args):
                result = getattr(instance, method_name)(*method_arg)
                actual.append(result)
        else:
            actual = func(*test_args_copy)

        elapsed = time.time() - start

        # For in-place modifications, check the modified argument instead of return value
        if test.check_modified_arg is not None:
            actual = test_args_copy[test.check_modified_arg]

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
                elapsed=elapsed,
                args=test_args,
            )

        if passed:
            return TestResult(name=test.name, passed=True, elapsed=elapsed, args=test_args)
        else:
            return TestResult(
                name=test.name,
                passed=False,
                error_msg="Wrong answer",
                actual=actual,
                expected=test.expected,
                elapsed=elapsed,
                args=test_args,
            )
    except Exception as e:
        return TestResult(
            name=test.name, passed=False, error_msg=f"{type(e).__name__}: {str(e)}", args=test_args
        )


def _display_html(html: str) -> None:
    """Display HTML in notebook or print for terminal."""
    if HAS_IPYTHON:
        display(HTML(html))  # type: ignore[no-untyped-call]
    else:
        text = re.sub(r"<[^>]+>", "", html)
        text = text.replace("&#x2705;", "[PASS]")
        text = text.replace("&#x274C;", "[FAIL]")
        text = text.replace("&#x1F4A1;", "[TIP]")
        text = text.replace("&#x1F680;", "[PERF]")
        text = text.replace("&#x26A0;", "[WARN]")
        text = text.replace("&nbsp;", " ")
        print(text)


def _display_results(func_name: str, results: list[TestResult], performance: bool) -> None:
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

        def format_failure(fail: TestResult, index: Optional[int] = None) -> str:
            """Format a single test failure with detailed information."""
            lines = []
            if index is not None:
                lines.append(f"{'─' * 40}")
                lines.append(f"FAILED TEST #{index + 1}: {fail.name}")
            else:
                lines.append(f"Test: {fail.name}")
            lines.append("")

            # Show input arguments - this is critical for debugging
            if fail.args is not None:
                lines.append("Input:")
                if isinstance(fail.args, tuple) and len(fail.args) == 1:
                    lines.append(f"  {repr(fail.args[0])}")
                else:
                    for i, arg in enumerate(fail.args):
                        lines.append(f"  arg{i + 1}: {repr(arg)}")
                lines.append("")

            # Show error message
            if fail.error_msg:
                lines.append(f"Error: {fail.error_msg}")
                lines.append("")

            # Show actual vs expected
            if fail.actual is not None or fail.expected is not None:
                lines.append(f"Your output:     {repr(fail.actual)}")
                lines.append(f"Expected output: {repr(fail.expected)}")

            return "\n".join(lines)

        # Show all failed tests (limit to 5 to avoid overwhelming output)
        max_failures_to_show = 5
        failures_to_show = failed[:max_failures_to_show]

        if len(failed) == 1:
            error_details = format_failure(failed[0])
        else:
            error_parts = []
            for i, fail in enumerate(failures_to_show):
                error_parts.append(format_failure(fail, i))

            error_details = "\n\n".join(error_parts)

            if len(failed) > max_failures_to_show:
                error_details += f"\n\n{'─' * 40}\n... and {len(failed) - max_failures_to_show} more failed test(s)"

        error_details = error_details.replace("&", "&amp;")
        error_details = error_details.replace("<", "&lt;")
        error_details = error_details.replace(">", "&gt;")

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
                        color: #333; max-height: 400px; overflow-y: auto;">
{error_details}
            </div>
            <div style="margin-top: 10px; color: #721c24; font-size: 13px;">
                &#x1F4A1; Tip: Use <code>hint("{func_name}")</code> for guidance
            </div>
        </div>
        """

    _display_html(html)


def check(
    function_or_name: Union[Callable[..., Any], str],
    *,
    verbose: bool = False,
    performance: bool = False,
) -> bool:
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
                print(f" ({result.elapsed * 1000:.1f}ms)")
            else:
                print()
            if not result.passed:
                if result.args is not None:
                    print(f"    Input: {repr(result.args)}")
                if result.error_msg:
                    print(f"    Error: {result.error_msg}")
                if result.actual is not None or result.expected is not None:
                    print(f"    Got:      {repr(result.actual)}")
                    print(f"    Expected: {repr(result.expected)}")

    _display_results(func_name, results, performance)

    return all(r.passed for r in results)


def check_all(
    category: Optional[str] = None, *, performance: bool = False
) -> dict[str, Optional[bool]]:
    """
    Run tests for all functions, optionally filtered by category.

    Args:
        category: Function name prefix to filter (e.g., "two_sum")
        performance: Include performance tests

    Returns:
        Dict mapping function names to pass/fail status
    """
    from . import _function_registry

    results: dict[str, Optional[bool]] = {}

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


def list_available_functions() -> list[str]:
    """Return a list of all functions that have test cases defined."""
    return sorted(TEST_CASES.keys())
