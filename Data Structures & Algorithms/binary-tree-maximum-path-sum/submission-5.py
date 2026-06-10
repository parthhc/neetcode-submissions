# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]
        def dfs(node):
            if not node: return 0

            left_res = dfs(node.left)
            right_res = dfs(node.right)

            left = left_res if left_res > 0 else 0
            right = right_res if right_res > 0 else 0

            res[0] = max(res[0], node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return res[0]
