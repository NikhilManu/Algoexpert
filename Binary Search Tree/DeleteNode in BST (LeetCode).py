"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
"""

# Solution --- Iterative 
# O(N) Time | O(1) Space
-------------------------------
def delete(root, key):
