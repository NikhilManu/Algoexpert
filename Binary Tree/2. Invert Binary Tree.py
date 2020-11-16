"""
Same Name in LeetCode
"""

"""
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""
# Solution 1 --> Iterative Solution
#
---------------------
def InvertBinaryTree(root):
    queue = deque([root])       # dont use normal list, Since pop(0) is very costly
    while queue:
        node = queue.popleft()
        if not node:
            continue

        node.left, node.right = node.right, node.left

        queue.append(node.left)
        queue.append(node.right)

    return root

# Solution 2 ---> Recursive Solution
# 
---------------------
def InvertBinaryTree(root):
    if not root:
        return 
    
    root.left, root.right = InvertBinaryTree(root.right), InvertBinaryTree(root.left)
    
    return root
