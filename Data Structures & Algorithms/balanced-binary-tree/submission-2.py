# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return (True, 0)
            isLeftBalanced, leftHeight = dfs(node.left)
            isRightBalanced, rightHeight = dfs(node.right)

            return (abs(leftHeight - rightHeight) <= 1 and isLeftBalanced and isRightBalanced, 1 + max(leftHeight, rightHeight))

        return dfs(root)[0]