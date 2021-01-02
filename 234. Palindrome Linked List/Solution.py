# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(head):
            prev_node = None
            
            while head:
                next_node = head.next
                head.next = prev_node
                prev_node = head
                head = next_node
            return prev_node
    
        fast = slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        fast = head
        slow = reverse(slow)
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True


# Another solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        return self.traverse(head)
        
    def traverse(self, right):
        if right == None:
            return True
        res = self.traverse(right.next) and right.val == self.left.val
        self.left = self.left.next
        return res