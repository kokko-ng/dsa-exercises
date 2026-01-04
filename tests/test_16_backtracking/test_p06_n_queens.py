"""Tests for n_queens problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


def is_valid_solution(board):
    """Check if a board configuration is valid."""
    n = len(board)
    queens = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'Q':
                queens.append((r, c))

    if len(queens) != n:
        return False

    # Check no attacks
    for i, (r1, c1) in enumerate(queens):
        for j, (r2, c2) in enumerate(queens):
            if i >= j:
                continue
            if r1 == r2 or c1 == c2:
                return False
            if abs(r1 - r2) == abs(c1 - c2):
                return False
    return True


@pytest.fixture
def n_queens():
    func = get_function("n_queens")
    if func is None:
        pytest.skip("Function 'n_queens' not registered.")
    return func


class TestNQueensBasic:
    def test_n_4(self, n_queens):
        result = n_queens(4)
        assert len(result) == 2
        for board in result:
            assert is_valid_solution(board)

    def test_n_1(self, n_queens):
        result = n_queens(1)
        assert result == [["Q"]]


class TestNQueensEdgeCases:
    def test_n_2(self, n_queens):
        result = n_queens(2)
        assert result == []

    def test_n_3(self, n_queens):
        result = n_queens(3)
        assert result == []

    def test_n_8(self, n_queens):
        result = n_queens(8)
        assert len(result) == 92
        for board in result:
            assert is_valid_solution(board)
