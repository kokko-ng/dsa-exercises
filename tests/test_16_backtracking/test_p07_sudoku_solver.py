"""Tests for sudoku_solver problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


def is_valid_sudoku(board):
    """Check if a completed sudoku board is valid."""
    # Check rows
    for row in board:
        if sorted(row) != list('123456789'):
            return False

    # Check columns
    for c in range(9):
        col = [board[r][c] for r in range(9)]
        if sorted(col) != list('123456789'):
            return False

    # Check 3x3 boxes
    for box_r in range(3):
        for box_c in range(3):
            box = []
            for r in range(box_r * 3, box_r * 3 + 3):
                for c in range(box_c * 3, box_c * 3 + 3):
                    box.append(board[r][c])
            if sorted(box) != list('123456789'):
                return False

    return True


@pytest.fixture
def sudoku_solver():
    func = get_function("sudoku_solver")
    if func is None:
        pytest.skip("Function 'sudoku_solver' not registered.")
    return func


class TestSudokuSolverBasic:
    def test_example_1(self, sudoku_solver):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        sudoku_solver(board)
        assert is_valid_sudoku(board)


class TestSudokuSolverEdgeCases:
    def test_easy_puzzle(self, sudoku_solver):
        board = [
            [".", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
        ]
        sudoku_solver(board)
        assert is_valid_sudoku(board)
        assert board[0][0] == "5"
