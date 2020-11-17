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
# O(N) Time | O(logN) Space
----------------------
def DiameterofTree(root):
    return findDiameter(root)[1]

def findDiameter(root):
    if not root:
        return 0,0  # depth, dia
    
    left = findDiameter(root.left)
    right = findDiameter(root.right)
    
    depth = max(left[0], right[0]) + 1
    diameter = max(left[1], right[1], left[0] + right[0])   
    """
    We are maximizing diameter,
    we have 3 poosibilties
    1. it can be the left Subtree  (not including the root) ---> we use left[1]
    2. it can be the right Subtree (not including the root) ----> we use right[1]
    3. it can be the sum of left and right Subtree (including the root) ---> we use left[0] + right[0], since we are calculating depth of any node that may 
    be a potential root of diameter
    
    these three possiblities are only ones at any given point
    """
    return depth, diameter


          