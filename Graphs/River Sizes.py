"""
Similar Qn in LeetCode
1. Number of Islands
2. Max Area of Island
"""

"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical).
You may assume all four edges of the grid are surrounded by water.
Return an Array Consisting of area of All Island

"""
# Solution - Recursive Solution
# Time O(R*C) | Space O(R*C)
-------------------------
def RiverSizes(grid):
    area, seen = [], set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                area.append(DFS(grid, i, j, seen))
                
    return area

def DFS(grid, i, j, seen):
    if outofBounds(i,j, grid) or grid[i][j] == 0 or (i,j) in seen:
        return 0
    seen.add((i,j))
    return 1 + DFS(grid, i+1, j, seen) + DFS(grid, i-1, j, seen) + DFS(grid, i, j+1, seen) + DFS(grid, i, j-1, seen) 

def outofBounds(i,j,grid):
    return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])
   
                       
  
