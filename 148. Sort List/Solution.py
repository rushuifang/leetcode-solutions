# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        mid = self.getMid(head)
        print(mid)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, list1: ListNode, list2: ListNode):
        dummyHead = ListNode()
        tail = dummyHead
        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        if list1 is None:
            tail.next = list2
        else:
            tail.next = list1
        return dummyHead.next

    def getMid(self, head: ListNode):
        midPrev = None
        while (head is not None) and (head.next is not None):
            if midPrev is None:
                midPrev = head
            else:
                midPrev = midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid