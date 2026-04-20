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

            leftRes = dfs(node.left)
            rightRes = dfs(node.right)

            leftVal = max(0, leftRes)
            rightVal = max(0, rightRes)

            res[0] = max(res[0], node.val + leftVal + rightVal)
            return node.val + max(leftVal, rightVal)

        dfs(root)
        return res[0]