"""
Binary Tree Maximum Path Sum [ Name of this Qn in LeetCode ]
"""

"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

Input :

    -10
   /   \
  9     20
       / \
      15  7

Output: 42


TestCase 2:

  Input :

      -10
      /  \

  Output: -10 

# TestCase 2 is given so that u can understand there is a small mistake in orginal Solution of AlgoExpert
"""

# Solution 1 ---> AlgoExpert Soln
# O(N) Time | O(logN) Space
-----------------
def maxPathSum(root):
    return findMaxSum(root)[1]

def findMaxSum(root):
    if not root:
        return float('-inf'), float('-inf')     # In Algoexpert given (0,0), This is wrong since if all the value is -ve it will take max and only give zero
    
    leftBranch, leftpathSum = findMaxSum(root.left)
    rightBranch, rightpathSum = findMaxSum(root.right)
    
    biggerChildBranch = max(leftBranch, rightBranch)    # It is called biggerChildBranch since it doesnt include current node
    biggerBranch = max(root.val, biggerchildBranch + root.val)
    
    maxSumatRoot = max( leftBranch + root.val + rightBranch, biggerBranch)
    maxpathSum = max( leftpathSum, rightpathSum, maxsumatRoot)
    return biggerBranch, maxpathSum
    
