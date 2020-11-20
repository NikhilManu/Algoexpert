"""
QN in Leetcode is for premium Members Only
"""

"""
Given the root of BST and a Target Value, We Have to find a value in BST such That it is the closest value to the target Value

"""

# Solution --- Recursive
# Time O(log N) | Space O(log N)     ----> Worst Case O(N) Time and Space
----------------------
def FindClosestValue(root, target):
    return Helper(root, target, float('inf'))

def Helper(node, target, closestValue):
    if not node:
        return closestValue
    
    if abs(target - closestValue) > abs(target - node.val):
        closestValue = node.val
    
    if target < node.val:
        return Helper(node.left, target, closestValue)
    elif target > node.val:
        return Helper(node.right, target, closestValue)
    else:
        return closestValue
    
    
# Solution --- Iterative
# Time O(log N) Avg and O(N) Worst | O(1) Space
---------------------------------
def FindClosestValue(root, target):
    cur = root
    closest = float('inf')
    
    while cur:
        if abs(closest - target) > abs(target - cur.val):
            closest = cur.val
        
        if target > cur.val:
            cur = cur.right
        elif target < cur.val:
            cur = cur.left
        else:
            break
            
    return closest
        
    
    
  

