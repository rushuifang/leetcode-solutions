# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_head = list2_tail = list2
        list1_head = list1
        
        while list2_tail.next:
            list2_tail = list2_tail.next
            
        for _ in range(a - 1):
            list1_head = list1_head.next
            
        nxt = list1_head.next
        list1_head.next = list2_head
        list1_head = nxt
        
        for _ in range(b - a):
            list1_head = list1_head.next
        
        list2_tail.next = list1_head.next
        list1_head.next = None
        return list1
        

    #    Another one 
    class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = None
        end = list1
        for i in range(b):
            if i == a - 1:
                start = end
            end = end.next
        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end.next
        end.next = None
        return list1