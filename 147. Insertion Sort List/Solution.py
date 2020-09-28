# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        node = ListNode(0)
        node.next = head
        while head and head.next:
            if head.val < head.next.val:
                head = head.next
            else:
                node1 = node
                nodetoinsert = head.next
                while node1.next.val < nodetoinsert.val:
                    node1 = node1.next
                head.next = nodetoinsert.next
                node1.next, nodetoinsert.next = nodetoinsert, node1.next
        return node.next
