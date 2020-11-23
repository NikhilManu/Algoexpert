"""
Same Name in LeetCode
"""

"""
Given root of BST, return the nodes in preorder Traversal

Could You do it Iteratively
"""

# Solution 1 --- Recursive 
# Time O(N)  | O(N) Space
-------------------------
def PreOrderTraversal(root):
    return preorder(root, [])

def preorder(node, res):
    if not node:
        return
    
    res.append(node.val)
    preorder(node.left, res)
    preorder(node.right, res)
    
    return res

# Solution 2 --- Iteratively
# Time O(N) | O(N) Space
-----------------------------
def PreorderTraversal(root):
    res, stack = [], [root]
    cur = root
    while stack:
        node = stack.pop()
        if not node:
            continue
        
        res.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
        
    return res
  
