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
    while stack:
        node = stack.pop()
        if not node:
            continue
        
        res.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
        
    return res
  
# SOlution 3 ---- Morris Traversal
# Time O(N) | O(1) Space
----------------------
def PreorderTraversal(root):
    res = []
    cur = root
    while cur:
        if not cur.left:
            res.append(cur.val)
            cur = cur.right
        else:
            pred = cur.left
            while pred.right and pred.right != cur:
                pred = pred.right
            
            if not pred.right:
                res.append(cur.val)
                pred.right = cur
                cur = cur.left
            else:
                pred.right = None
                cur = cur.right
    
    return res
    
