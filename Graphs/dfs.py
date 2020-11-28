"""
Dfs on A Graph
"""

# Time O(V+E) | Space O(V)
--------------------
class Node:
    def __init__(self, name):
        self.name = name 
        self.children = []
        
    def addChildren(self, name):
        self.children.append(Node(name))
        
    def DFS(self, arr):
        array.append(self.name)
        for child in self.children:
            child.DFS(arr)
        return arr
