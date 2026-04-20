# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ",".join(res)
                
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data[0] == "N": return None
        arr = data.split(",")

        q = collections.deque()
        root = TreeNode(int(arr[0]))
        q.append(root)
        i = 1
        while q and i < len(arr):
            node = q.popleft()
            if arr[i] != "N":
                node.left = TreeNode(int(arr[i]))
                q.append(node.left)
            i += 1
            if arr[i] != "N":
                node.right = TreeNode(int(arr[i]))
                q.append(node.right)
            i += 1
        
        return root



