""" 
implement BFS in a Graph
"""

# Time O(V+E) | O(V) Space
--------------------
class Node:
    def __init__(self, name):
        self.name = name 
        self.children = []
        
    def addChild(self, name):
        self.children.append(Node(name))
        
    def BFS(self, arr):
        queue = deque([self])
        while queue:
            node = queue.popleft()
            arr.append(node.name)
            for child in node.children:
                queue.append(child)
                
        return arr
