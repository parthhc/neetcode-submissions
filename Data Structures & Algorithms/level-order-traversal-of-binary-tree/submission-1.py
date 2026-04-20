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
            num_elems = len(queue)
            temp_arr = []
            for i in range(num_elems):
                node = queue.pop(0)
                temp_arr.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            soln.append(temp_arr)

        return soln


                    

