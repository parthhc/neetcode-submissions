/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> seenNodes = new HashSet<>();
        ListNode dummy = new ListNode(head.val, head.next);
        while (dummy != null) {
            if (seenNodes.contains(dummy)) {
                return true;
            }
            seenNodes.add(dummy);
            dummy = dummy.next;
        }
        return false;
        
    }
}
