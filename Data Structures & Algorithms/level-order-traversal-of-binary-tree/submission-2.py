# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        q = collections.deque()
        q.append(root)
        while q:
            length = len(q)
            to_add = []
            for i in range(length):
                curr = q.popleft()
                to_add.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            ans.append(to_add)
        return ans


                    

