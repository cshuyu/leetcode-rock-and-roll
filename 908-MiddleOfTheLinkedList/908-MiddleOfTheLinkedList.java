// Last updated: 2/23/2026, 6:44:58 PM
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
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null) {
            fast = fast.next;
            if (fast == null) {
                // even case
                return slow;
            }
            fast = fast.next;
            slow = slow.next;
        }
        return slow;
    }
}