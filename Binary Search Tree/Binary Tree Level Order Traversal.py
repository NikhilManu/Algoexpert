"""
Same Name in LeetCode
"""
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    3
   / \
  9  20
    /  \
   15   7

Output:
[
  [3],
  [9,20],
  [15,7]
]

"""

# Solution 1 --- Iterative    , I think this is more Easier than recursive
# Time O(N) | Space O(N)
--------------------------------

def LevelOrder(root):
    if not root:
        return []   # Handling empty Tree
    
    queue, res = deque([root]), []
    while queue:
        levelArray = []
        level = len(queue)
        for _ in range(level):
            node = queue.popleft()
            levelArray.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        res.append(levelArray)
        
    return res
    
    

