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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode start = head;
        ListNode end = head;
        ListNode breakOne = head;
        
        int i = 1;
        while (i < left) {
            start = start.next;
            end = end.next;
            i++;
        }
        
        while (i < right) {
            end = end.next;
            i++;
        }
        
        int j = 1;
        while (j < left - 1) {
            breakOne = breakOne.next;
            j++;
        }
        
        ListNode breakTwo = end.next;
        end.next = null;
        ListNode revStart = reverse(start);
        ListNode revEnd = reverse(start);
        while (revEnd.next != null) {
            revEnd = revEnd.next;
        }
        revEnd.next = breakTwo;
        if (left == 1) {
            return revStart;
        }
        breakOne.next = revStart;
        return head;
    }
    
    public ListNode reverse(ListNode head) {
        ListNode pre = null;
        ListNode cur = head;
        ListNode nxt = head;
        while (cur != null) {
            nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
}