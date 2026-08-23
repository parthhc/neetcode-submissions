# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def _build_inorder(node):
            if not node:
                return
            
            res = []
            left = _build_inorder(node.left)
            right = _build_inorder(node.right)

            if left:
                res += left
            res += [node.val]
            if right:
                res += right
            
            return res

        inorder = _build_inorder(root)

        return inorder[k - 1]