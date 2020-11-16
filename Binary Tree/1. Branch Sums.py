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
    

"""
Qn ---> Path Sums

"""
# Recursive Solution 
------------------
def hasPathSum(root, Sum):
    return checker(root, Sum, 0)
    
def checker(node, Sum, currentSum):
    if not node:
    return 

    currentSum += node.val
    if not node.left and not node.right:
        return currentSum == Sum

    return checker(node.left, Sum, currentSum) or checker(node.right, Sum, currentSum)


# Iterative Solution
-------------------------
def hasPathSum(root, Sum):
    if not root:
        return False

    stack = [(root, 0)]
    while stack:
        node, currentSum = stack.pop()
        if not node:
            continue

        currentSum += node.val
        if not node.left and not node.right and currentSum == Sum:
            return True

        stack.append((node.left, currentSum))
        stack.append((node.right, currentSum))                

    return False

