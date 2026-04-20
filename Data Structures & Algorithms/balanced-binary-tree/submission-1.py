# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root == None: return [True, 0]
            left_dfs = dfs(root.left)
            right_dfs = dfs(root.right)
            return [left_dfs[0] and right_dfs[0] and abs(left_dfs[1] - right_dfs[1]) <= 1, 1 + max(right_dfs[1], left_dfs[1])]

        return dfs(root)[0]