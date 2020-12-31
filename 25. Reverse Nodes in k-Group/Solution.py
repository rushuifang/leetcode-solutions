# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(a: ListNode, b: ListNode):
            pre = None
            cur = a
            nxt = a
            while cur != b :
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        
        if head == None: return None
        a = b = head
        for _ in range(k):
            if b == None:
                return head
            b = b.next
        newHead = reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead