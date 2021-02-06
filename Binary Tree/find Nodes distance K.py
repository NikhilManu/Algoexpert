"""
All Nodes Distance K in Binary Tree
"""

"""
Check in LeetCode
"""

# Solution (My Solution)
# Time O(n) | O(n) Space
-----------
def findNodesDistanceK(tree, target, k):
	parent = getParent(tree)
	return findTargetandNodes(tree, target, parent, k)

def findTargetandNodes(node, target, parent, k):
	if not node:
		return [] 
	
	if node.value == target:
		return getNodes(node, k, parent)
	
	left = findTargetandNodes(node.left, target, parent, k) 

	
	return left if left else findTargetandNodes(node.right, target, parent, k)
	
	
	
def getNodes(target, k, parent):
	stack = [(target, 0)]
	vis = set()
	res = []
	while stack:
		node, level = stack.pop()
		if not node or node in vis:
			continue
		
		vis.add(node)
		
		if level == k:
			res.append(node.value)
			continue
			
		stack.append((node.left, level + 1))
		stack.append((node.right, level + 1))
		stack.append((parent[node], level + 1))

	return res

def getParent(node):
	parent = {node:None}
	stack = [node]
	while stack:
		node = stack.pop()
		
		if node.left:
			parent[node.left] = node
			stack.append(node.left)
			
		if node.right:
			parent[node.right] = node
			stack.append(node.right)
			
	return parent
