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



