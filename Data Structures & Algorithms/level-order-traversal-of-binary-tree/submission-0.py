# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        soln = []
        if not root: return soln

        queue.append(root)

        while queue:
            new_q = []
            soln_to_append = []
            for node in queue:
                if node:
                    new_q.append(node.left)
                    new_q.append(node.right)
                    soln_to_append.append(node.val)
            
            if soln_to_append: soln.append(soln_to_append)
            queue = new_q

        return soln

                    

