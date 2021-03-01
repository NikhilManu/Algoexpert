"""
Balanced Binary Tree [LeetCOde]
"""

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

# Solution
# Time - O(n) And Space - O(h)
---------------------------
def heightBalancedBinaryTree(root):
	return dfs(root) != '#'
	
def dfs(root):
	if not root:
		return 0
	
	left = dfs(root.left)
	right = dfs(root.right)
	
	if left == '#' or right == '#' or abs(left - right) > 1:
		return '#'
	
	return 1 + max(left, right)
	
