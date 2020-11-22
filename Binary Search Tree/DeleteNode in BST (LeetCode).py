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
    return deleteNode(root, key, None)

def deleteNode(root, key, parent):
    cur = root
    while cur:
        if key > cur.val:
            parent = cur
            cur = cur.right
        elif key < cur.val:
            parent = cur
            cur = cur.left
        else:
            if cur.left and cur.right:
                succ, succFather = findSuccessor(cur)
                cur.val = succ.val
                
                #---------- Method 1-----------------
                deleteNode(cur.right, cur.val, cur)             # You can either Use Method 1 or Method 2. Method 1 does it Calling the function again on Right Subtree
                                                                # Method 2 does it by changing the pointers
                #---------- Method 2---------------
                # if succ != cur.right:
                #     succFather.left = succ.right
                # else:
                #     cur.right = succ.right
                
                
                
            if not parent:
                return cur.left or cur.right    # This Also deals with the case with only one node
            elif parent.left == cur:
                parent.left = cur.left or cur.right
            elif parent.right == cur:
                parent.right = cur.left or cur.right
            
            break   # Important
            
    return root

def findSuccessor(node):
    succFather = node
    succ = node.right
    while succ.left:
        succFather = succ
        succ = succ.left
    return succ, succFather
            
            
  
