"""
Same Name in leetCode
"""

"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

"""

# Solution 
# O(N) Time | O(h) Space
----------------------
def binaryTreeDiameter(tree):
    return dfs(tree)[1]

def dfs(node):
    if not node:
        return 0,0 

    leftHeight, leftDiameter = dfs(node.left)
    rightHeight, rightDiameter = dfs(node.right)

    Height = max(leftHeight, rightHeight) + 1
    Diameter = max(leftDiameter, rightDiameter, leftHeight + rightHeight)
    return Height, Diameter   


    """
    We are maximizing diameter,
    we have 3 poosibilties
    1. it can be in the left Subtree  (not passing through the root) 
    2. it can be in the right Subtree (not passing through the root) 
    3. it can be a path which passes through the root
    
    these three possiblities are only ones at any given point
    """



          
