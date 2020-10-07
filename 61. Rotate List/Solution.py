# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or head.next is None or k == 0:
            return head
        else:
            listN = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            listN += 1
        tail.next = head
        newTail = tail
        for _ in range(listN - k % listN):
            newTail = newTail.next
        newHead = newTail.next
        newTail.next = None
        return newHead