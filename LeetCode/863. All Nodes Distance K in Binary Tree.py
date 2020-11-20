"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.


Note: If you want To visualize the Tree, Go to Leetcode

Constraints:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.

"""
# Solution ---> 
# O(N) Time | O(N) Space

"""
Intution or Logic:

Since you need to go back and go down the tree to find the K distance nodes. Then you can directly image this tree question to a graph question. 
For each node, it has three edges: left, right, parent. 
Since this treeNode does not have a parent, you firstly need to use a dictionary to connect each node with its parents (go through the tree first to get the parents map). 
Then Use BFS to iterate the new constructed graph to find the K distance Node starting from the target Node. 

Note: You Need to use a visited set to avoid visiting the same node multiple times.

"""
----------------------------
def KdistanceFromNode(root, target, k):     # target is a node
    parents = getParents(root)
    return BFS(target, parents, k)


def BFS(target, parents, k):
    vis = set()
    vis.add(target)
    queue = deque([target])
    cnt = 0
    while queue:
        if k == cnt:
            return getValues(queue)
            
        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()
            if cur.left and cur.left not in vis:
                queue.append(cur.left)
                vis.add(cur.left)
            if cur.right and cur.right not in vis:
                queue.append(cur.right)
                vis.add(cur.right)
            if parents[cur] and parents[cur] not in vis:
                queue.append(parents[cur])
                vis.add(parents[cur])
        
        cnt += 1
        
    return []  # if graph doesnt Have k distance from the target Node


def getValues(queue):
    res = []
    while queue:
        cur = queue.popleft()
        res.append(cur.val)
    return res
        

def getParents(root):
    queue = deque([root])
    parents = {root: None}     # root Node has No Parent
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
            parents[cur.left] = cur
        if node.right:
            queue.append(node.right)
            parents[cur.right] = cur
            
    return parents 
    
  
