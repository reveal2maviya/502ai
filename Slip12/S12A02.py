"""
4-Queens Problem Solver

Question:
Write a Python program to simulate the 4-Queens problem.

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python four_queens_solver.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 four_queens_solver.py
"""

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check if there is a queen in the diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def print_solution(board):
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def solve_four_queens(board, row):
    if row == len(board):
        # All queens are placed successfully
        print("Solution:")
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_four_queens(board, row + 1)
            board[row] = -1  # Backtrack

if __name__ == "__main__":
    board_size = 4
    initial_board = [-1] * board_size  # Initialize the board with -1 indicating no queen in a row

    solve_four_queens(initial_board, 0)
