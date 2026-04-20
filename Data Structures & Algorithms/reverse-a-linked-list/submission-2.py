# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        new_head = head
        prev = None
        while new_head != None:
            next_node = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = next_node

        return prev