# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxx):
            if not node: return 0
            
            if node.val >= maxx:
                maxx = node.val
                return 1 + dfs(node.left, maxx) + dfs(node.right, maxx)

            return dfs(node.left, maxx) + dfs(node.right, maxx)
            
        return dfs(root, float('-inf'))


