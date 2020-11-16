"""
Path Sum 
            ---> [ Name of the Qn in LeetCode ]
Path Sum II
"""

"""
Given a Binary Tree, Compute Sum of the Branches and return them in an array

Input: 

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1


output : [27, 22, 26, 18]
"""
# Solution --->
# O(N) Time and Space
---------------
def BranchSums(root):
    sums = []
    calculateSum(root, currentSum, sums)
    return sums

def calculateSum(node, currentSum, sums):
    if not node:
        return
    
    currentSum += node.val
    if not node.left and not node.right:
        sums.append(currentSum)
        return 
    
    calculateSum(node.left, currentSum, sums)
    calculateSum(node.right, currentSum, sums)
    
