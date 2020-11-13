# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        stack3 = []

        while stack1 and stack2:
            x = stack1.pop()
            y = stack2.pop()
            z = (x + y + carry) % 10
            carry = (x + y + carry) // 10
            stack3.append(z)

        while stack1:
            x = stack1.pop()
            z = (x + carry) % 10
            carry = (x + carry) // 10
            stack3.append(z)

        while stack2:
            y = stack2.pop()
            z = (y + carry) % 10
            carry = (y + carry) // 10
            stack3.append(z)

        if carry:
            stack3.append(carry)
        stack3 = stack3[::-1]
        l3 = ListNode(stack3.pop())
        while stack3:
            l3 = ListNode(stack3.pop(), l3)
        return l3
