# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        ans = []
        queue.append(root)

        while queue != []:
            last_node = None
            new_q = []
            for node in queue:
                if node:
                    new_q.append(node.left)
                    new_q.append(node.right)
                    last_node = node
            queue = new_q
            if last_node: ans.append(last_node.val)
        return ans