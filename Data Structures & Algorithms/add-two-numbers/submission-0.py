# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, None)
        ref = ans
        carry = 0

        while l1 != None and l2 != None:
            ref.next = ListNode((l1.val + l2.val + carry) % 10, None)
            if (l1.val + l2.val + carry < 10):
                carry = 0
            else:
                carry = 1 
            ref = ref.next
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            ref.next = ListNode((l1.val + carry) % 10, None)
            if (l1.val + carry < 10):
                carry = 0
            else:
                carry = 1 
            ref = ref.next
            l1 = l1.next

        while l2 != None:
            ref.next = ListNode((l2.val + carry) % 10, None)
            if (l2.val + carry < 10):
                carry = 0
            else:
                carry = 1 
            ref = ref.next
            l2 = l2.next
        
        if carry != 0:
            ref.next = ListNode(carry, None)
            carry = 0

        return ans.next