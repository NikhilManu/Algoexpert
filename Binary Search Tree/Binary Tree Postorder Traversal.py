"""
Same name in Leetcode
"""
"""
Given the root of a BST, return the nodes in postorder Traversal

Could you Implement it iteratively
"""

# Solution 1 ---- Recursive
# Time O(N) | O(N) Space
------------------------
def PostOrderTraversal(root):
    return postorder(root, [])

def postorder(node, res):
    if not node:
        return 
    
    postorder(node.left, res)
    postorder(node.right, res)
    res.append(node.val)
    
    return res


# Solution 2 --- Iterative
# Time O(N) | Space O(N)
----------------------
def PostOrder(root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if not node:
            continue
        
        res.append(node.val)
        stack.append(node.left)
        stack.append(node.right)
        
    return res[::-1]

# Solution 3 --- Morris Traversal
# Time O(N) | Space O(1)
------------------------------
def postOrder(root):
    res = []
    cur = root
    while cur:
        if not cur.right:
            res.append(cur.val)
            cur = cur.left
        else:
            succ = cur.right
            while succ.left and succ.left != cur:
                succ = succ.left
            
            if not succ.left:
                res.append(cur.val)
                succ.left = cur
                cur = cur.right
            else:
                succ.left = None
                cur = cur.left
    
    return res[::-1]

                
        
      
  
