# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node: return 0

            leftRes = max(dfs(node.left), 0)
            rightRes = max(dfs(node.right), 0)

            res[0] = max(leftRes + rightRes + node.val, res[0])

            return node.val + max(leftRes, rightRes)

        dfs(root)
        return res[0]