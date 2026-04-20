# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class NodeWrapper:
            def __init__(self, node):
                self.val = node.val
                self.next = node.next
            
            # needed to do heap operations
            def __lt__(self, other):
                return self.val < other.val

        heap = []

        for linked_list in lists:
            if linked_list: heapq.heappush(heap, NodeWrapper(linked_list))
        
        ans = dummy = ListNode(-1)

        while heap:
            node = heapq.heappop(heap)
            dummy.next = ListNode(node.val)
            dummy = dummy.next
            if node.next:
                heapq.heappush(heap, NodeWrapper(node.next))

        return ans.next