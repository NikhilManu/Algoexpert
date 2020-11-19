"""
Similar Qn but not Same Qn.

Populating Next Right Pointers in Each Node
Populating Next Right Pointers in Each Node ll
"""

"""

"""

# Solution --
# O(N) Time | O(1) Space
--------------------------
def RightSiblingTree(root):
    mutate(root, None, None)
    return root

def mutate(node, parent, isleftChild):
    if not node:
        return 
    
    left, right = node.left, node.right
    mutate(left, node, True)
    
    if not parent:
        node.right = None
    elif isleftChild:
        node.right = parent.right
    else:
        if not parent.right:
            node.right = None
        else:
            node.right = parent.right.left
        
    mutate(right, node, False)
    
    
