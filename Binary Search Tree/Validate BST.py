"""
Validate Binary Search Tree [ Name of this Qn in LeetCode ]
"""

# Below AlgoExpert Solution, I have also provided answer to LeetCode Qn

"""
Given a BST, return True if it is a Valid BST

Input:      5
           / \
          1   4
             / \
            3   6
            
Output: False

"""

# SOlution --
# O(N) Time | O(d) Space
----------------------
def validBST(root):
    return validateBST(root, float('-inf'), float('inf'))

def validateBST(node, minVal, maxVal):
    if not node:
        return True
   
    if minVal > node.val or node.val >= maxVal:
        return False
    
    return validateBST(node.left, minVal, node.val) and validateBST(node.right, node.val, maxVal)


"""
LeetCode:

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3
  
Output: True

"""
# Solution 1 --- Recursive
# Time O(N) | O(d) Space
---------------------------
def isvalidBST(root):
    return ValidateBST(root, float('-inf'), float('inf'))

def validateBST(node, minVal, maxVal):
    if not node:
        return True
   
    if minVal >= node.val or node.val >= maxVal:        # Read The conditions of BST
        return False
    
    return validateBST(node.left, minVal, node.val) and validateBST(node.right, node.val, maxVal)

 
# Solution 2 --- Iterative 
# Time O(N) | O(N) Space
-----------------------------
def validateBST(root):
    stack = [(root, float('-inf'), float('inf'))]
    while stack:
        node, minVal, maxVal = stack.pop()

        if not node:
            continue

        if minVal >= node.val or node.val >= maxVal:
            return False

        stack.append((node.left, minVal, node.val))
        stack.append((node.right, node.val, maxVal))

    return True

# Solution 3 -- Inorder Iterative
# Time O(N) | O(N) Space
-------------------------
def validateBST(root):
    cur = root
    stack = []
    prev = float('-inf')
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        node = stack.pop()
        if node.val <= prev:
            return False
        
        prev = node.val
        cur = node.right
        
    return True
              


