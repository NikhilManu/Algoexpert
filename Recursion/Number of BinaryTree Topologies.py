"""
Unique Binary Search Tree
"""

"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Input: n = 3
Output: 5

Input: n = 1
Output: 1
"""

# Solution
#
----------------------
def numberOfBinaryTreeTopologies(n):
	dp = [1]
	for m in range(1, n+1):
		numofTree = 0
		for left in range(m):
			right = m - 1 - left
			leftSubtree = dp[left]
			rightSubtree = dp[right]
			numofTree += leftSubtree * rightSubtree
		dp.append(numofTree)
	return dp[n]
	
	
	
# Solution
# 
------------------------------
def numberOfBinaryTreeTopologies(n):
  dp = [0] * (n+1)
	dp[0] = 1
	for i in range(1, n + 1):
		for left in range(i):
			right = i - 1 - left
			dp[i] += dp[left] * dp[right]
	return dp[n]
