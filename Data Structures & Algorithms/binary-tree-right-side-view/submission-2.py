# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        q = collections.deque()
        ans = []
        q.append(root)

        while q:
            level_len = len(q)
            for i in range(level_len):
                curr = q.popleft()
                if i == level_len - 1: ans.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
        
        return ans