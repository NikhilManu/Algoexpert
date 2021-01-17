"""

"""

"""
You're given a 2D array containing 0 and 1. An island is defined as any number of 1 which is horizontally
or vertically adjacent but not diagonally adjacent
It is not an island if it touches with the border of the matrix

Note that island can be in T or L shaped.

Write a program to remove all of the valid islands
"""

# Solution
# Time O(wh) And Space O(wh)
-----------------------------
def removeIslands(arr):
	rlen, clen = len(arr), len(arr[0])
	connectedWithBorder = set()

	for row in range(rlen):
		for col in range(clen):
			if isBorder(arr, row, col) and arr[row][col] == 1:
				dfs(arr, row, col, connectedWithBorder)

	for row in range(rlen):
		for col in range(clen):
			if (row, col) in connectedWithBorder:
				continue
			
			arr[row][col] = 0
					
	return arr

def dfs(arr, row, col, connectedWithBorder):
	if outofBounds(arr, row, col):
		return 
	
	if isConnectedWithBorder(row, col, connectedWithBorder):
		return 
	
	if arr[row][col] == 0:
		return 
	
	connectedWithBorder.add((row,col))
	dfs(arr, row+1, col, connectedWithBorder)	
	dfs(arr, row-1, col, connectedWithBorder)
	dfs(arr, row, col+1, connectedWithBorder)
	dfs(arr, row, col-1, connectedWithBorder)

def isBorder(arr, row, col):
	return row == 0 or col == 0 or row == len(arr) - 1 or col == len(arr[row]) - 1

def isConnectedWithBorder(row, col, connectedWithBorder):
	return (row, col) in connectedWithBorder

def outofBounds(arr, row, col):
	return row < 0 or col < 0 or row >= len(arr) or col >= len(arr[row])

				
		
				
