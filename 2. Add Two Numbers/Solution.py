# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        curr = dummyHead
        p = l1
        q = l2
        carry = 0
        while p is not None or q is not None:
            if p is not None:
                x = p.val
                p = p.next
            else:
                x = 0
            if q is not None:
                y = q.val
                q = q.next
            else:
                y = 0
            z = (x + y + carry) % 10
            carry = (x + y + carry) // 10
            curr.next = ListNode(z)
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next
