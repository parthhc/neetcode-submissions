# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # level order traversal
        if root == None: return ''
        q = collections.deque()
        values = [str(root.val)]
        q.append(root)
        while q:
            prev_level_len = len(q)
            curr_level = []
            for i in range(prev_level_len):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    curr_level.append(str(node.left.val))
                else:
                    curr_level.append('-')
                if node.right:
                    q.append(node.right)
                    curr_level.append(str(node.right.val))
                else:
                    curr_level.append('-')
            values.extend(curr_level)

        return ','.join(values)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '': return None
        
        arr = data.split(',')

        root = TreeNode(int(arr[0]))
        q = collections.deque()
        q.append(root)
        i = 1
        while q and i < len(arr):
            node = q.popleft()

            if arr[i] != '-':
                new_node = TreeNode(int(arr[i]))
                node.left = new_node
                q.append(new_node)
            i += 1

            if arr[i] != '-':
                new_node = TreeNode(int(arr[i]))
                node.right = new_node
                q.append(new_node)
            i += 1

        return root


