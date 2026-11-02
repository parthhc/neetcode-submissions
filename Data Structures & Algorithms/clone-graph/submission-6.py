"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(curr_node):
            if curr_node in old_to_new: return old_to_new[curr_node]
            if not node: return None

            new_node = Node(curr_node.val)
            old_to_new[curr_node] = new_node
            for nei in curr_node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node

        return dfs(node)