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

            leftSum = 0 if leftRes < 0 else leftRes
            rightSum = 0 if rightRes < 0 else rightRes

            res[0] = max(res[0], node.val + leftSum + rightSum)

            return node.val + max(leftSum, rightSum)

        dfs(root)

        return res[0]