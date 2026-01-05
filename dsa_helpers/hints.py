"""
Progressive hint system for DSA exercises.

Provides the hint() function that displays progressive hints for problems,
helping users learn without giving away the complete solution.
"""

from collections import defaultdict
from pathlib import Path
from typing import Any, Optional

import yaml

try:
    from IPython.display import HTML, Markdown, display
    HAS_IPYTHON = True
except ImportError:
    HAS_IPYTHON = False


# Track hint progress per session
_hint_state: dict[str, int] = defaultdict(int)

# Cache for loaded hints
_hints_cache: Optional[dict[str, dict[str, Any]]] = None


def _get_hints_dir() -> Path:
    """Get the hints directory path."""
    return Path(__file__).parent.parent / "hints"


def _load_all_hints() -> dict[str, dict[str, Any]]:
    """Load all hints from YAML files."""
    global _hints_cache
    if _hints_cache is not None:
        return _hints_cache

    _hints_cache = {}
    hints_dir = _get_hints_dir()

    if not hints_dir.exists():
        return _hints_cache

    for yaml_file in hints_dir.glob("*.yaml"):
        try:
            with open(yaml_file, encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data:
                    _hints_cache.update(data)
        except (OSError, yaml.YAMLError):
            continue

    return _hints_cache


def _display_output(html: str, markdown: Optional[str] = None) -> None:
    """Display output in notebook or terminal."""
    if HAS_IPYTHON:
        display(HTML(html))  # type: ignore[no-untyped-call]
        if markdown:
            display(Markdown(markdown))  # type: ignore[no-untyped-call]
    else:
        # Strip HTML for terminal
        import re
        text = re.sub(r'<[^>]+>', '', html)
        text = text.replace('&#x1F4A1;', '[HINT]')
        text = text.replace('&#x1F527;', '[IMPL]')
        text = text.replace('&#x26A0;', '[EDGE]')
        text = text.replace('&#x27A1;', '->')
        text = text.replace('&nbsp;', ' ')
        print(text)
        if markdown:
            print(markdown)


def hint(problem_name: str, *, level: Optional[int] = None, reset: bool = False) -> None:
    """
    Display progressive hints for a problem.

    Hints are organized in 3 levels:
    - Level 1: Strategy/Approach - High-level thinking
    - Level 2: Implementation - Pseudocode and key steps
    - Level 3: Edge Cases - Common pitfalls and gotchas

    Args:
        problem_name: Name of the problem (e.g., "two_sum")
        level: Specific level to show (1, 2, or 3). If None, shows next level.
        reset: Reset hint progress for this problem

    Usage:
        hint("two_sum")           # Shows level 1, then 2, then 3 on subsequent calls
        hint("two_sum", level=2)  # Jump to specific level
        hint("two_sum", reset=True)  # Reset and show level 1
    """
    if reset:
        _hint_state[problem_name] = 0

    # Load hints
    all_hints = _load_all_hints()

    if problem_name not in all_hints:
        html = f"""
        <div style="padding: 10px; background: #fff3cd; border-left: 4px solid #ffc107; margin: 10px 0;">
            <strong style="color: #856404;">No hints available</strong> for '{problem_name}'
        </div>
        """
        _display_output(html)
        return

    hints_data = all_hints[problem_name]

    # Determine which level to show
    max_level = 3
    if level is not None:
        current_level = min(max(1, level), max_level)
        _hint_state[problem_name] = current_level
    else:
        _hint_state[problem_name] += 1
        current_level = min(_hint_state[problem_name], max_level)

    # Get hint content
    level_key = f"level_{current_level}"
    if level_key not in hints_data:
        html = f"""
        <div style="padding: 10px; background: #d4edda; border-left: 4px solid #28a745; margin: 10px 0;">
            <strong style="color: #155724;">All hints revealed!</strong>
            You've seen all available hints for '{problem_name}'.
        </div>
        """
        _display_output(html)
        return

    hint_info = hints_data[level_key]

    # Styling per level
    level_icons = {1: "&#x1F4A1;", 2: "&#x1F527;", 3: "&#x26A0;"}  # Lightbulb, Wrench, Warning
    level_colors = {1: "#17a2b8", 2: "#6f42c1", 3: "#fd7e14"}
    level_names = {1: "Strategy", 2: "Implementation", 3: "Edge Cases"}

    icon = level_icons.get(current_level, "&#x1F4A1;")
    color = level_colors.get(current_level, "#17a2b8")
    name = level_names.get(current_level, "Hint")
    title = hint_info.get('title', name)
    content = hint_info.get('content', '')

    # Build HTML
    html = f"""
    <div style="padding: 15px; background: #f8f9fa; border-left: 4px solid {color};
                margin: 10px 0; border-radius: 4px;">
        <div style="font-size: 14px; color: {color}; margin-bottom: 8px; font-weight: bold;">
            {icon} Hint {current_level}/3: {name}
        </div>
        <div style="font-size: 15px; font-weight: bold; margin-bottom: 10px; color: #333;">
            {title}
        </div>
    </div>
    """

    _display_output(html, content)

    # Show "more hints available" message
    if current_level < max_level:
        remaining = max_level - current_level
        more_html = f"""
        <div style="padding: 8px; background: #e9ecef; border-radius: 4px; margin-top: 10px;
                    font-size: 13px; color: #666;">
            &#x27A1; Call <code>hint("{problem_name}")</code> again for more guidance
            ({remaining} hint{"s" if remaining > 1 else ""} remaining)
        </div>
        """
        _display_output(more_html)
    else:
        final_html = """
        <div style="padding: 8px; background: #fff3cd; border-radius: 4px; margin-top: 10px;
                    font-size: 13px; color: #856404;">
            &#x1F914; Still stuck? Try breaking down the problem into smaller parts,
            or review similar solved problems.
        </div>
        """
        _display_output(final_html)


def list_problems(category: Optional[str] = None) -> dict[str, list[str]]:
    """
    List all available problems with hints.

    Args:
        category: Optional category name to filter (e.g., "01_array_string")

    Returns:
        Dict mapping category names to list of problem names
    """
    hints_dir = _get_hints_dir()
    problems: dict[str, list[str]] = {}

    if not hints_dir.exists():
        return problems

    for yaml_file in sorted(hints_dir.glob("*.yaml")):
        category_name = yaml_file.stem
        if category and category not in category_name:
            continue

        try:
            with open(yaml_file, encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data:
                    problems[category_name] = list(data.keys())
        except (OSError, yaml.YAMLError):
            continue

    return problems


def show_problems(category: Optional[str] = None) -> None:
    """
    Display available problems in a formatted table.

    Args:
        category: Optional category name to filter
    """
    problems = list_problems(category)

    if not problems:
        print("No problems found with hints.")
        return

    html = """
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        <h3 style="color: #333; margin-bottom: 15px;">Available Problems</h3>
        <table style="border-collapse: collapse; width: 100%;">
            <thead>
                <tr style="background: #f8f9fa;">
                    <th style="padding: 10px; text-align: left; border-bottom: 2px solid #dee2e6;">Category</th>
                    <th style="padding: 10px; text-align: left; border-bottom: 2px solid #dee2e6;">Problems</th>
                </tr>
            </thead>
            <tbody>
    """

    for cat_name, prob_list in problems.items():
        # Format category name nicely
        display_name = cat_name.replace('_', ' ').title()
        probs_formatted = ', '.join(f'<code>{p}</code>' for p in prob_list[:5])
        if len(prob_list) > 5:
            probs_formatted += f' <em>... and {len(prob_list) - 5} more</em>'

        html += f"""
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #dee2e6; vertical-align: top;">
                        <strong>{display_name}</strong>
                    </td>
                    <td style="padding: 10px; border-bottom: 1px solid #dee2e6;">
                        {probs_formatted}
                    </td>
                </tr>
        """

    html += """
            </tbody>
        </table>
        <p style="margin-top: 15px; color: #666; font-size: 13px;">
            Use <code>hint("problem_name")</code> to get hints for any problem.
        </p>
    </div>
    """

    _display_output(html)


def reset_all_hints() -> None:
    """Reset hint progress for all problems."""
    global _hint_state
    _hint_state = defaultdict(int)
    print("All hint progress has been reset.")


def reload_hints() -> None:
    """Reload hints from YAML files (useful after editing hint files)."""
    global _hints_cache
    _hints_cache = None
    _load_all_hints()
    print("Hints reloaded from files.")
