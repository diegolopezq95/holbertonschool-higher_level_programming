#!/usr/bin/python3
"""
This module solves the n_queens problem
"""

from sys import argv, exit

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if not argv[1].isdigit():
    print("N must be a number")
    exit(1)
if int(argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

def check(board, row, col):
    '''
    Checks valid positions in col
    '''
    for i in range(col):
        if board[i] is row:
            return False
        if abs(board[i] - row) is abs(i - col):
            return False
    return True


def solve(board, col):
    '''
    Solves the n_queens problem
    '''
    if col is len(board):
        for i in range(len(board)):
            print("[{}, {}]".format(str(i), str(board[i])), end="")
            if i != len(board) - 1:
                print(",", end="")
            else:
                print("")
    for row in range(len(board)):
        if check(board, row, col):
            board[col] = row
            solve(board, col + 1)

if __name__ == "__main__":
    N = int(argv[1])
    for col in range(N):
        board = [0] * (N)
    solve(board, 0)
