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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        } else if (list2 == null) {
            return list1;
        }

        ListNode listA = new ListNode(list1.val, list1.next);
        ListNode listB = new ListNode(list2.val, list2.next);
        ListNode output = new ListNode(-1);
        ListNode dummy = output;
        while (listA != null && listB != null) {
            if (listA.val < listB.val) {
                dummy.next = listA;
                listA = listA.next;
            } else {
                dummy.next = listB;
                listB = listB.next;
            }
            dummy = dummy.next;
        }
        if (listA != null) {
            dummy.next = listA;
        } else {
            dummy.next = listB;
        }
        return output.next;
    }
}