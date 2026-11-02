"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        old_to_new = {}
        tmp = head
        while tmp:
            old_to_new[tmp] = Node(tmp.val)
            tmp = tmp.next

        tmp = head
        while tmp:
            neww = old_to_new[tmp]
            neww.next = old_to_new[tmp.next] if tmp.next != None else None
            neww.random = old_to_new[tmp.random] if tmp.random != None else None
            tmp = tmp.next


        return old_to_new[head]