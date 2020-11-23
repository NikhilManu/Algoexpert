"""
Same Name in LeetCode
"""

"""
Given root of BST, return the inorder Traversal of the nodes 

Recursion is trivial, 
Follow Up:

1. Do it Without Recursion
2. Do it in O(1) Space

"""

# Solution 1 --- Recursive
# O(N) Time | O(N) Space
----------------------------
def Inorder(root):
    return inorderHelper(root, [])

def inorderHelper(node, res):
    if not node:
        return
    
    inorderHelper(node.left, res)
    res.append(node.val)
    inorderHelper(node.right, res)
    
    return res


# Solution 2 --- Iterative with Stack
# O(N) Time | O(N) Space
-------------------------------
def InorderTraversal(root):
    res, stack = [], []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
            
        node = stack.pop()
        res.append(node.val)
        cur = node.right
    
    return res

# Solution 3 ---- Morris Traversal
# O(N) Time | O(1) Space , if the resultant array is not included
-------------------------------------------
def InorderTraversal(root):
    res = []
    current = root
    while current:
        if not current.left:
            res.append(current.val)
            cur = cur.right
        else:
            predecessor = current.left 
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
                
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                res.append(current.val)
                predecessor.right = None
                current = current.right
                
    return res
        
    
    
