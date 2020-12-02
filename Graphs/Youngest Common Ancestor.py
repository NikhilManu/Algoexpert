"""
Similar Qns
1. Lowest Common Ancestor of Binary Tree  ---> In LeetCode Section
2. Lowest Common Ancestor of Binary Seach Tree [Easy]
"""

"""
Given a tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

"""

#Solution - if the Tree contains .parent 
# Time O(N) | Space O(1)
----------------------------
def YoungestCommonAncestor(root, node1, node2):
    depthOne = getDepth(node1, root)
    depthTwo = getDepth(node2, root)
    differenceofDepth = abs(depthOne - depthTwo)
    if depthOne > depthTwo:
        return makeSameLevel_and_FindAncestor(node1, node2, differenceofDepth)
    else:
        return makeSameLevel_and_FindAncestor(node2, node1, differenceofDepth)
    
def makeSameLevel_and_FindAncestor(lower, higher, difference):
    while difference > 0:
        lower = lower.parent
        difference -= 1
        
    while lower != higher:
        higher = higher.parent
        lower = lower.parent
        
    return lower

def getDepth(node, root):
    depth = 0 
    while node != root:
        node = node.parent
        depth += 1
        
    return depth


# Solution - if the tree doesnt contain .parent Functionality
# Time O(N) | Space O(N)
-----------------------
def YoungestCommonAncestor(root, node1, node2):
    parent = getParent(root)   # Dictionary which contains the parent of Every Node
    depthOne = getDepth(node1, root, parent)
    depthTwo = getDepth(node2, root, parent)
    differenceofDepth = abs(depthOne - depthTwo)
    if depthOne > depthTwo:
        return makeSameLevel_and_FindAncestor(node1, node2, differenceofDepth, parent)
    else:
        return makeSameLevel_and_FindAncestor(node2, node1, differenceofDepth, parent)
    
def makeSameLevel_and_FindAncestor(lower, higher, difference, parent):
    while difference > 0:
        lower = parent[lower]
        difference -= 1
        
    while lower != higher:
        higher = parent[higher]
        lower = parent[lower]
        
    return lower

def getParent(root):
    parent = {root:None}
    stack = [root]
    while stack:
        node = stack.pop()
        for child in node.children:
            parent[child] = node
            stack.append(child)
    return parent

def getDepth(node, root, parent):
    depth = 0 
    while node != root:
        node = parent[node]
        depth += 1
        
    return depth
