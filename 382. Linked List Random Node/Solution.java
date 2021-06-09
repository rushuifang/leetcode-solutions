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

    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    
    private ListNode h;
    
    public Solution(ListNode head) {
        this.h = head;
    }
    
    /** Returns a random node's value. */
    public int getRandom() {
        ListNode p = this.h;
        int i = 0;
        int res = p.val;
        
        Random r = new Random();
        while (p != null) {
            if (r.nextInt(++i) == 0) {
                res = p.val;
            }
            p = p.next;
        }
        return res;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */