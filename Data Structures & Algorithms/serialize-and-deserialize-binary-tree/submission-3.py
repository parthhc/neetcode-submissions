# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        flattened = []
        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:
                flattened.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                flattened.append('n')

        return ','.join(flattened)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        flattened = data.split(',')
        if len(flattened) == 0 or flattened[0] == 'n': return None
        
        q = collections.deque()
        root = TreeNode(flattened[0])
        q.append(root)

        i = 1

        while q:
            node = q.popleft()

            if flattened[i] != 'n':
                node.left = TreeNode(int(flattened[i]))
                q.append(node.left)
            i += 1

            if flattened[i] != 'n':
                node.right = TreeNode(int(flattened[i]))
                q.append(node.right)
            i += 1
            

        return root
