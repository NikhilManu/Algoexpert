"""
Flatten Binary Tree To linked List [ Name of this Qn in LeetCode ]
"""

"""
AlgoExpert Qn:
Given Binary Tree or BST, flatten it to Doubly Linked List in Inorder Fashion,
ie...if it is a BST then the linkedList will be sorted.

"""
# Solution ---
# O(N) Time | O(d) Space where d is the depth
----------------------
def FlattenBinaryTree(root):
    return Flatten(root)[0]

def Flatten(node):
    if not node.left:
        leftMost = node
    else:
        leftSubtreeLeftmost, leftSubtreeRightmost = Flatten(node.left)
        ConnectNodes(leftSubtreeLeftmost, node)
        leftMost = leftSubtreeLeftmost
        
    if not node.right:
        rightMost = node
    else:
        rightSubtreeLeftmost, rightSubtreeRightmost = Flatten(node.right)
        ConnectNodes(node, rightSubtreeRightmost)
        rightMost = rightSubtreeRightmost
        
    return leftMost, rightMost
  
def ConnectNodes(leftNode, rightNode):
    leftNode.right = rightNode
    rightNode.left = leftNode
