# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy, prev = head, None

        while dummy:
            nxt = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = nxt
        
        return prev
