"""
Inorder Successor of BST
"""

"""
Find the inorder Successor of a Binary Tree

"""

# Solution
# O(h) Time | O(1) SPace
------------------------
def findSuccessor(tree, node):
    if node.right:
        return getLeftmostOfRight(node)

    return getRightmost(node)


def getRightmost(node):
    cur = node
    while cur.parent and cur.parent.right == cur:
        cur = cur.parent

    return cur.parent

def getLeftmostOfRight(node):
    cur = node.right
    while cur.left:
        cur = cur.left

    return cur
