# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        pos_from_start = length - n

        prev = dummy
        for i in range(pos_from_start):
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next