"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in Tree
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

"""

# Solution --
# Time O(N) | Space O(N)
-------------------------
def lowestCommonAncestor(root, p, q):
    parent = getParent(root)
    depthOne = getDepth(p, root, parent)
    depthTwo = getDepth(q, root, parent)
    if depthOne > depthTwo:
        return makeSamelevel_and_findAncestor(p, q, depthOne - depthTwo, parent)
    else:
        return makeSamelevel_and_findAncestor(q, p, depthTwo - depthOne, parent)

def makeSamelevel_and_findAncestor(lower, higher, diff, parent):
    while diff > 0:
        lower = parent[lower]
        diff -= 1

    while lower != higher:
        lower = parent[lower]
        higher = parent[higher]

    return lower


def getDepth(node, root, parent):
    depth = 0
    while node != root:
        node = parent[node]
        depth += 1
    return depth

def getParent(root):
    parent = {root:None}
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)

        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    return parent
