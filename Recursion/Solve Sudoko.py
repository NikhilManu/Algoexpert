""" 
Sudoko Solver
"""

"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
"""

#Solution
# Time O(1) Space and Time
----------------------------
def solveSudoku(board):
	solve(0, 0, board)
	return board

def solve(row, col, board):
	find = findEmpty(board)
	if not find:
		return True
	
	row, col = find
	for i in range(1, 10):
		if isValid(i, row, col, board):
			board[row][col] = i
			
			if solve(row, col, board):
				return True
			
			board[row][col] = 0
			
	return False

def isValid(num, row, col, board):
	for c in range(9):
		if board[row][c] == num and c != col:
			return False
	for r in range(9):
		if board[r][col] == num and r != row:
			return False
	boxX = (row//3) * 3
	boxY = (col//3) * 3
	
	for rowidx in range(3):
		for colidx in range(3):
			curRow = boxX + rowidx
			curCol = boxY + colidx
			if board[curRow][curCol] == num:
				return False
			
	return True
			
def findEmpty(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == 0:
				return i, j
	return 
