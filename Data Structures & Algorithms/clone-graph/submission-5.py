"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if not node: return None
            if node in oldToNew: return oldToNew[node]

            newNode = Node(node.val)
            oldToNew[node] = newNode
            neighbors = []
            for nei in node.neighbors:
                neighbors.append(dfs(nei))
            newNode.neighbors = neighbors
            
            return newNode


        return dfs(node)
