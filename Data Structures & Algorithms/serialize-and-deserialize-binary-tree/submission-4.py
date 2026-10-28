# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = collections.deque()
        q.append(root)

        res = []
        while q:
            node = q.popleft()
            if not node:
                res.append('N')
            else:
                q.append(node.left)
                q.append(node.right)
                res.append(str(node.val))

        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(',')
        if not arr:
            return None
        if arr[0] == 'N':
            return None

        q = collections.deque()
        root = TreeNode(int(arr[0]))
        q.append(root)
        
        i = 1
        while q:
            node = q.popleft()
            if arr[i] != 'N':
                new_node = TreeNode(int(arr[i]))
                node.left = new_node
                q.append(new_node)
            i += 1

            if arr[i] != 'N':
                new_node = TreeNode(int(arr[i]))
                node.right = new_node
                q.append(new_node)
            i += 1


        return root