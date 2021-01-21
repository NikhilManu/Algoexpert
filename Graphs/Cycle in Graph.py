"""
Course Schedule
"""

"""
"""

# Solution - My Solution
# Time
-----------------------

def cycleInGraph(edges):
	graph = makeGraph(edges)
	for i in range(len(edges)):
		if cycleCheck(i, graph, set(), set()):
			return True

	return False

def cycleCheck(i, graph, visited, visiting):
	if i in visiting:
		return True
	if i in visited:
		return 
	visited.add(i)
	visiting.add(i)
	for node in graph[i]:
		if cycleCheck(node, graph, visited, visiting):
			return True
	visiting.remove(i)
	return False

def makeGraph(edges):
	graph = {}
	for i in range(len(edges)):
		graph[i] = edges[i]
		
	return graph


