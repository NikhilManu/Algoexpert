"""
 Binary Tree Inorder Traversal [ Similar Qn in LeetCOde ]

"""
#AlgoExpert Solution for is BullShit. just Learn Morris Traversal

# Solution ----> With stack
# Time O(N) | O(N) Space
--------------------------
def InorderTraversal(root, callback):
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
    
        if stack:
            node = stack.pop()
            callback(node)
            cur = node.right
            
    
 # Solution ----> Morris Traversal
# Time O(N) | O(N) Space
-------------------------- 
def InorderTraversal(root, callback):
    current = root
    predecessor = None  
    while current:
        if not current.left:
            callback(current)
            current = current.right
        else:
            predecessor = current.left
            whlie predecessor.right and predecessor.right != current:   # Finding Inorder Predecessor 
                predecessor = predecessor.right
                
            if not predecessor.right:
                predecessor.right = cur # Link predecessor and cur Node
                cur = cur.left
            else:
                callback(current)
                current = current.right
                predecessor.right = None
                
                
