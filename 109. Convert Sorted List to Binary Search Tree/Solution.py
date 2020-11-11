# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def convertBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(values[mid])
            root.left = convertBST(left, mid - 1)
            root.right = convertBST(mid + 1, right)
            return root

        return convertBST(0, len(values) - 1)
