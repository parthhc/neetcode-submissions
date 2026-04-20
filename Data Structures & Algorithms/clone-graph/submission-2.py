"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        def dfs(node):
            if node in seen: return seen[node]

            newNode = Node(node.val, [])
            seen[node] = newNode
            for i in range(len(node.neighbors)):
                newNode.neighbors.append(dfs(node.neighbors[i]))

            return newNode

        return dfs(node) if node else None